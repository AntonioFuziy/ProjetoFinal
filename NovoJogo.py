import pygame
from os import path
import random

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

GALHO_LISTA = [(450, HEIGHT - 140),
               (200, HEIGHT - 290),
               (200, HEIGHT - 440),
               (450, HEIGHT - 590),
               (450, HEIGHT - 740)]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path.join(img_dir,'PersonagemTeste.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH/2 - 50
        self.rect.y = HEIGHT - 100
        
        self.pos = 0
        
    def update(self):
        self.rect.x += self.pos
        
        if self.rect.right < WIDTH/2 - 50:
            self.rect.right = WIDTH/2 - 50
        if self.rect.left > WIDTH/2 + 50:
            self.rect.left = WIDTH/2 + 50

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y    

class Galho(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(img_dir,'Goomba.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image,(150,50))
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        pass

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Timberman!!!")

all_sprites = pygame.sprite.Group()
galho = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
                    player.pos = 200

                if event.key == pygame.K_LEFT:
                    player.pos = -250
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    for branch in galho:
                        branch.rect.y += 100
                        if branch.rect.top >= HEIGHT:
                            branch.kill()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.pos = 0
                if event.key == pygame.K_RIGHT:
                    player.pos = 0
            
        while len(galho) < 4:
            lista_posicao = [200, 450]
            random.shuffle(lista_posicao)
            g = Galho(lista_posicao[0], 10)
            all_sprites.add(g)
            galho.add(g)

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, galho, False)
        if hits:
            running = False
                    
        screen.fill(BLACK)
#        screen.blit(background.image, background.rect)
#        screen.blit(text, textRect)
        all_sprites.draw(screen)
        pygame.display.flip()
                    
                
finally:
    pygame.quit()
