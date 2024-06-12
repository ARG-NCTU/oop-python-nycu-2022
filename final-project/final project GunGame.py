
import pygame
import sys
import math
import time
import random
# 初始化 Pygame
pygame.init()


# 設定視窗大小
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)


# 設定顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FONT = 50


# 重力加速度
GRAVITY = 0.6


# 設定玩家初始位置和速度
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 10
PLAYER_ACCERATION = 0.5
JUMP_HEIGHT = 13  # 跳躍高度適中
RELIVE_X  = [250, 970]
RELIVE_Y = 0
# 地板位置列表
GROUND_LEVELS = [310, 410, 525, 615]  # 示例地板高度，可以根据实际情况修改

def distance_2D(x1, y1, x2, y2):
    return math.pow(math.pow(abs(x2-x1), 2) + math.pow(abs(y1-y2), 2), 0.5)



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def draw_init():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(BLACK)
    pygame.display.set_caption("GunGame")
    state = 0  # 0: show title, 1: show instructions, 2: start game
    while state < 2:
        if state == 0:
            screen.fill(BLACK)
            draw_text(screen, "GunGame", 64, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
            draw_text(screen, "Press any key to continue", 22, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        elif state == 1:
            screen.fill(BLACK)
            draw_text(screen, "Instructions", 64, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
            draw_text(screen, "WASD to move Player 1, Arrow keys to move Player 2", 22, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            draw_text(screen, "Space to shoot Player 1, Enter to shoot Player 2", 22, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 40)
            draw_text(screen, "B to drop bomb Player 1, L to drop bomb Player 2", 22, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 80)
            draw_text(screen, "Press any key to start the game", 22, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 120)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                state += 1
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 建立遊戲場景類別
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("GunGame")
        self.clock = pygame.time.Clock()
        self.background_img = pygame.image.load('./oop-python-nycu/final-project/background.jpg') # 載入背景圖片
        self.initial_img = pygame.image.load('./oop-python-nycu/final-project/initial.png') # 載入初始畫面
        self.tap_img = pygame.image.load('./oop-python-nycu/final-project/tap_any_bottom.png') # 載入提示
        self.player1_img = pygame.image.load('./oop-python-nycu/final-project/player_1.png') # 載入玩家圖片
        self.player2_img = pygame.image.load('./oop-python-nycu/final-project/player_2.png') # 載入玩家圖片
        self.bomb_img = pygame.image.load('./oop-python-nycu/final-project/bomb.png') # 載入炸彈圖片
        self.bomb_effect_img = pygame.image.load('./oop-python-nycu/final-project/bomb_effect.png') # 載入爆炸特效
        self.smallgun1_img = pygame.image.load('./oop-python-nycu/final-project/smallgun1.png') # 載入小槍圖片
        self.smallgun2_img = pygame.image.load('./oop-python-nycu/final-project/smallgun2.png')
        self.shotgun1_img = pygame.image.load('./oop-python-nycu/final-project/shotgun1.png')
        self.shotgun2_img = pygame.image.load('./oop-python-nycu/final-project/shotgun2.png')
        self.sniper1_img = pygame.image.load('./oop-python-nycu/final-project/sniper1.png')
        self.sniper2_img = pygame.image.load('./oop-python-nycu/final-project/sniper2.png')
        self.box_img = pygame.image.load('./oop-python-nycu/final-project/box.png')
        self.player1 = Player(RELIVE_X[0] , RELIVE_Y, self.player1_img)
        self.player2 = Player(RELIVE_X[1] , RELIVE_Y, self.player2_img)
        self.player2.turn_img("left")
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.bomb_effects = pygame.sprite.Group()
        self.all_sprites.add(self.player1, self.player2)
        self.font = pygame.font.Font(None, FONT)
        self.treasure_boxes = pygame.sprite.Group() 

    def spawn_treasure_box(self):
        treasure_box = TreasureBox(random.randint(90, 1160),-100, ["smallgun", "shotgun", "sniper"], self.box_img)
        self.all_sprites.add(treasure_box)
        self.treasure_boxes.add(treasure_box)    

    def run(self):
        running = True
        self.player1_press_jump = 0
        self.player2_press_jump = 0
        self.box_check = 0
        self.box_time = 300
        show_start_screen = True       # 顯示開始畫面-----------------------------------------
        while running:
            if show_start_screen:
                draw_init()
                show_start_screen = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.box_check == 0:# 生成寶箱
                self.box_time -= 1
                if self.box_time == 0:
                    self.box_time = 300
                    self.spawn_treasure_box()
                    self.box_check = 1

            mkeys = pygame.key.get_pressed()
            if mkeys[pygame.QUIT]:
                running = False
            if mkeys[pygame.K_w]:
                self.player1.jump(self.player1_press_jump)
                self.player1_press_jump = 1
            else :
                self.player1_press_jump = 0
            if mkeys[pygame.K_UP]:
                self.player2.jump(self.player2_press_jump)
                self.player2_press_jump = 1
            else :
                self.player2_press_jump = 0
            if mkeys[pygame.K_s]:
                self.player1.move_down()
            if mkeys[pygame.K_DOWN]:
                self.player2.move_down()
            if mkeys[pygame.K_a]:
                self.player1.move_x("left")
            if mkeys[pygame.K_d]:
                self.player1.move_x("right")
            if mkeys[pygame.K_LEFT]:
                self.player2.move_x("left")
            if mkeys[pygame.K_RIGHT]:
                self.player2.move_x("right")
            if mkeys[pygame.K_v]:
                if fire1_press_check == 0:
                    self.fire_bullet(self.player1, self.player1.get_direction(), RED, self.player1.now_gun())
                fire1_press_check = 1
            else :
                fire1_press_check = 0
            if mkeys[pygame.K_k]:
                if fire2_press_check == 0:
                    self.fire_bullet(self.player2, self.player2.get_direction(), YELLOW, self.player2.now_gun())
                fire2_press_check = 1
            else :
                fire2_press_check = 0
            if mkeys[pygame.K_b]:
                if bomb_press_check1 == 0 and self.player1.minus_bomb_num():
                    self.drop_bomb(self.player1, self.bomb_img)
                bomb_press_check1 = 1
            else :
                bomb_press_check1 = 0
            if mkeys[pygame.K_l]:
                if bomb_press_check2 == 0 and self.player2.minus_bomb_num():
                    self.drop_bomb(self.player2, self.bomb_img)
                bomb_press_check2 = 1
            else :
                bomb_press_check2 = 0

            self.all_sprites.update()
            self.bullets.update()
            self.bombs.update()
            
            # 碰撞檢測
            for bullet in self.bullets:
                if bullet.leave_check():
                    if bullet.rect.colliderect(self.player1.rect):
                        self.player1 .speed_x +=  3 * bullet.speed
                        bullet.kill()
                    if bullet.rect.colliderect(self.player2.rect):
                        self.player2.speed_x += 3 * bullet.speed
                        bullet.kill()
                if not pygame.sprite.spritecollideany(bullet, self.all_sprites):
                    bullet.turn_check()
                if bullet.out() or bullet.update():
                    bullet.kill()

            for bomb in self.bombs:
                if bomb.countdown():
                    bomb_effect = Bomb_effect(bomb.rect.centerx, bomb.rect.bottom, self.bomb_effect_img)
                    self.bomb_effects.add(bomb_effect)
                    bomb.explosion(self.player1)
                    bomb.explosion(self.player2)
                    bomb.kill()
            
            for bomb_effect in self.bomb_effects:
                if bomb_effect.Countdown():
                    bomb_effect.kill()

            for treasure_box in self.treasure_boxes:
                if pygame.sprite.collide_rect(self.player1, treasure_box):
                    gun = treasure_box.open_box()
                    self.player1.change_gun(gun)
                    treasure_box.kill()
                    self.box_check = 0
                if pygame.sprite.collide_rect(self.player2, treasure_box):
                    gun = treasure_box.open_box()
                    self.player2.change_gun(gun)
                    treasure_box.kill()
                    self.box_check = 0
                if treasure_box.rect.top > WINDOW_HEIGHT:
                    treasure_box.kill()
                    self.box_check = 0

            text = self.font.render(str(self.player1.now_gun()), True, (255, 255, 255)) #輸出左上角的字（用來測試）
            self.screen.blit(self.background_img, (0, 0))  # 绘制背景图像
            self.bomb_effects.draw(self.screen)
            self.all_sprites.draw(self.screen)
            self.bullets.draw(self.screen)
            self.bombs.draw(self.screen)
            self.screen.blit(text,(10,10))
            pygame.display.flip()

            self.clock.tick(60)

            #玩家重生
            if self.player1.rect.top > WINDOW_HEIGHT:
                self.player1.relive(0)
            if self.player2.rect.top > WINDOW_HEIGHT:
                self.player2.relive(1)

    # 發射子彈
    def fire_bullet(self, player, direction, color, gun):
        if player.get_value("gunlag") <= 0:
            bullet = Bullet(color, player.rect.centerx, player.rect.centery, direction, gun)
            self.bullets.add(bullet)
            player.change_gunlag(gun)

    def drop_bomb(self, player, img):
        bomb = Bomb(player.rect.centerx, player.rect.centery - 65, img, player.get_direction())
        self.bombs.add(bomb)

class Physics(object):
        def __init__(self, x, y, img):
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed_x = 0
            self.speed_y = 0
            self.on_ground = False
        
        def update(self):
            # 應用重力
            self.speed_y += GRAVITY

            # 移動
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            # 檢查是否在地板上
            self.check_ground()

            #讓角色滑行
            self.speed_x = self.speed_x * 0.93

            # 限制在窗口內
            # if self.rect.left < 0:
            #     self.rect.left = 0
            # elif self.rect.right > WINDOW_WIDTH:
            #     self.rect.right = WINDOW_WIDTH

        def check_ground(self):
            # 找到距離玩家最近的地板
            min_distance = float('inf')
            closest_ground = None
            for ground_level in GROUND_LEVELS:
                if ground_level == GROUND_LEVELS[0] and not ((self.rect.x > 310 and self.rect.x < 570) or (self.rect.x > 680 and self.rect.x < 940)):
                    continue
                if ground_level == GROUND_LEVELS[1] and not (self.rect.x > 185 and self.rect.x < 1070):
                    continue
                if ground_level == GROUND_LEVELS[2] and not ((self.rect.x > 90 and self.rect.x < 360) or (self.rect.x > 890 and self.rect.x < 1160)):
                    continue
                if ground_level == GROUND_LEVELS[3] and not (self.rect.x > 325 and self.rect.x < 940):
                    continue
                distance = abs(self.rect.bottom - ground_level)
                if distance < min_distance:
                    min_distance = distance
                    closest_ground = ground_level
            if min_distance >= 10:
                self.on_ground = False
            if self.on_ground == True:
                if self.speed_y > 0:
                    self.speed_y = 0
                self.rect.bottom = closest_ground
            elif self.speed_y >= 0 and min_distance < self.speed_y:
                self.on_ground = True
                self.speed_y = 0
                self.rect.bottom = closest_ground

    # 建立玩家類別
class Player(pygame.sprite.Sprite, Physics):
    def __init__(self, x, y, img):
        super().__init__()
        Physics.__init__(self, x, y, img)
        self.right_img = img
        self.left_img = pygame.transform.flip(img, True, False)
        self.on_ground = True
        self.ground_level = None  #玩家所在的地板高度
        self.bomb_num = 3
        self.double_jump = 1
        self.gunlag = 0
        self.gun = "smallgun"
                
    def change_gunlag(self, num):
        if num == "smallgun":
            self.gunlag = 5
        elif num == "shotgun":
            self.gunlag = 30
        elif num == "sniper":
            self.gunlag = 60

    def get_value(self, sub): # 拿來取要的值
        if sub == "x":
            return self.rect.x
        if sub == "y":
            return self.rect.y
        if sub == "bottom":
            return self.rect.bottom
        if sub == "gunlag":
            return self.gunlag
    
    def on_ground(self): # 回傳on_ground值
        return self.on_ground

    def turn_img(self, direction):
        if direction == "left":
            self.image = self.left_img
        elif direction == "right":
            self.image = self.right_img

    def get_direction(self):
        if self.image == self.left_img:
            return -1
        else:
            return 1
    
    def update(self): # 繼承update
        Physics.update(self)
        self.gunlag -= 1

    def check_ground(self): # 繼承check_ground
        super().check_ground()

    def move_x(self, direction):
        if direction == "left":
            if self.speed_x >= -PLAYER_SPEED:
                self.speed_x -= PLAYER_ACCERATION
            self.turn_img("left")
        elif direction == "right":
            if self.speed_x <= PLAYER_SPEED:
                self.speed_x += PLAYER_ACCERATION
            self.turn_img("right")

    def jump(self, check):
        if self.on_ground:  # 只有在地面上才能跳
            self.speed_y = -JUMP_HEIGHT
            self.double_jump = 1
            self.on_ground = False
        elif self.double_jump == 1 and check == 0: # 二段跳
            self.speed_y = -10
            self.double_jump = 0

    def move_down(self):
        # 玩家要在地板上才能往下移動
        if self.on_ground:
            if not((self.rect.bottom == GROUND_LEVELS[2] and ((self.rect.x > 90 and self.rect.x < 360) or (self.rect.x > 890 and self.rect.x < 1160))) or (self.rect.bottom == GROUND_LEVELS[3] and (self.rect.x > 325 and self.rect.x < 940))):
                self.rect.y += 15
                self.check_ground()

    def minus_bomb_num(self):
        self.bomb_num -= 1
        if self.bomb_num < 0:
            return False
        else:
            return True

    def relive(self, num):
        #玩家復活
        self.rect.x = RELIVE_X[num]
        self.rect.y = RELIVE_Y
        self.on_ground = True
        self.speed_x = 0
        self.speed_y = 0
        self.bomb_num = 3

    def change_gun(self, gun):
        self.gun = gun

    def now_gun(self):
        return self.gun
        

# 建立槍類別
class Gun():
    def __init__(self, speed, recoil, numofbullet, lagtime):
        self.speed = speed
        self.recoil = recoil
        self.numofbullet = numofbullet
        self.lagtime = lagtime

# 建立子彈類別
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, x, y, direction, which_gun):
        super().__init__()
        self.image = pygame.Surface([15, 5])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.leave = False
        self.out_check = False
        if which_gun == "smallgun":
            gun = Gun(5, 1, 100000, 5)
        if which_gun == "shotgun":
            gun = Gun(15, 2, 12, 30)
        if which_gun == "sniper":
            gun = Gun(15, 4, 8, 60)
        self.speed = gun.speed * direction
        self.gun = gun
        self.creation_time = time.time()
    def turn_check(self):
        self.leave = True

    def fire(self):
        self.lag = self.gun.lagtime

    def leave_check(self):
        return self.leave

    def update(self):
        elapsed_time = time.time() - self.creation_time
        acceleration = 0.005
        if self.speed == 0:
            return True
        elif self.speed > 0:
            self.speed -= acceleration*elapsed_time
        elif self.speed < 0:
            self.speed += acceleration*elapsed_time
            
        self.rect.x += self.speed
        if self.rect.left > WINDOW_WIDTH + 100 or self.rect.right < -100:
            self.out_check = True
        return False

    def out(self):
        return self.out_check

# 建立炸彈類別
class Bomb(pygame.sprite.Sprite, Physics):
    def __init__(self, x, y, img, direction):
        super().__init__()
        Physics.__init__(self, x, y, img)
        self.rect.centerx = x
        self.speed_x = 10 * direction
        self.dir = direction
        self.time_countdown = 120
        self.fixed = 0

    def update(self): # 繼承update
        Physics.update(self)
        self.time_countdown -= 1
        
        if self.on_ground == True:
            if self.fixed == 0:
                self.fixed_x = self.rect.x
                self.fixed_y = self.rect.y
                self.fixed = 1
            self.speed_x = 0
            if self.time_countdown % 30 < 5:
                self.image = pygame.transform.scale(self.image, (60, 60))
                self.rect.x = self.fixed_x - 7.5
                self.rect.y = self.fixed_y - 7.5
            else:
                self.image = pygame.transform.scale(self.image, (45, 45))
                self.rect.x = self.fixed_x
                self.rect.y = self.fixed_y
        
        
    def countdown(self): # 炸彈倒數計時
        if self.time_countdown == 0:
            return True

    def check_ground(self): # 繼承check_ground
        super().check_ground()

    def force(self, x1, y1, player, F):
        player.speed_x += F * (player.rect.centerx - x1) / self.D
        if (player.rect.centery - y1) < 0:
            if F * (player.rect.centery - y1) / self.D <- 30:
                player.speed_y += -30
            else:
                player.speed_y += F * (player.rect.centery - y1) / self.D

    def explosion(self, player): # 爆炸
        self.D = distance_2D(self.rect.centerx, self.rect.centery, player.rect.centerx, player.rect.centery)
        if self.D < 60:
            self.force(self.rect.centerx, self.rect.centery, player, 80)
        elif self.D < 200:
            self.force(self.rect.centerx, self.rect.centery, player, 288000/math.pow(self.D, 2))

class Bomb_effect(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = x - 135
        self.rect.y = y - 190
        self.countdown = 25

    def Countdown(self):
        self.countdown -= 1
        if self.countdown == 0:
            return True
        else:
            return False

#寶箱掉落

class TreasureBox(pygame.sprite.Sprite, Physics):
    def __init__(self, x, y, guns, box_images):
        super().__init__()
        self.image = box_images
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.guns = guns  # 槍的圖片列表
        self.speed_x = 0  # 寶箱水平速度
        self.speed_y = 0 # 寶箱下落速度
    def get_random_gun(self):
        # 從槍的圖片列表中隨機選擇一個圖片
        return random.choice(self.guns)

    def open_box(self):
        # 隨機獲得一把槍
        return self.get_random_gun()
    
    def update(self):
        Physics.update(self)

# 執行遊戲
if __name__ == "__main__":
    game = Game()
    game.run()
