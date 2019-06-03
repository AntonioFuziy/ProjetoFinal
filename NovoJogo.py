import pygame
from os import path
import random

img_dir = path.join(path.dirname(__file__),'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 800
HEIGHT = 600 

FPS = 60

WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)

VIDA = 100

GALHO_LISTA = [(450, HEIGHT - 140),
               (200, HEIGHT - 290),
               (200, HEIGHT - 440),
               (450, HEIGHT - 590),
               (450, HEIGHT - 740)]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path.join(img_dir,'Pulica1.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image,(120,120))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH/2 - 70
        self.rect.y = HEIGHT - 100
        
        self.pos = 0
        
    def update(self):
        self.rect.x += self.pos
        
        if self.rect.right < WIDTH/2 - 30:
            self.rect.right = WIDTH/2 - 30
        if self.rect.left > WIDTH/2 + 30:
            self.rect.left = WIDTH/2 + 30
        
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        background = pygame.image.load(path.join(img_dir,'Background.jpg')).convert()
        
        self.image = background
        self.image = pygame.transform.scale(background,(WIDTH,HEIGHT))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((100,20))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.y = 20

        self.regen = 0

    def update(self):
        #healthWidth += self.regen
        pass

class Galho(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(img_dir,'Galho.png')).convert_alpha()
        #self.image = pygame.transform.scale(self.image,(150,50))
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        pass

class Tronco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(img_dir,'Tronco2.png')).convert_alpha()
        #self.image = pygame.transform.scale(self.image,(100,600))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.y = 0

    def update(self):
        pass

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Timberman!!!")

background = pygame.image.load(path.join(img_dir, 'Background.jpg')).convert()
background = pygame.transform.scale(background,(800,600))
background_rect = background.get_rect()

#background.rect.x = 1920 
#background.rect.y = 1080

#pygame.mixer.music.load(path.join(snd_dir, ''))
#pygame.mixer.music.set_volume(0.4)
#boom_sound = pygame.mixer.Sound(path.join(snd_dir, ''))
#destroy_sound = pygame.mixer.Sound(path.join(snd_dir, ''))
#pew_sound = pygame.mixer.Sound(path.join(snd_dir, ''))

all_sprites = pygame.sprite.Group()
galho = pygame.sprite.Group()

tronco = Tronco()
health = HealthBar()
player = Player()
#background = Background()

#all_sprites.add(background)
all_sprites.add(tronco)
all_sprites.add(player)
all_sprites.add(health)

for branch in GALHO_LISTA:
    g = Galho(*branch)
    all_sprites.add(g)
    galho.add(g)

try:        
    running = True
            
    while running:
    
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.pos = 170
                    player.image = pygame.image.load(path.join(img_dir,'Pulica3_Invertido.png'))
                    player.image = pygame.transform.scale(player.image,(120,120)) 

                if event.key == pygame.K_LEFT:
                    player.pos = -220
                    player.image = pygame.image.load(path.join(img_dir,'Pulica3.png'))
                    player.image = pygame.transform.scale(player.image,(120,120))
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    for branch in galho:
                        branch.rect.y += 100
                        if branch.rect.top >= HEIGHT:
                            branch.kill()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.pos = 0
                    player.image = pygame.image.load(path.join(img_dir,'Pulica1.png'))
                    player.image = pygame.transform.scale(player.image,(120,120))
                    
                if event.key == pygame.K_RIGHT:
                    player.pos = 0
                    player.image = pygame.image.load(path.join(img_dir,'Pulica1_Invertido.png'))
                    player.image = pygame.transform.scale(player.image,(120,120))
                    
        if len(galho) < 4:
            lista_posicao = [200, 450]
            random.shuffle(lista_posicao)
            g = Galho(lista_posicao[0], 40)
            all_sprites.add(g)
            galho.add(g)

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, galho, False)
        if hits:
            running = False
                    
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        #screen.blit(text, textRect)
        all_sprites.draw(screen)
        pygame.display.flip()
                    
                
finally:
    pygame.quit()
