import random
import time

class participant:
    def __init__(self, controlable, hp, item):
        self.controlable = controlable
        self.hp = hp
        self.item = item
        self.item_queen = 0
        self.blood_queen = 0

class computer(participant):
    def __init__(self, hp, item):
        participant.__init__(self, False, hp, item)
        self.handcuff = False
        self.bullet_pattern = []
        self.known_live = 0
        self.known_blank = 0
        self.max_item = 8
    def dohandcuff(self):
        self.handcuff = True
    def unhandcuff(self):
        self.handcuff = False
    def reset_bullet_pattern(self,number):
        self.bullet_pattern = []
        for i in range(number):
            self.bullet_pattern.append('unknown')
        self.known_live = 0
        self.known_blank = 0
    def set_bullet_pattern(self,poition,value):
        self.bullet_pattern[poition] = value
        if value == 'live':
            self.known_live += 1
        else:
            self.known_blank += 1
    def pop_bullet_pattern(self):
        if self.bullet_pattern.pop(0) == 'live':
            self.known_live -=1
        else:
            self.known_blank -=1

class player(participant):
    def __init__(self, hp, item, money = 0):
        participant.__init__(self, True, hp, item)
        self.handcuff = False
        self.money = money
        self.max_item = 8
        self.queen_used = []
    def dohandcuff(self):
        self.handcuff = True
    def unhandcuff(self):
        self.handcuff = False

