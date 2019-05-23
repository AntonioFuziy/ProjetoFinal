import pygame
from os import path
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        
        personagem = pygame.image.load(path.join(img_dir,personagem_frente)).convert_alpha()
        
        self.image = personagem
        self.image = pygame.transform.scale(personagem,(80,100))
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 120
        
        self.speedx = 0
        self.speedy = 0
        
        self.radius =  int(self.rect.width * .85 / 2)
        self.health = 3

    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

    def update(self):
        self.rect.x += self.speedx
        #self.jump()
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.top < 0:
            self.rect.top = 0
        
        self.speedy += GRAVIDADE
        
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = STILL


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        BACKGROUND = pygame.image.load(path.join(img_dir,"Cenario.png")).convert()
        self.image = BACKGROUND
        self.image = pygame.transform.scale(BACKGROUND,(1200,HEIGHT))
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
        self.speedx = 0
        
    def update(self):
        self.rect.x += self.speedx
                
class Mob(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        mob_image = pygame.image.load(path.join(img_dir,MONSTRO)).convert_alpha()
        
        self.image = pygame.transform.scale(mob_image,(70,60))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 990
        self.rect.y = HEIGHT - 120
        
        self.speedx = 3
        self.speedy = 0

        self.health = 100
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy        
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = -self.speedx
        if self.rect.bottom > HEIGHT - 120:
            self.rect.bottom = HEIGHT - 120

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y, speedx):
        pygame.sprite.Sprite.__init__(self)
        
        bullet_image = pygame.image.load(path.join(img_dir,bala_frente)).convert_alpha()
        
        self.image = bullet_image
        self.image = pygame.transform.scale(bullet_image,(50,40))
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

        self.speedx = speedx
        
    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()        
        
class Blocks(pygame.sprite.Sprite):
    def __init__(self,block_image,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        block_image = pygame.image.load(path.join(img_dir,block)).convert_alpha()
        self.image = block_image
        
        self.image = pygame.transform.scale(block_image(30,30))
        
        self.image.set_colorkey(BLACK)

        self.rect = self.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.speedx = 0
        
    def update(self):
        self.rect.x += self.speed