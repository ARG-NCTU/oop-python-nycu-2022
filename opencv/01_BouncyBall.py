import pygame
from random import choice

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Ball():
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.x_direction = choice((-2, 2))
        self.y_direction = choice((-2, 2))
        self.radius = 40

    def move(self):
        self.x += self.x_direction
        self.y += self.y_direction
        self.contact_detect()

    def contact_detect(self):
        if self.x + self.radius >= SCREEN_WIDTH or\
                self.x - self.radius <= 0:
            self.x_direction = -self.x_direction

        if self.y + self.radius >= SCREEN_HEIGHT or\
                self.y - self.radius <= 0:
            self.y_direction = -self.y_direction

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('BouncyBall')
ball = Ball()
ball_2 = Ball()

# game loop
is_running = True
while is_running:
    screen.fill(WHITE)
    ball.move()
    ball.draw(screen)
    ball_2.move()
    ball_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()
    pygame.image.save(screen, "screen.png")
    clock.tick(30)
pygame.quit()