class game:
    def __init__(self, player, computer, hp, risk):
        self.player = player
        self.computer = computer
        self.player.hp = hp
        self.computer.hp = hp
        self.round = 1
        self.item_list = ['放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素']
        self.special_item = ['未知藍圖','禁藥','大口徑子彈','榴彈砲','彈藥包']
        self.queen = ['漆黑皇后','神聖皇后','蔚藍皇后','腥紅皇后'] 
        if risk == 1:
            self.item_list = ['放大鏡','香菸','手鋸','啤酒','手銬','手機','轉換器','過期藥物','腎上腺素','禁藥','大口徑子彈','榴彈砲','彈藥包']
            if random.randint(0,1):
                print('高風險模式，血量大幅提升')
                health = random.randint(3,10)
                self.player.hp += health
                self.computer.hp += health
        print('遊戲開始,每人有',self.player.hp,'點血量')

    def give_participant_item(self,number,participant):
        for i in range(number):
            if len(participant.item) < participant.max_item:
                time.sleep(1)
                self.item_list.append('未知藍圖')
                item=self.item_list[random.randint(0,len(self.item_list)-1)]
                self.item_list.remove('未知藍圖')
                print('你' if participant.controlable else '莊家','獲得了',item)
                participant.item.append(item)
                
            else:
                print('物品欄已滿')

    def give_item(self,number):
        for i in range(number):
            if len(self.player.item) < self.player.max_item:
                chance = random.randint(1,100)
                if (chance <= 20) and (self.player.item.count('未知藍圖') == 0):
                    item='未知藍圖'
                    if (random.randint(1,4) == 4) and (risk == 1):
                        item=self.queen[random.randint(0,len(self.queen)-1)]
                        print('***你獲得了 ',item,' ***')
                    else:
                        print('你獲得了',item)
                    self.player.item.append(item)
                elif (chance > 95):
                    while True:
                        chance = random.randint(1,100)
                        if chance <= 20:
                            if ('神聖皇后' in self.player.queen_used) & (bool(random.randint(0,1))):
                                continue
                            item='神聖皇后'
                            print('***你獲得了 神聖皇后 ***')
                            self.player.item.append(item)    
                        elif chance <= 45:
                            if ('蔚藍皇后' in self.player.queen_used) & (bool(random.randint(0,1))):
                                continue
                            item='蔚藍皇后'
                            print('***你獲得了 蔚藍皇后 ***')
                            self.player.item.append(item)
                        elif chance <= 70:
                            item='腥紅皇后'
                            print('***你獲得了 腥紅皇后 ***')
                            self.player.item.append(item)
                        else:
                            item='漆黑皇后'
                            print('***你獲得了 漆黑皇后 ***')
                            self.player.item.append(item)
                        break

                else:
                    item=self.item_list[random.randint(0,len(self.item_list)-1)]
                    print('你獲得了',item)
                    self.player.item.append(item)
            else:
                print('你的物品欄已滿')
            if len(self.computer.item) < self.computer.max_item:
                chance = random.randint(1,20)
                if chance == 20:
                    item='未知藍圖'
                    self.computer.item.append(item)
                elif (chance == 19) and (risk == 1):
                    item='未知藍圖'
                    self.computer.item.append(item)
                else:
                    self.computer.item.append(self.item_list[random.randint(0,len(self.item_list)-1)])
                
    def computer_bonus(self,bonus_number):
        self.computer.item.append(self.item_list[random.randint(0,len(self.item_list)-1)])
        if (bonus_number+1) % 2 == 0:
            self.computer.hp += 1
            print('莊家的血量增加了一點')
        if (bonus_number+1) % 10 == 0:
            self.computer.item.pop(0)
            self.computer.item.append('未知藍圖')
            

    def one_round(self,live_bullet,blank,item_number):
        time.sleep(3)
        print('第',self.round,'局開始')
        if self.player.handcuff:
            self.player.unhandcuff()
            print('你的手銬解除,可以自由行動了')
        if self.computer.handcuff:
            self.computer.unhandcuff()
            print('莊家的手銬解除,可以自由行動了')
        handsaw = False
        skip = False    
        killer_queen = False
        self.give_item(item_number)
        remain_bullet = []
        self.computer.reset_bullet_pattern(live_bullet+blank)
        print('這局有',live_bullet,'發實彈',blank,'發空包彈')
        for i in range(live_bullet):
            remain_bullet.append(True)
        for i in range(blank):
            remain_bullet.append(False)
        random.shuffle(remain_bullet)
        time.sleep(2)
        while len(remain_bullet) > 0:
            skip = False
            try_count = 0
            not_blue_print = True

            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            
            time.sleep(1)
            print('==========================================')
            print('你的回合')
            print('你的物品欄:',self.player.item)
            print('玩家血量:',self.player.hp,'莊家血量:',self.computer.hp)  
            print('剩餘',live_bullet,'發實彈',blank,'發空包彈')
            print('請選擇要做的事')
            print('1.射向莊家, 2.射向自己, 3.使用物品, 4.顯示莊家物品欄')
            if self.player.blood_queen > 0 and (handsaw==False):
                print('腥紅皇后使你獲得手鋸效果')
                time.sleep(1)
                handsaw = True
                self.player.blood_queen -= 1
            while True:
                action = int(input())
                if type(action) != int:
                    print('請輸入正確的數字')
                    continue
                if action < 1 or action > 4:
                    print('請輸入正確的數字')
                    continue
                break
            if action==1:
                if remain_bullet[0]&handsaw&killer_queen:
                    self.computer.hp -= 10
                    print('你使用漆黑皇后射中了莊家,造成十點傷害')
                    if self.computer.blood_queen > 0:
                        print('腥紅皇后使莊家免疫額外傷害')
                        self.computer.hp += 5
                        self.computer.blood_queen -= 1
                    else:
                        print('節哀順變')
                    handsaw = False
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&killer_queen:
                    self.computer.hp -= 5
                    print('你使用漆黑皇后射中了莊家,造成五點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                    killer_queen = False
                elif remain_bullet[0]&handsaw:
                    self.computer.hp -= 2
                    print('你射中了莊家,造成兩點傷害')
                    if self.computer.blood_queen > 0:
                        print('腥紅皇后使莊家免疫額外傷害')
                        self.computer.hp += 1
                        self.computer.blood_queen -= 1
                    handsaw = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]:
                    self.computer.hp -= 1
                    print('你射中了莊家,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                else:
                    print('你的子彈打空了')
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    handsaw = False
                remain_bullet.pop(0)
            elif action==2:
                if remain_bullet[0]&handsaw&killer_queen:
                    self.player.hp -= 10
                    print('你用漆黑皇后射中了自己,造成十點傷害')
                    if self.player.blood_queen > 0:
                        print('腥紅皇后使你免疫額外傷害')
                        self.player.hp += 5
                        self.player.blood_queen -= 1
                    else:
                        print('節哀順變')
                    handsaw = False
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&killer_queen:
                    self.player.hp -= 5
                    print('你用漆黑皇后射中了自己,造成五點傷害')
                    print('節哀順變')
                    killer_queen = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]&handsaw:
                    self.player.hp -= 2
                    print('你射中了自己,造成兩點傷害')
                    if self.player.blood_queen > 0:
                        print('腥紅皇后使你免疫額外傷害')
                        self.player.hp += 1
                        self.player.blood_queen -= 1
                    else:
                        print('你是笨蛋嗎?')
                    handsaw = False
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                elif remain_bullet[0]:
                    self.player.hp -= 1
                    print('你射中了自己,造成一點傷害')
                    self.computer.pop_bullet_pattern()
                    live_bullet -= 1
                else:
                    print('你的子彈打空了,額外獲得一回合')
                    remain_bullet.pop(0)
                    self.computer.pop_bullet_pattern()
                    blank -= 1
                    continue
                remain_bullet.pop(0)
            elif action==3:
                print('請選擇要使用的物品')
                for i in range(len(self.player.item)):
                    print(i+1,'.',self.player.item[i])
                item = int(input())
                if item > len(self.player.item):    
                    print('請輸入正確的數字')
                    continue
                if self.player.item[item-1] == '手鋸':
                    handsaw = True
                    print('你使用了手鋸,下一發子彈造成兩倍傷害')
                elif self.player.item[item-1] == '啤酒':
                    if remain_bullet.pop(0):
                        print('你使用了啤酒,退掉一發實彈')
                        live_bullet -= 1
                    else:
                        print('你使用了啤酒,退掉一發空包彈')
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                elif self.player.item[item-1] == '手機':
                    print('你使用了手機')
                    if len(remain_bullet) == 1:
                        n = 0
                    else:
                        n=random.randint(1,len(remain_bullet)-1)
                    if remain_bullet[n]:
                        print('第',n+1,'發是實彈')
                    else:
                        print('第',n+1,'發是空包彈')
                elif self.player.item[item-1] == '轉換器':
                    print('你使用了轉換器,現在這發子彈將反轉')
                    remain_bullet[0] = not remain_bullet[0]
                    if remain_bullet[0]:
                        live_bullet += 1
                        blank -= 1
                    else:
                        live_bullet -= 1
                        blank += 1
                elif self.player.item[item-1] == '過期藥物':
                    print('你使用了過期藥物')
                    if random.randint(0,1):
                        self.player.hp += 2
                        print('你回復了兩點血量')
                    else:
                        self.player.hp -= 1
                        print('你失去了一點血量')
                        if self.player.hp <= 0:
                            time.sleep(2)
                            print('**************************************')
                            print('你死了')
                            time.sleep(2)
                            return
                elif self.player.item[item-1] == '放大鏡':
                    print('你使用了放大鏡看到 ','實彈' if remain_bullet[0] else '空包彈')
                elif self.player.item[item-1] == '香菸':
                    print('你使用了香菸,回復一點血量')
                    self.player.hp += 1
                elif self.player.item[item-1] == '手銬':
                    print('你使用了手銬,莊家下回合無法行動')
                    self.computer.dohandcuff()
                elif self.player.item[item-1] == '未知藍圖':
                    if self.player.item.count('過期藥物') >= 3:
                        print('你獲得了禁藥')
                        self.player.item.append('禁藥')
                        for i in range(3):
                            self.player.item.remove('過期藥物')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('手鋸') >= 2) and  (self.player.item.count('放大鏡') >= 1):
                        print('你獲得了大口徑子彈')
                        self.player.item.append('大口徑子彈')
                        for i in range(2):
                            self.player.item.remove('手鋸')
                        self.player.item.remove('放大鏡')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('大口徑子彈') >= 1) and (self.player.item.count('腎上腺素') >= 1) and (self.player.item.count('轉換器') >= 1):
                        print('你獲得了榴彈砲')
                        self.player.item.append('榴彈砲')
                        self.player.item.remove('腎上腺素')
                        self.player.item.remove('大口徑子彈')
                        self.player.item.remove('轉換器')
                        self.player.item.remove('未知藍圖')
                    elif (self.player.item.count('啤酒') >= 2) and (self.player.item.count('香菸') >= 1) and ((live_bullet+blank) >= 3):
                        print('你獲得了彈藥包')
                        self.player.item.remove('啤酒')
                        self.player.item.remove('啤酒')
                        self.player.item.remove('香菸')
                        self.player.item.append('彈藥包')
                        self.player.item.remove('未知藍圖')
                    elif len(self.player.item) == self.player.max_item:
                        print('你獲得了擴增背包,物品欄增加2格')
                        self.player.item = []
                        self.player.max_item += 2
                    else:
                        print('你的物品不足以合成')
                        continue
                    not_blue_print = False
                elif self.player.item[item-1] == '禁藥':
                    #70%機率血量翻倍並+3，30%血量降低到1點，若血量為1則死亡
                    print('你使用了禁藥')
                    if random.randint(1,10) <= 7:
                        self.player.hp *= 2
                        self.player.hp += 3
                        print('你的血量大幅提升,現在血量為',self.player.hp)
                    else:
                        if self.player.hp == 1:
                            print('你死了')
                            time.sleep(2)
                            return
                        self.player.hp = 1
                        print('你中毒了，血量降為1')
                elif self.player.item[item-1] == '大口徑子彈':
                    #將目前這發直接子彈替換成大口徑子彈並直接發射，造成3點傷害，如果有使用手鋸則造成6點傷害
                    if handsaw:
                        self.computer.hp -= 6
                        print('你發射了大口徑子彈,造成6點傷害')
                    else:
                        self.computer.hp -= 3
                        print('你發射了大口徑子彈,造成3點傷害')
                    if remain_bullet.pop(0):
                        live_bullet -= 1
                    else:
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    self.player.item.pop(item-1)
                    skip = True
                    handsaw = False
                elif self.player.item[item-1] == '榴彈砲':
                    #將自身血量降低至1點，並發射現在這發子彈，若為實彈則造成(降低的血量+1)點傷害，使用手鋸則造成兩倍傷害，若為空包彈則不造成傷害，使用後輪到莊家的回合
                    damage = self.player.hp
                    self.player.hp = 1
                    if remain_bullet.pop(0):
                        if handsaw:
                            self.computer.hp -= 2*damage
                            print('你發射了榴彈砲,造成',2*damage,'點傷害')
                            handsaw = False
                        else:
                            self.computer.hp -= damage
                            print('你發射了榴彈砲,造成',damage,'點傷害')
                        live_bullet -= 1
                    else:
                        print('你發射了榴彈砲,但是子彈打空了')
                        blank -= 1
                    self.computer.pop_bullet_pattern()
                    self.player.item.pop(item-1)
                    skip = True
                elif self.player.item[item-1] == '彈藥包':
                    #對莊家造成剩餘實彈數量的傷害，之後用實彈和空包彈隨機將彈藥填滿至8發
                    damage = live_bullet
                    self.computer.hp -= damage
                    print('你使用了彈藥包,對莊家造成',damage,'點傷害')
                    remain_bullet = []
                    live_bullet = 0
                    blank = 0
                    for i in range(8-len(remain_bullet)):
                        if random.randint(0,1):
                            remain_bullet.append(True)
                            live_bullet += 1
                        else:
                            remain_bullet.append(False)
                            blank += 1
                    random.shuffle(remain_bullet)
                    print('彈藥已重新裝填')
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                elif self.player.item[item-1] == '漆黑皇后':
                    #移除雙方所有道具，將彈夾裝填為一發空包彈一發實彈，這發實彈將造成5點傷害
                    print('你使用了漆黑皇后，彈藥裝填為一發空包彈一發5點傷害實彈，祈禱吧!')
                    self.player.item = []
                    self.computer.item = []
                    remain_bullet = [True,False]
                    live_bullet = 1
                    blank = 1
                    self.computer.reset_bullet_pattern(live_bullet+blank)
                    random.shuffle(remain_bullet)
                    killer_queen = True
                    not_blue_print = False
                    self.player.queen_used.append('漆黑皇后')
                elif self.player.item[item-1] == '神聖皇后':
                    #回3點血量，背包上限+2，獲得3個隨機物品
                    print('你使用了神聖皇后，回復3點血量，背包上限+2，獲得3個隨機物品')
                    self.player.hp += 3
                    self.player.max_item += 3
                    self.give_participant_item(3,self.player)
                    self.player.max_item -= 1
                    self.player.queen_used.append('神聖皇后')
                elif self.player.item[item-1] == '蔚藍皇后':
                    #玩家的回合結束時，獲得一個隨機物品
                    print('你使用了蔚藍皇后，輪到莊家的回合時你將獲得一個隨機物品')
                    self.player.item_queen += 1   
                    self.player.queen_used.append('蔚藍皇后')
                elif self.player.item[item-1] == '腥紅皇后':
                    #玩家的回合開始時，附加手鉅效果
                    print('你使用了腥紅皇后，每回合獲得手鋸效果並免疫手鉅的額外傷害，可以觸發五次')
                    self.player.blood_queen += 5       
                    self.player.queen_used.append('腥紅皇后')                             
                elif self.player.item[item-1] == '腎上腺素':
                    print('你使用了腎上腺素,可以偷取莊家的物品')
                    if len(self.computer.item) == 0:
                        print('莊家沒有物品可以偷取')
                        continue
                    print('請選擇要偷取的物品:')
                    for i in range(len(self.computer.item)):
                        print(i+1,'.',self.computer.item[i])
                    steal = int(input())
                    #馬上使用選擇的物品 
                    if self.computer.item[steal-1] == '手鋸':
                        handsaw = True
                        print('你使用了手鋸,下一發子彈造成兩倍傷害')
                    elif self.computer.item[steal-1] == '啤酒':
                        if remain_bullet.pop(0):
                            print('你使用了啤酒,退掉一發實彈')
                            live_bullet -= 1
                        else:
                            print('你使用了啤酒,退掉一發空包彈')
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                    elif self.computer.item[steal-1] == '手機':
                        print('你使用了手機')
                        if len(remain_bullet) == 1:
                            n = 0
                        else:
                            n=random.randint(1,len(remain_bullet)-1)
                        if remain_bullet[n]:
                            print('第',n+1,'發是實彈')
                        else:
                            print('第',n+1,'發是空包彈')
                    elif self.computer.item[steal-1] == '轉換器':
                        print('你使用了轉換器,現在這發子彈將反轉')
                        remain_bullet[0] = not remain_bullet[0]
                        if remain_bullet[0]:
                            live_bullet += 1
                            blank -= 1
                        else:
                            live_bullet -= 1
                            blank += 1
                    elif self.computer.item[steal-1] == '過期藥物':
                        print('你使用了過期藥物')
                        if random.randint(0,1):
                            self.player.hp += 2
                            print('你回復了兩點血量')
                        else:
                            self.player.hp -= 1
                            print('你失去了一點血量')
                            if self.player.hp <= 0:
                                time.sleep(2)
                                print('**************************************')
                                print('你死了')
                                time.sleep(2)
                                return
                    elif self.computer.item[steal-1] == '放大鏡':
                        print('你使用了放大鏡看到 ','實彈' if remain_bullet[0] else '空包彈')
                    elif self.computer.item[steal-1] == '香菸':
                        print('你使用了香菸,回復一點血量')
                        self.player.hp += 1
                    elif self.computer.item[steal-1] == '手銬':
                        print('你使用了手銬,莊家下回合無法行動')
                        self.computer.dohandcuff()
                    elif self.computer.item[steal-1] == '未知藍圖':
                        self.player.item.append('未知藍圖')
                        print('你獲得了未知藍圖')
                    elif self.computer.item[steal-1] == '禁藥':
                        print('你使用了禁藥')
                        if random.randint(1,10) <= 7:
                            self.player.hp *= 2
                            self.player.hp += 3
                            print('你的血量大幅提升,現在血量為',self.player.hp)
                        else:
                            if self.player.hp == 1:
                                print('你死了')
                                time.sleep(2)
                                return
                            self.player.hp = 1
                            print('你中毒了，血量降為1')
                    elif self.computer.item[steal-1] == '大口徑子彈':
                        if handsaw:
                            self.computer.hp -= 6
                            print('你使用了大口徑子彈,造成6點傷害')
                        else:
                            self.computer.hp -= 3
                            print('你使用了大口徑子彈,造成3點傷害')
                        if remain_bullet.pop(0):
                            live_bullet -= 1
                        else:
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    elif self.computer.item[steal-1] == '榴彈砲':
                        damage = self.player.hp 
                        self.player.hp = 1
                        if remain_bullet.pop(0):
                            if handsaw:
                                self.computer.hp -= 2*damage
                                print('你使用了榴彈砲,造成',2*damage,'點傷害')
                                handsaw = False
                            else:
                                self.computer.hp -= damage
                                print('你使用了榴彈砲,造成',damage,'點傷害')
                            live_bullet -= 1
                        else:
                            print('你使用了榴彈砲,但是子彈打空了')
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                    elif self.computer.item[steal-1] == '彈藥包':
                        damage = live_bullet
                        self.computer.hp -= damage
                        print('你使用了彈藥包,對莊家造成',damage,'點傷害')
                        remain_bullet = []
                        live_bullet = 0
                        blank = 0
                        for i in range(8-len(remain_bullet)):
                            if random.randint(0,1):
                                remain_bullet.append(True)
                                live_bullet += 1
                            else:
                                remain_bullet.append(False)
                                blank += 1
                        random.shuffle(remain_bullet)
                        print('彈藥已重新裝填')
                        self.computer.reset_bullet_pattern(live_bullet+blank)
                        
                    elif self.computer.item[steal-1] == '腎上腺素':
                        print('你不能偷取腎上腺素')
                        continue
                    self.computer.item.pop(steal-1)

                if not_blue_print and not skip: 
                    self.player.item.pop(item-1)
                time.sleep(2)
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if not skip:
                    continue
            elif action==4:
                print('莊家的物品欄:',self.computer.item)
                continue
            if self.computer.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你贏了')
                time.sleep(2)
                return
            if self.player.hp <= 0:
                time.sleep(2)
                print('**************************************')
                print('你死了')
                time.sleep(2)
                return
            if len(remain_bullet) == 0:
                print('子彈打完了')
                print('進入下一局')
                return
            if self.player.item_queen > 0:
                print('蔚藍皇后使你獲得隨機物品')
                time.sleep(1)
            for i in range(self.player.item_queen):
                self.give_participant_item(1,self.player)
            print('==========================================')
            print('莊家的回合')
            print('==========================================')
            time.sleep(1)
            try_count = 0
            not_blue_print = True
            if self.computer.item.count('腥紅皇后') > 0 & (not handsaw):
                print('腥紅皇后使莊家獲得手鋸效果')
                time.sleep(1)
                handsaw = True
                self.computer.blood_queen -= 1
            #莊家進行剩餘子彈分析
            if (live_bullet-self.computer.known_live) <= 0:
                for i in range(len(self.computer.bullet_pattern)):
                    if self.computer.bullet_pattern[i] == 'unknown':
                        self.computer.set_bullet_pattern(i,'blank')
            elif (blank-self.computer.known_blank) <= 0:
                for i in range(len(self.computer.bullet_pattern)):
                    if self.computer.bullet_pattern[i] == 'unknown':
                        self.computer.set_bullet_pattern(i,'live')

            if self.computer.handcuff:
                print('莊家被手銬銬住了,無法行動')
                self.computer.unhandcuff()
                continue

            skip = False
            not_blue_print = True

            while True:
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    return
                time.sleep(2)
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                #莊家的行動判斷
                if len(self.computer.item) > 2 :
                    if try_count >= 3:
                        action = random.randint(1,2)
                        if self.computer.bullet_pattern[0] == 'live':
                            action = 1
                        elif self.computer.bullet_pattern[0] == 'blank':
                            action = 2
                    elif random.randint(1,4) == 4:
                        action = random.randint(1,2)
                    else:
                        action = 3
                elif self.computer.bullet_pattern[0] == 'live':
                    action = 1
                elif self.computer.bullet_pattern[0] == 'blank':
                    action = 2
                elif len(self.computer.item) == 0:
                    action = random.randint(1,2)
                else:
                    action = random.randint(1,3)
                if (live_bullet > blank) & (action == 2):
                    action = 1
                
                if (self.computer.bullet_pattern[0] == 'blank') & ('轉換器' in self.computer.item):
                    print('莊家使用了轉換器,現在這發子彈將反轉')
                    remain_bullet[0] = True
                    live_bullet += 1
                    blank -= 1
                    self.computer.bullet_pattern[0] = 'live'
                    self.computer.item.remove('轉換器')
                    time.sleep(2)
                    continue
                if (self.computer.bullet_pattern[0] == 'live') & ('手鋸' in self.computer.item) and not handsaw:  
                    handsaw = True
                    print('莊家使用了手鋸,下一發子彈造成兩倍傷害')
                    time.sleep(2)
                    self.computer.item.remove('手鋸')
                    action = 1
                if '未知藍圖' in self.computer.item:
                    #馬上使用未知藍圖
                    print('莊家使用了未知藍圖')
                    time.sleep(2)
                    temp = random.randint(1,5)
                    if temp == 1:
                        print('莊家獲得了禁藥')
                        
                        self.computer.item.append('禁藥')
                    elif temp == 2:
                        print('莊家獲得了大口徑子彈')
                        
                        self.computer.item.append('大口徑子彈')
                    elif temp == 3:
                        print('莊家獲得了榴彈砲')
                        
                        self.computer.item.append('榴彈砲')
                    elif temp == 4:
                        print('莊家獲得了彈藥包')
                        
                        self.computer.item.append('彈藥包')
                    elif temp == 5:
                        print('莊家獲得了擴增背包')
                        
                        self.computer.max_item += 1
                    self.computer.item.remove('未知藍圖')
                    time.sleep(2)
                    continue
                    
                #莊家的行動選項和玩家相同
                if action==1:
                    try_count = 0
                    if remain_bullet[0]&handsaw&killer_queen:
                        self.player.hp -= 10
                        print('莊家使用漆黑皇后射中了你,造成十點傷害')
                        if self.player.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.player.hp += 5
                            self.player.blood_queen -= 1
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&killer_queen:
                        self.player.hp -= 5
                        print('莊家使用漆黑皇后射中了你,造成五點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        killer_queen = False
                    elif remain_bullet[0]&handsaw:
                        self.player.hp -= 2
                        print('莊家射中了你,造成兩點傷害')
                        if self.player.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.player.hp += 1
                            self.player.blood_queen -= 1
                        handsaw = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]:
                        self.player.hp -= 1
                        print('莊家射中了你,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    else:
                        print('莊家的子彈打空了')
                        blank -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    remain_bullet.pop(0)
                elif action==2:
                    try_count = 0
                    if remain_bullet[0]&handsaw&killer_queen:
                        self.computer.hp -= 10
                        print('莊家使用漆黑皇后射中了自己,造成十點傷害')
                        if self.computer.blood_queen > 0:
                            print('腥紅皇后使你免疫額外傷害')
                            self.computer.hp += 5
                            self.computer.blood_queen -= 1
                        else:
                            print('你逃過了一截')
                        handsaw = False
                        killer_queen = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]&killer_queen:
                        self.computer.hp -= 5
                        print('莊家使用漆黑皇后射中了自己,造成五點傷害')
                        print('你逃過了一截')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        killer_queen = False
                    elif remain_bullet[0]&handsaw:
                        self.computer.hp -= 2
                        print('莊家射中了自己,造成兩點傷害')
                        if self.computer.blood_queen > 0:
                            print('腥紅皇后使莊家免疫額外傷害')
                            self.computer.hp += 1
                            self.computer.blood_queen -= 1
                        else:
                            print('莊家是笨蛋嗎笑死')
                        handsaw = False
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                    elif remain_bullet[0]:
                        self.computer.hp -= 1
                        print('莊家射中了自己,造成一點傷害')
                        live_bullet -= 1
                        self.computer.pop_bullet_pattern()
                        handsaw = False
                    else:
                        print('莊家射向自己，子彈打空了,額外獲得一回合')
                        remain_bullet.pop(0)
                        self.computer.pop_bullet_pattern()
                        blank -= 1
                        handsaw = False
                        continue
                    remain_bullet.pop(0)
                elif action==3:
                    item = random.randint(0,len(self.computer.item)-1)
                    if (self.computer.item[item] == '啤酒') & (self.computer.bullet_pattern[0]=='live'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手銬') & self.player.handcuff:
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '過期藥物') & (self.computer.hp == 1):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手機') & (len(remain_bullet) <= 2):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手鋸') & handsaw:
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手鋸') & (self.computer.bullet_pattern[0] == 'blank'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '榴彈砲') & (self.computer.bullet_pattern[0] == 'blank'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '放大鏡') & (self.computer.bullet_pattern[0] != 'unknown'):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '手機') & ('unknown' not in self.computer.bullet_pattern):
                        try_count +=1
                        continue
                    if (self.computer.item[item] == '轉換器') & (self.computer.bullet_pattern[0] == 'unknown'):
                        try_count +=1
                        continue
                    try_count = 0
                    if self.computer.item[item] == '手鋸':
                        handsaw = True
                        print('莊家使用了手鋸,下一發子彈造成兩倍傷害')
                    elif self.computer.item[item] == '啤酒':
                        if remain_bullet.pop(0):
                            print('莊家使用了啤酒,退掉一發實彈')
                            live_bullet -= 1
                            self.computer.pop_bullet_pattern()
                        else:
                            print('莊家使用了啤酒,退掉一發空包彈')
                            blank -= 1
                            self.computer.pop_bullet_pattern()
                        if len(remain_bullet) == 0:
                            print('子彈打完了')
                            print('進入下一局')
                            return
                    elif self.computer.item[item] == '手機':
                        print('莊家使用了手機')
                        if len(remain_bullet) == 1:
                            n = 0
                        else:
                            n=random.randint(1,len(remain_bullet)-1)
                        if remain_bullet[n]:
                            self.computer.set_bullet_pattern(n,'live')
                        else:
                            self.computer.set_bullet_pattern(n,'blank')
                    elif self.computer.item[item] == '轉換器':
                        print('莊家使用了轉換器,現在這發子彈將反轉')
                        remain_bullet[0] = not remain_bullet[0]
                        if remain_bullet[0]:
                            live_bullet += 1
                            blank -= 1
                        else:
                            live_bullet -= 1
                            blank += 1
                        if self.computer.bullet_pattern[0] == 'live':
                            self.computer.set_bullet_pattern(0,'blank')
                        elif self.computer.bullet_pattern[0] == 'blank':
                            self.computer.set_bullet_pattern(0,'live')
                    elif self.computer.item[item] == '過期藥物':
                        print('莊家使用了過期藥物')
                        if random.randint(0,1):
                            self.computer.hp += 2
                            print('莊家回復了兩點血量')
                        else:
                            self.computer.hp -= 1
                            print('莊家失去了一點血量')
                            if self.computer.hp <= 0:
                                time.sleep(2)
                                print('**************************************')
                                print('你贏了')
                                time.sleep(2)
                                return
                    elif self.computer.item[item] == '放大鏡':
                        print('莊家使用了放大鏡')
                        self.computer.set_bullet_pattern(0,'live' if remain_bullet[0] else 'blank')
                    elif self.computer.item[item] == '香菸':
                        print('莊家使用了香菸,回復一點血量')
                        self.computer.hp += 1
                    elif self.computer.item[item] == '手銬':
                        print('莊家使用了手銬,你下回合無法行動')
                        self.player.dohandcuff()
                    elif self.computer.item[item] == '未知藍圖':
                        print('莊家使用了未知藍圖')
                        time.sleep(2)
                        temp = random.randint(1,5)
                        if temp == 1:
                            print('莊家獲得了禁藥')
                            self.computer.item.pop(item)
                            self.computer.item.append('禁藥')
                        elif temp == 2:
                            print('莊家獲得了大口徑子彈')
                            self.computer.item.pop(item)
                            self.computer.item.append('大口徑子彈')
                        elif temp == 3:
                            print('莊家獲得了榴彈砲')
                            self.computer.item.pop(item)
                            self.computer.item.append('榴彈砲')
                        elif temp == 4:
                            print('莊家獲得了彈藥包')
                            self.computer.item.pop(item)
                            self.computer.item.append('彈藥包')
                        elif temp == 5:
                            print('莊家獲得了擴增背包')
                            self.computer.item.pop(item)
                            self.computer.max_item += 1
                    elif self.computer.item[item] == '禁藥':
                        print('莊家使用了禁藥')
                        if random.randint(1,10) <= 7:
                            self.computer.hp *= 2
                            self.computer.hp += 3
                            print('莊家的血量大幅提升,現在血量為',self.computer.hp)
                        else:
                            if self.computer.hp == 1:
                                print('莊家中毒身亡，你贏了')
                                time.sleep(2)
                                return
                            self.computer.hp = 1
                            print('莊家中毒了，血量降為1')    
                    elif self.computer.item[item] == '大口徑子彈':
                        self.computer.item.pop(item)
                        if handsaw:
                            self.player.hp -= 6
                            print('莊家使用了大口徑子彈,造成6點傷害')
                        else:
                            self.player.hp -= 3
                            print('莊家使用了大口徑子彈,造成3點傷害')
                        if remain_bullet.pop(0):
                            live_bullet -= 1
                        else:
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        skip = True
                        handsaw = False
                    elif self.computer.item[item] == '榴彈砲':
                        self.computer.item.pop(item)
                        damage = self.computer.hp 
                        self.computer.hp = 1
                        if remain_bullet.pop(0):
                            if handsaw:
                                self.player.hp -= 2*damage
                                print('莊家使用了榴彈砲,造成',2*damage,'點傷害')
                                handsaw = False
                            else:
                                self.player.hp -= damage
                                print('莊家使用了榴彈砲,造成',damage,'點傷害')
                            live_bullet -= 1
                        else:
                            print('莊家使用了榴彈砲,但是子彈打空了')
                            blank -= 1
                        self.computer.pop_bullet_pattern()
                        skip = True
                    elif self.computer.item[item] == '彈藥包':
                        damage = live_bullet
                        self.player.hp -= damage
                        print('莊家使用了彈藥包,對你造成',damage,'點傷害')
                        remain_bullet = []
                        live_bullet = 0
                        blank = 0
                        for i in range(8-len(remain_bullet)):
                            if random.randint(0,1):
                                remain_bullet.append(True)
                                live_bullet += 1
                            else:
                                remain_bullet.append(False)
                                blank += 1
                        random.shuffle(remain_bullet)
                        print('彈藥已重新裝填')
                        self.computer.reset_bullet_pattern(live_bullet+blank)

                    elif self.computer.item[item] == '腎上腺素':   
                        self.computer.item.pop(item) 
                        print('莊家使用了腎上腺素,可以偷取你的物品')
                        if len(self.player.item) == 0:
                            print('你沒有物品可以偷取')
                            continue
                        #隨機偷取玩家的一件物品，馬上使用偷取的物品
                        item = random.randint(0,len(self.player.item)-1)
                        if self.player.item[item] == '手鋸':
                            handsaw = True
                            print('莊家偷走了手鋸,下一發子彈造成兩倍傷害')
                        elif self.player.item[item] == '啤酒':
                            if remain_bullet.pop(0):
                                print('莊家偷走了啤酒,退掉一發實彈')
                                live_bullet -= 1
                                self.computer.pop_bullet_pattern()
                            else:
                                print('莊家偷走了啤酒,退掉一發空包彈')
                                blank -= 1
                                self.computer.pop_bullet_pattern()
                            if len(remain_bullet) == 0:
                                print('子彈打完了')
                                print('進入下一局')
                                return
                        elif self.player.item[item] == '手機':
                            print('莊家偷走了手機')
                            if len(remain_bullet) == 1:
                                n = 0
                            else:
                                n=random.randint(1,len(remain_bullet)-1)
                            if remain_bullet[n]:
                                self.computer.set_bullet_pattern(n,'live')
                            else:
                                self.computer.set_bullet_pattern(n,'blank')
                        elif self.player.item[item] == '轉換器':
                            print('莊家偷走了轉換器,現在這發子彈將反轉')
                            remain_bullet[0] = not remain_bullet[0]
                            if remain_bullet[0]:
                                live_bullet += 1
                                blank -= 1
                            else:
                                live_bullet -= 1
                                blank += 1
                            if self.computer.bullet_pattern[0] == 'live':
                                self.computer.set_bullet_pattern(0,'blank')
                            elif self.computer.bullet_pattern[0] == 'blank':
                                self.computer.set_bullet_pattern(0,'live')
                        elif self.player.item[item] == '過期藥物':
                            print('莊家偷走了過期藥物')
                            if random.randint(0,1):
                                self.computer.hp += 2
                                print('莊家回復了兩點血量')
                            else:
                                self.computer.hp -= 1
                                print('莊家失去了一點血量')
                                if self.computer.hp <= 0:
                                    time.sleep(2)
                                    print('**************************************')
                                    print('你贏了')
                                    time.sleep(2)
                                    return
                        elif self.player.item[item] == '放大鏡':
                            print('莊家偷走了放大鏡')
                            self.computer.set_bullet_pattern(0,'live' if remain_bullet[0] else 'blank')
                        elif self.player.item[item] == '香菸':
                            print('莊家偷走了香菸,回復一點血量')
                            self.computer.hp += 1
                        elif self.player.item[item] == '手銬':
                            print('莊家偷走了手銬,你下回合無法行動')
                            self.player.dohandcuff()
                        elif self.player.item[item] == '漆黑皇后':
                            #效果和玩家使用漆黑皇后相同
                            print('莊家偷走了漆黑皇后，彈藥裝填為一發空包彈一發5點傷害實彈，祈禱吧!')
                            self.computer.item = []
                            self.player.item = []
                            remain_bullet = [True,False]
                            live_bullet = 1
                            blank = 1
                            self.computer.reset_bullet_pattern(live_bullet+blank)
                            random.shuffle(remain_bullet)
                            killer_queen = True
                            not_blue_print = False
                        elif self.player.item[item] == '神聖皇后':
                            #效果和玩家使用神聖皇后相同
                            print('莊家偷走了神聖皇后，回復3點血量，背包上限+2，獲得3個隨機物品')
                            self.computer.hp += 3
                            self.computer.max_item += 2
                            self.give_participant_item(3,self.computer)
                        elif self.player.item[item] == '蔚藍皇后':
                            #效果和玩家使用蔚藍皇后相同
                            print('莊家偷走了蔚藍皇后，你獲得回合時莊家將獲得隨機物品')
                            self.computer.item_queen += 1
                            
                        elif self.player.item[item] == '未知藍圖':
                            temp = random.randint(1,5)
                            if temp == 1:
                                print('莊家獲得了禁藥')
                                self.computer.item.append('禁藥')
                            elif temp == 2:
                                print('莊家獲得了大口徑子彈')
                                self.computer.item.append('大口徑子彈')
                            elif temp == 3:
                                print('莊家獲得了榴彈砲')
                                self.computer.item.append('榴彈砲')
                            elif temp == 4:
                                print('莊家獲得了彈藥包')
                                self.computer.item.append('彈藥包')
                            elif temp == 5:
                                print('莊家獲得了擴增背包')
                                self.computer.max_item += 1
                        elif self.player.item[item] == '禁藥':
                            print('莊家偷走了禁藥')
                            if random.randint(1,10) <= 7:
                                self.computer.hp *= 2
                                self.computer.hp += 3
                                print('莊家的血量大幅提升,現在血量為',self.computer.hp)
                            else:
                                if self.computer.hp == 1:
                                    print('莊家中毒身亡，你贏了')
                                    time.sleep(2)
                                    return
                                self.computer.hp = 1
                                print('莊家中毒了，血量降為1')
                        elif self.player.item[item] == '大口徑子彈':
                            if handsaw:
                                self.player.hp -= 6
                                print('莊家偷走了大口徑子彈,造成6點傷害')
                            else:
                                self.player.hp -= 3
                                print('莊家偷走了大口徑子彈,造成3點傷害')
                            if remain_bullet.pop(0):
                                live_bullet -= 1
                            else:
                                blank -= 1
                            handsaw = False
                            self.computer.pop_bullet_pattern()
                            break
                        elif self.player.item[item] == '榴彈砲':
                            damage = self.computer.hp 
                            self.computer.hp = 1
                            if remain_bullet.pop(0):
                                if handsaw:
                                    self.player.hp -= 2*damage
                                    print('莊家偷走了榴彈砲,造成',2*damage,'點傷害')
                                    handsaw = False
                                else:
                                    self.player.hp -= damage
                                    print('莊家偷走了榴彈砲,造成',damage,'點傷害')
                                live_bullet -= 1
                            else:
                                print('莊家偷走了榴彈砲,但是子彈打空了')
                                blank -= 1
                            self.player.pop_bullet_pattern()
                            break
                        elif self.player.item[item] == '彈藥包':
                            damage = live_bullet
                            self.player.hp -= damage
                            print('莊家偷走了彈藥包,對你造成',damage,'點傷害')
                            remain_bullet = []
                            live_bullet = 0
                            blank = 0
                            for i in range(8-len(remain_bullet)):
                                if random.randint(0,1):
                                    remain_bullet.append(True)
                                    live_bullet += 1
                                else:
                                    remain_bullet.append(False)
                                    blank += 1
                            random.shuffle(remain_bullet)
                            print('彈藥已重新裝填')
                            self.player.reset_bullet_pattern(live_bullet+blank)
                        elif self.player.item[item] == '腎上腺素':
                            print('莊家試著偷取腎上腺素但失敗了')
                        self.player.item.pop(item)
                    if skip:
                        break
                    if not_blue_print:
                        self.computer.item.pop(item)
                    continue
                if self.player.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你死了')
                    time.sleep(2)
                    return
                if self.computer.hp <= 0:
                    time.sleep(2)
                    print('**************************************')
                    print('你贏了')
                    time.sleep(2)
                    return
                if self.player.handcuff:
                    print('你被手銬銬住了,無法行動')
                    self.player.unhandcuff()
                    try_count = 0
                    continue
                if len(remain_bullet) == 0:
                    print('子彈打完了')
                    print('進入下一局')
                    return
                if self.computer.item_queen > 0:
                    print('蔚藍皇后使莊家獲得隨機物品')
                    time.sleep(1)
                for i in range(self.computer.item_queen):
                    self.give_participant_item(1,self.computer)
                break
            
            

