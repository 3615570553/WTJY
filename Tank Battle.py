from typing import Any
import pygame
import os

FPS = 60
WIDTH = 1000
HEIGHT = 600
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("坦克大战")
clock = pygame.time.Clock()
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        tank_img = pygame.image.load(os.path.join("img/myTank","tank_T1_0.png")).convert()
        self.tank = tank_img
        self.tank.set_colorkey(WHITE)
        self.image = self.tank.subsurface((0,0),(48,48))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speed = 8
        self.direction = 'UP'

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.tank.subsurface((0,144),(48,42))
            self.direction = 'RIGHT'
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.tank.subsurface((0,96),(48,42))
            self.direction = 'LEFT'
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
            self.image = self.tank.subsurface((0,0),(48,48))
            self.direction = 'UP'
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.image = self.tank.subsurface((0,48),(48,48))
            self.direction = 'DOWN'
        if(self.rect.right > WIDTH):
            self.rect.right = WIDTH
        if(self.rect.left < 0 ):
            self.rect.left = 0
        if(self.rect.top < 0 ):
            self.rect.top = 0
        if(self.rect.bottom > HEIGHT):
            self.rect.bottom = HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.centery,self.direction)
        all_sprites.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction) -> None:
        super().__init__()
        self.bullets = ['./img/bullet/bullet_up.png','./img/bullet/bullet_down.png','./img/bullet/bullet_left.png','./img/bullet/bullet_right.png']
        self.direction = direction
        if self.direction == 'UP':
            self.bullet = pygame.image.load(self.bullets[0])
        if self.direction == 'DOWN':
            self.bullet = pygame.image.load(self.bullets[1])
        if self.direction == 'LEFT':
            self.bullet = pygame.image.load(self.bullets[2])
        if self.direction == 'RIGHT':
            self.bullet = pygame.image.load(self.bullets[3])
        self.image = self.bullet
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    
    def update(self):
        if self.direction == 'UP':
            self.rect.y -= self.speed
        if self.direction == 'DOWN':
            self.rect.y += self.speed
        if self.direction == 'LEFT':
            self.rect.x -= self.speed
        if self.direction == 'RIGHT':
            self.rect.x += self.speed
        if self.rect.top < 0:
            self.kill()
        if self.rect.bottom > HEIGHT:
            self.kill()
        if self.rect.left < 0:
            self.kill()
        if self.rect.right > WIDTH:
            self.kill()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_SPACE):
                player.shoot()
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()