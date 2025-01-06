import datetime
import os
import random
import threading
import pygame

### PyGame Setup ###
#Pygame
pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("I am a Joker")

### Load IMG ###
#Icon
Icon = pygame.image.load("assets/Wallpaper.png")
pygame.display.set_icon(Icon)

#Runing animation
RUNNING = [
    pygame.image.load(os.path.join("assets/Joker", "JokerRun1.png")),
    pygame.image.load(os.path.join("assets/Joker", "JokerRun2.png")),
]
#Jumping animation
JUMPING = pygame.image.load(os.path.join("assets/Joker", "JokerJump.png"))
#Ducking animation
DUCKING = [
    pygame.image.load(os.path.join("assets/Joker", "JokerDuck1.png")),
    pygame.image.load(os.path.join("assets/Joker", "JokerDuck2.png")),
]

#Ground Obstacles
SMALL_BOOK = [
    pygame.image.load(os.path.join("assets/Book", "SmallBook1.png")),
    pygame.image.load(os.path.join("assets/Book", "SmallBook2.png")),
    pygame.image.load(os.path.join("assets/Book", "SmallBook3.png")),
]
LARGE_BOOK = [
    pygame.image.load(os.path.join("assets/Book", "LargeBook1.png")),
    pygame.image.load(os.path.join("assets/Book", "LargeBook2.png")),
    pygame.image.load(os.path.join("assets/Book", "LargeBook3.png")),
]

#Sky Obstacles
GPA = [
    pygame.image.load(os.path.join("assets/GPA", "GPA1.png")),
    pygame.image.load(os.path.join("assets/GPA", "GPA2.png")),
]

#W for win
W = pygame.image.load(os.path.join("assets/Other", "W.png"))

#Backgound
BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))

FONT_COLOR=(128,128,128)


### Joker ###
class Joker:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5
    
    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.joker_duck = False
        self.joker_run = True
        self.joker_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.joker_rect = self.image.get_rect()
        self.joker_rect.x = self.X_POS
        self.joker_rect.y = self.Y_POS
    
    #State
    def update(self, userInput):
        if self.joker_duck:
            self.duck()
        if self.joker_run:
            self.run()
        if self.joker_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.joker_jump:
            self.joker_duck = False
            self.joker_run = False
            self.joker_jump = True
        elif userInput[pygame.K_DOWN] and not self.joker_jump:
            self.joker_duck = True
            self.joker_run = False
            self.joker_jump = False
        elif not (self.joker_jump or userInput[pygame.K_DOWN]):
            self.joker_duck = False
            self.joker_run = True
            self.joker_jump = False
          
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.joker_rect = self.image.get_rect()
        self.joker_rect.x = self.X_POS
        self.joker_rect.y = self.Y_POS
        self.step_index += 1
      
    def jump(self):
        self.image = self.jump_img
        if self.joker_jump:
            self.joker_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.joker_jump = False
            self.jump_vel = self.JUMP_VEL
      
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.joker_rect = self.image.get_rect()
        self.joker_rect.x = self.X_POS
        self.joker_rect.y = self.Y_POS_DUCK
        self.step_index += 1
            
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.joker_rect.x, self.joker_rect.y))
        
        
### Obstacles ###
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
            
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)
        
### W ###
class WforWin:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = W
        self.width = self.image.get_width()
        
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
            
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y)) 
        
### GPA ###
class Gpa(Obstacle):
    GPA_HEIGHTS = [200, 250, 320]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.GPA_HEIGHTS)
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

### LargeObs ###
class LargeBook(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300
        
### SmallObs ###
class SmallBook(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325
        
def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, highscore
    run = True
    clock = pygame.time.Clock()
    player = Joker()
    w = WforWin()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    death_count = 0
    pause = False

    def score():
        global points, game_speed, highscore
        points += 1
        if points % 100 == 0:
            game_speed += 1
        current_time = datetime.datetime.now().hour
        if points > highscore:
            highscore = points
        
        text = font.render("High Score: "+ str(highscore) + "  Points: " + str(points), True, FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (900, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    def unpause():
        nonlocal pause, run
        pause = False
        run = True
    
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Game Paused, Press 'u' to Unpause", True, FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT  // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    unpause()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                run = False
                paused()

        current_time = datetime.datetime.now().second
        round_current_time = current_time % 47
        if 23 < round_current_time < 46:
            SCREEN.fill((0, 0, 0))
        else:
            SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallBook(SMALL_BOOK))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeBook(LARGE_BOOK))
            elif random.randint(0, 2) == 2:
                obstacles.append(Gpa(GPA))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.joker_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        w.draw(SCREEN)
        w.update()

        score()

        clock.tick(30)
        pygame.display.update()
        
        
def menu(death_count):
    global points, highscore
    global FONT_COLOR
    run = True
    while run:
        FONT_COLOR=(0, 0, 0)
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            highscore = 0
            text = font.render("Press any Key to Start", True, FONT_COLOR)
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, FONT_COLOR)
            score = font.render("Your Score: " + str(points), True, FONT_COLOR)
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
            if points > highscore:
                highscore = points
                
            hs_score_text = font.render(
                "High Score : " + str(highscore), True, FONT_COLOR
            )
            hs_score_rect = hs_score_text.get_rect()
            hs_score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            SCREEN.blit(hs_score_text, hs_score_rect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main()


t1 = threading.Thread(target=menu(death_count=0), daemon=True)
t1.start()
