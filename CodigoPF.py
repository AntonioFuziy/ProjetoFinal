import pygame
from os import path
import random
import time

img_dir = path.join(path.dirname(__file__),'img')

WIDTH = 995
HEIGHT = 654
FPS = 45

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVIDADE = -0.4

VIDA = 3

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        personagem = pygame.image.load(path.join(img_dir,"PersonagemTeste.png")).convert_alpha()
        
        self.image = personagem
        
        self.image = pygame.transform.scale(personagem,(80,100))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 87
        
        self.speedx = 0
        self.speedy = 0
        
        self.radius =  int(self.rect.width * .85 / 2)
        
    def update(self):
        self.rect.x += self.speedx
        self.jump()
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT - 87:
            self.rect.bottom = HEIGHT - 87
            self.speedy = 0
    
    def jump(self):
        self.speedy -= GRAVIDADE
        self.rect.y += self.speedy

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        BACKGROUND = pygame.image.load(path.join(img_dir,"Imagem de fundo.jpg")).convert()
        self.image = BACKGROUND
        self.image = pygame.transform.scale(BACKGROUND,(WIDTH,HEIGHT))
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
        
        self.image = pygame.transform.scale(mob_image,(50,40))
        
        self.rect = self.image.get_rect()
       
        self.image.set_colorkey(BLACK)
        
        self.rect.x = 990
        self.rect.y = HEIGHT - 122
        
        self.speedx = 3
        self.speedy = 0
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        pulo = random.randint(1,5)
        
        if pulo == 1:
            self.jump()
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = -self.speedx
        if self.rect.bottom > HEIGHT - 88:
            self.rect.bottom = HEIGHT - 88
            
    def jump(self):
        self.speedy -= GRAVIDADE
        tempo_de_pulo=time.time()
        if tempo_de_pulo == 1.2:
            self.speedy += GRAVIDADE
        self.rect.y += self.speedy

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        
        bullet_image = pygame.image.load(path.join(img_dir,'Bala.png')).convert_alpha()
        self.image = bullet_image
        
        self.image = pygame.transform.scale(bullet_image,(50,40))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = 5
        
    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
    
        
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("MINEEEE!!!")

clock = pygame.time.Clock()

#background = pygame.image.load(path.join(img_dir,"Imagem de fundo.jpg"))
#background_rect = background.get_rect()

player = Player()
background = Background()

all_sprites = pygame.sprite.Group()
  
all_sprites.add(background) 
all_sprites.add(player) 
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
#background = pygame.sprite.Group()

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
                if event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                    player.speedx = 0
                    background.speedx += 7
                if event.key == pygame.K_d or event.key == pygame.K_LEFT:
                    player.speedx = 0
                    background.speedx -= 7
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.speedy -= 7
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.right, player.rect.centery)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.speedy += 7 
                if event.key == pygame.K_a or event.key == pygame.K_LEFT: 
                    player.speedx = 0
                    background.speedx += 7
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.speedx = 0    
                    background.speedx -= 7
                
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
        #pygame.display.update()
        
finally:
    pygame.quit()