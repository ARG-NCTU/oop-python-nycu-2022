import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# 載入圖片
background = pygame.image.load("background.png")
player_image = pygame.image.load("player.png")
rock_image = pygame.image.load("rock.png")

# 設定字體
font = pygame.font.SysFont(None, 48)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()  # call sprite的初始函式
        self.image = player_image
        self.rect = self.image.get_rect()  # 屬性二: rect
        self.rect.centerx = 250
        self.rect.top = 550

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.x < 400:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.y < 530:
            self.rect.y += 5

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()  # call sprite的初始函式
        self.image = rock_image
        self.rect = self.image.get_rect()  # 屬性二: rect
        self.rect.centerx = random.randint(1, 500)
        self.rect.top = -10

    def update(self):
        self.rect.top += 5
        if self.rect.top > 600:  # 如果岩石移出畫面，就刪除
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((20, 50))  # 繪製簡單的矩形作為子彈
        self.image.fill((255, 0, 0))  # 設定子彈顏色為紅色
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        self.rect.top -= 10  # 子彈向上移動
        if self.rect.bottom < 0:  # 如果子彈移出畫面，就刪除
            self.kill()

# Sprite 群組
all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()  # 用於管理岩石
bullets = pygame.sprite.Group()  # 用於管理子彈

player = Player()
all_sprites.add(player)

# 顯示結束畫面
def show_game_over_screen():
    screen.fill((0, 0, 0))  # 設定背景為黑色
    text = font.render("Game Over", True, (255, 255, 255))  # 顯示 "Game Over"
    subtext = font.render("Press Any Key to Exit", True, (255, 255, 255))  # 提示訊息
    screen.blit(text, (125, 250))
    screen.blit(subtext, (50, 320))
    pygame.display.flip()  # 更新畫面

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # 玩家按下任意鍵後結束遊戲
                waiting = False

# 遊戲迴圈
nn = 0
running = True
while running:
    if nn == 30:  # 每隔一定時間產生岩石
        rock = Rock()
        all_sprites.add(rock)
        rocks.add(rock)
        nn = 0
    nn += 1

    clock.tick(60)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 按空白鍵射出子彈
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # 更新遊戲
    all_sprites.update()  # 執行所有的sprite中update函式

    # 檢查子彈與岩石的碰撞
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)  # 岩石與子彈消失

    # 檢查岩石與玩家的碰撞
    if pygame.sprite.spritecollide(player, rocks, False):  # 如果有碰撞發生
        show_game_over_screen()  # 顯示結束畫面
        running = False  # 結束遊戲迴圈
        pygame.quit()

    # 畫面顯示
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)  # 畫出所有的sprite
    pygame.display.flip()

pygame.quit()
