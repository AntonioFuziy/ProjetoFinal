import pygame
from os import path
import random
from time import sleep

img_dir = path.join(path.dirname(__file__),'img')

WIDTH = 800
HEIGHT = 600 

FPS = 60

WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)

ordem = random.randint(1,2)

lista_galho = [(0, HEIGHT - 40, WIDTH, 40),
               (WIDTH / 2, HEIGHT - 130, 52, 10),
               (WIDTH -50, HEIGHT - 250, 52, 10),
               (150, HEIGHT - 310, 52, 10),
               (WIDTH / 4, HEIGHT - 430, 52, 10)]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path.join(img_dir,'PersonagemTeste.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - 100
        self.rect.y = HEIGHT - 50
        
        self.pos = 0
        
    def update(self):
        self.rect.x += self.pos
        
        if self.rect.x > WIDTH/2 + 50:
            self.rect.x = WIDTH/2 + 50
        if self.rect.x < WIDTH/2 - 100:
            self.rect.x = WIDTH/2 - 100

class Galho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path.join(img_dir,'Corsinha.jpg')).convert()
        
        self.image = pygame.transform.scale(self.image,(50,30))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = WIDTH/2 - 50
        self.rect.y = 0
        
        
    def update(self):
        self.novo_tronco = ordem
        if self.novo_tronco == 1:
            self.rect.x = WIDTH/2 + 50
            self.rect.y = self.rect.y 
            
        if self.novo_tronco == 2:
            self.rect.x = WIDTH/2 - 100
            self.rect.y = self.rect.y
        

class Tronco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path.join(img_dir,'Tronco.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,600))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - 50
        self.rect.y = HEIGHT
        
    #def update(self):
        

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Timberman!!!")

player = Player()
tronco = Tronco()

galhos = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(tronco)
all_sprites.add(player)

#tronco = Tronco()

for galho in lista_galho:        
    galho=Galho()
    all_sprites.add(galho)
    galhos.add(galho)

    
try:        
    running = True
            
    while running:
    
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.pos = 150
                    galho.rect.y += 50
                    ordem = random.randint(1,2)
                    
                    
                if event.key == pygame.K_LEFT:
                    player.pos = -200
                    galho.rect.y += 50
                    ordem = random.randint(1,2)
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.pos = 0
                    
                if event.key == pygame.K_RIGHT:
                    player.pos = 0
                    
                    
        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, galhos, False, pygame.sprite.collide_circle)                
    
        if hits:
            player.image = pygame.image.load(path.join(img_dir,'Moeda.png')).convert_alpha()
            player.image = pygame.transform.scale(player.image,(50,50))
            
            sleep(1)
            running = False
                    
        screen.fill(BLACK)
#        screen.blit(background.image, background.rect)
#        screen.blit(text, textRect)
        all_sprites.draw(screen)
        pygame.display.flip()
                    
finally:
    pygame.quit()
