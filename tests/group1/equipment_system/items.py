class item:
    def __init__(self, name, discription = "", unlocked_phase = 0):
        self.name = name
        self.discription = discription
        self.unlocked = False
        self.unlocked_phase = unlocked_phase

    def unlock(self, phase):
        if phase >= self.unlocked_phase:
            self.unlocked = True

class spell_card(item):
    def __init__(self, name, discription = "", unlocked_phase = 0):
        item.__init__(self, name, discription, unlocked_phase)

class weapon(item):
    def __init__(self, name, discription = "", unlocked_phase = 0, damage = 0):
        item.__init__(self, name, discription, unlocked_phase)
        self.damage = damage

class accessory(item):
    def __init__(self, name, discription = "", unlocked_phase = 0, cost = 0):
        item.__init__(self, name, discription, unlocked_phase)
        self.cost = cost

weapons = []
weapons.append(weapon("七耀魔法書", "消耗魔力進行遠程持續傷害", 1, 1))
weapons.append(weapon("貪欲的叉勺", "近戰攻擊能夠消彈", 3, 1))

spell_cards = []    
spell_cards.append(spell_card("彩符「彩光亂舞」", "全畫面散射攻擊，提供較長的無敵時間", 1))
spell_cards.append(spell_card("逆符「階級反轉」", "逆轉雙方彈幕，將所受傷害反擊給對方", 2))
spell_cards.append(spell_card("戀符「極限火花」", "集中火力的超高輸出攻擊", 2))

accessories = []
accessories.append(accessory("水晶吊墜", "魔力上限增加10點", 1, 1))
accessories.append(accessory("心型吊墜", "血量上限增加1點", 1, 1))
accessories.append(accessory("亡靈提燈", "增加受傷後無敵時間", 1, 1))
accessories.append(accessory("蝙蝠吊墜", "衝刺可以造成傷害", 2, 2))
accessories.append(accessory("銀製匕首", "提升近戰傷害", 2, 2))
accessories.append(accessory("斷線的人偶", "提升魔法傷害和符卡傷害", 2, 2))
accessories.append(accessory("神社的符咒", "符卡可用次數+1", 3, 3))
accessories.append(accessory("巫女的御幣", "近戰攻擊次數+1", 3, 3))

def get_weapons():
    return weapons

def get_spell_cards():
    return spell_cards

def get_accessories():
    return accessories