#來玩一場吧
#先讓玩家設定一些初始值
money = 0
risk = 0
action = input('歡迎來到俄羅斯輪盤遊戲,輸入1進入設定,或按下Enter開始遊戲')
if action == '1':
    money = int(input('請設定你的初始金錢:'))
    print('高風險模式下，特殊道具可以直接出現，玩家獲得皇后和莊家獲得藍圖的機率翻倍')
    print('每回合有50%機率雙方血量大幅提升，獲勝時獎金1.3倍')
    risk = int(input('是否開啟高風險模式? : 1.是 2.否'))
round = 0
player1 = player(5,[],money)
computer1 = computer(5,[])
hp=random.randint(2,6)
games={}
games[round] = game(player1,computer1,hp,risk)
while True:
    live_bullet = random.randint(1,4)
    blank = random.randint(1,4)
    item_number = random.randint(2,5)
    games[round].one_round(live_bullet,blank,item_number)
    games[round].round += 1
    if player1.hp <= 0:
        print('你的屍體旁躺著未能帶走的',player1.money,'元')
        break
    elif computer1.hp <= 0:
        if player1.money == 0:
            player1.money = random.randint(14000,52459)
            print('你獲得了',player1.money,'元')
            time.sleep(2)
            print('加倍或放棄?')
            print('1.加倍 2.放棄')
            action = int(input())
            if action == 1:
                round += 1
                print('你帶著',player1.money,'元繼續遊戲')
                computer1 = computer(5,[])
                hp=random.randint(2,6)
                games[round] = game(player1,computer1,hp,risk)
                continue
            else:
                print('你帶著',player1.money,'元離開了賭場')
                break
        else:
            player1.money *= 2
            print('你獲得了',player1.money,'元')
            time.sleep(2)
            print('加倍或放棄?')
            print('1.加倍 2.放棄')
            action = int(input())
            if action == 1:
                round += 1
                print('你帶著',player1.money,'元繼續遊戲')
                computer1 = computer(5,[])
                hp=random.randint(2,6)
                games[round] = game(player1,computer1,hp,risk)
                for i in range(int(round/3)):
                    games[round].computer_bonus(i)
                continue
            else:
                for queen in ['蔚藍皇后','神聖皇后','漆黑皇后','腥紅皇后']:
                    pass
                print('你使用了',player1.item.count('漆黑皇后'),'個漆黑皇后，每個獎金倍率為1.7')
                time.sleep(0.5)
                print('你使用了',player1.item.count('腥紅皇后'),'個腥紅皇后，每個獎金倍率為1.2')
                time.sleep(0.5)
                print('你使用了',player1.item.count('蔚藍皇后'),'個蔚藍皇后，每個獎金倍率為1.2')
                time.sleep(0.5)
                print('你使用了',player1.item.count('神聖皇后'),'個神聖皇后，每個獎金倍率為1.1')
                time.sleep(0.5)
                print('原始獎金為',player1.money,'元')
                n = pow(1.7,player1.item.count('漆黑皇后'))*pow(1.2,player1.item.count('腥紅皇后'))*pow(1.2,player1.item.count('蔚藍皇后'))*pow(1.1,player1.item.count('神聖皇后'))
                time.sleep(0.5)
                print('你的獎金倍率為',n)
                if risk == 1:
                    n *= 1.3
                    print('高風險模式下，獎金再x1.3倍') 
                time.sleep(0.5)
                print('最終獎金為',int(player1.money*n),'元')
                time.sleep(0.5)
                print('你帶著',int(player1.money*n),'元離開了賭場')
        break


        
