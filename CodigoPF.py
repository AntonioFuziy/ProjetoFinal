import pygame
from os import path
import random
import time

img_dir = path.join(path.dirname(__file__),'img')

WIDTH = 995
HEIGHT = 654
FPS = 45

SENTIDO = 1

GROUND = HEIGHT - 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVIDADE = 2
JUMP_SIZE = 30

STILL = 0
JUMPING = 1
FALLING = 2

INITIAL_BLOCKS = 5

bala_frente = 'Bala.png'
bala_traz = 'BalaInvertida.png'
personagem_frente = 'PersonagemTeste.png'
personagem_traz = 'PersonagemTesteInvertido.png'
block = 'bloco.png' 

VIDA = 3

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
            
    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING        

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
        
        mob_image = pygame.image.load(path.join(img_dir,'Goomba.png')).convert_alpha()
        
        self.image = pygame.transform.scale(mob_image,(70,60))
        
        self.rect = self.image.get_rect()
       
        self.image.set_colorkey(BLACK)
        
        self.rect.x = 990
        self.rect.y = HEIGHT - 120
        
        self.speedx = 3
        self.speedy = 0
        
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
        self.rect.x += self.speedx
        
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("MINEEEE!!!")

clock = pygame.time.Clock()

player = Player()
background = Background()
#mobs = Mob()

all_sprites = pygame.sprite.Group()
all_sprites.add(background) 
all_sprites.add(player)
#all_sprites.add(mobs) 
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

#world_blocks = pygame.sprite.Group()

#for bloco in range(INITIAL_BLOCKS):
#    block_x

for i in range(2):
    m=Mob()
    all_sprites.add(m)
    mobs.add(m)

try:
    running = True
    while running:
        
        clock.tick(FPS)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    SENTIDO = 1
                    player.speedx += 5
                    background.speedx -= 7
                    personagem = pygame.image.load(path.join(img_dir, personagem_frente))
                    player.image = personagem
                    player.image = pygame.transform.scale(personagem,(80,100))

                if event.key == pygame.K_LEFT:
                    SENTIDO = 2
                    player.speedx -= 5
                    background.speedx += 7
                    personagem = pygame.image.load(path.join(img_dir, personagem_traz))
                    player.image = personagem
                    player.image = pygame.transform.scale(personagem,(80,100))
        
                if event.key == pygame.K_UP:
                    player.jump()
                
                if SENTIDO == 1:
                    if event.key == pygame.K_SPACE:
                        
                        bullet = Bullet(player.rect.right, player.rect.centery, 7)
                        bullet.bullet_image = pygame.image.load(path.join(img_dir, bala_frente)).convert_alpha()
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                       
                if SENTIDO == 2:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(player.rect.left, player.rect.centery, -7)
                        bullet.bullet_image = pygame.image.load(path.join(img_dir, bala_traz)).convert_alpha()
                        all_sprites.add(bullet)
                        bullets.add(bullet)
 
            if event.type == pygame.KEYUP:
                    
                if event.key == pygame.K_LEFT: 
                    player.speedx = 0
                    background.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                    background.speedx = 0
        all_sprites.update()
        
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:  
            m = Mob()      
            all_sprites.add(m)
            mobs.add(m)
            
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        if hits:
            time.sleep(1)
            running = False
        
        screen.fill(BLACK)
        screen.blit(background.image, background.rect)
        all_sprites.draw(screen)
        pygame.display.flip()

finally:
    pygame.quit()