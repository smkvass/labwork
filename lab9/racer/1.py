import pygame
import sys
import random
import time

pygame.init()
pygame.mixer.init()

SIZE = WIDTH, HEIGHT = 400, 600
FPS = 60

FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE_COIN = 0
N = 5  # Increase speed every N coins
SPEED_INCREMENT = 0.1  # Speed increment value
SPEED_INCREMENT_DELAY = 1000  # Delay for speed increment (in milliseconds)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet1.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_coin_image = pygame.image.load("coin.png")
        scaled_width = original_coin_image.get_width() // 4  # Reduce width by half
        scaled_height = original_coin_image.get_height() // 4
        self.image = pygame.transform.scale(original_coin_image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect()
        self.reset_position()
        self.weight = random.randint(1, 5)  # Assign a random weight to the coin

    def reset_position(self):
        self.rect.center = (random.randint(30, WIDTH - 30), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.reset_position()


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, SPEED_INCREMENT_DELAY)

NEW_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(NEW_COIN, 1000)  # Every 1 second

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += SPEED_INCREMENT
            if SCORE % N == 0:
                SPEED += 1
        if event.type == NEW_COIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    collisions = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collisions:
        SCORE += 1

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash1.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)