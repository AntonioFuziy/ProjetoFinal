import pygame
from os import path
import random
import time

img_dir = path.join(path.dirname(__file__),'img')
snd_dir = path.join(path.dirname(__file__), 'snd2')


WIDTH = 800
HEIGHT = 600 

FPS = 60

WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)

TAXA_VIDA = 200
VIDA = 100

GALHO_LISTA = [(450, HEIGHT - 120),
               (200, HEIGHT - 270),
               (200, HEIGHT - 420),
               (450, HEIGHT - 570),
               (450, HEIGHT - 720)]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(path.join(img_dir,'Pulica1.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image,(120,120))
        
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH/2 - 30
        self.rect.y = HEIGHT - 100
        
        self.pontos = 0
        self.score = 0

        self.pos = 0
        
    def update(self):
        self.rect.x += self.pos
        self.pontos += self.score
        
        if self.rect.right < WIDTH/2 - 30:
            self.rect.right = WIDTH/2 - 30
        if self.rect.left > WIDTH/2 + 30:
            self.rect.left = WIDTH/2 + 30
        self.score = 0

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.VIDA = VIDA
        self.image = pygame.image.load(path.join(img_dir,'health.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.VIDA,20))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.y = 50

        self.regen = 1

    def update(self):
        if self.VIDA >= 100:
            self.regen = -5
        self.VIDA += self.regen
        if self.VIDA < 0:
            self.VIDA = 0
        self.image = pygame.transform.scale(self.image,(self.VIDA,20))
        self.regen = 0

class Galho(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(img_dir,'Galho.png')).convert_alpha()
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        if self.rect.x == 200:
            self.image = pygame.image.load(path.join(img_dir,'GalhoE.png')).convert_alpha()
            self.image.set_colorkey(BLACK)
        else:
            self.image = pygame.image.load(path.join(img_dir,'GalhoD.png')).convert_alpha()
            self.image.set_colorkey(BLACK)

class Tronco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(img_dir,'Tronco3.png')).convert_alpha()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.y = 0

    def update(self):
        pass
background = pygame.image.load(path.join(img_dir,'Background.jpg'))
background = pygame.transform.scale(background,(800,600))
background_rect = background.get_rect()

imgfundo = pygame.image.load(path.join(img_dir,'MenuFundo.jpg'))
imgfundo = pygame.transform.scale(imgfundo,(800,600))
imgfundo_rect = imgfundo.get_rect()

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(path.join(snd_dir,'MusicaJogo.ogg'))
pygame.mixer.music.set_volume(0.4)
destroy_sound = pygame.mixer.Sound(path.join(snd_dir,'Madeira_hit.wav'))

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("ChopperMAN!!!")

previous_time = pygame.time.get_ticks()

all_sprites = pygame.sprite.Group()
galho = pygame.sprite.Group()

tronco = Tronco()
health = HealthBar()
player = Player()
all_sprites.add(tronco)
all_sprites.add(player)
all_sprites.add(health)

font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 32)
text = font.render("Pontos: {0}".format(player.pontos), True, YELLOW)
textRect = text.get_rect()
textRect.center = (WIDTH // 2 - 300, 50)

for branch in GALHO_LISTA:
    g = Galho(*branch)
    all_sprites.add(g)
    galho.add(g)

try:
    print("------------------------")
    print("       CHOPPERMAN       ")
    print("\nOs controles do jogo são:\nTecla [Direita]  - Mover para a direita\nTecla [Esquerda] - Mover para a esquerda")
    print("Quantas madeiras você consegue cortar?\nBoa sorte!\n")
    print("------------------------")        
    pygame.mixer.music.play(loops=-1)
    
    running = True
    menu = True

    while menu:
        #clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    menu = False

        screen.fill(BLACK)
        screen.blit(imgfundo, imgfundo_rect)
        pygame.display.flip()

    while running:
    
        clock.tick(FPS)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.pos = 170
                    player.image = pygame.image.load(path.join(img_dir,'Pulica3_Invertido.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image,(120,120))

                if event.key == pygame.K_LEFT:
                    player.pos = -220
                    player.image = pygame.image.load(path.join(img_dir,'Pulica3.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image,(120,120))
                    
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    health.regen = 5
                    player.score = 1
                    text = font.render("Pontos: {0}".format(player.pontos), True, YELLOW)
                    textRect = text.get_rect()
                    textRect.center = (WIDTH // 2 - 300, 50)
                    destroy_sound.play()
                    for branch in galho:
                        branch.rect.y += 100
                        if branch.rect.top >= HEIGHT:
                            branch.kill()
                           

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.pos = 0
                    player.image = pygame.image.load(path.join(img_dir,'Pulica1.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image,(120,120))

                if event.key == pygame.K_RIGHT:
                    player.pos = 0
                    player.image = pygame.image.load(path.join(img_dir,'Pulica1_Invertido.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image,(120,120))
            
        if len(galho) < 4:
            lista_posicao = [200, 450]
            random.shuffle(lista_posicao)
            g = Galho(lista_posicao[0], 40)
            all_sprites.add(g)
            galho.add(g)

        if player.pontos > 199:
            TAXA_VIDA = 15
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > TAXA_VIDA:
                health.regen = -1
                previous_time = current_time

        if player.pontos > 149:
            TAXA_VIDA = 30
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > TAXA_VIDA:
                health.regen = -1
                previous_time = current_time

        elif player.pontos > 99:
            TAXA_VIDA = 50
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > TAXA_VIDA:
                health.regen = -1
                previous_time = current_time

        elif player.pontos > 49:
            TAXA_VIDA = 75
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > TAXA_VIDA:
                health.regen = -1
                previous_time = current_time

        elif player.pontos > 19:
            TAXA_VIDA = 100
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > TAXA_VIDA:
                health.regen = -1
                previous_time = current_time  
              
        elif player.pontos > 0:
            current_time = pygame.time.get_ticks()
            if current_time - previous_time > TAXA_VIDA:
                health.regen = -1
                previous_time = current_time

        if health.VIDA <= 0:
            running = False

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, galho, False)
        if hits and player.pos == 170:
            player.pos = -220
        elif hits and player.pos == -220:
            player.pos = 170
                    
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(text, textRect)
        all_sprites.draw(screen)
        pygame.display.flip()
                    
                
finally:
    pygame.quit()
