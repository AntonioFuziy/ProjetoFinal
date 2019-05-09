import pygame
from os import path

img_dir = path.join(path.dirname(__file__),'img')

WIDTH = 995
HEIGHT = 654
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVIDADE = -0.4

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
        
    def update(self):
        self.rect.x += self.speedx
       
        player.jump()
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        self.rect.y += self.speedy
        
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT - 87:
            self.rect.bottom = HEIGHT - 87
    
    def jump(self):
        self.speedy -= GRAVIDADE
        self.rect.y += self.speedy
            
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Personagem")

clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir,"Imagem de fundo.jpg"))
background_rect = background.get_rect()

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)    

try:
    running = True
    while running:
        
        clock.tick(FPS)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.speedx = -7
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.speedx = 7
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.speedy = -7
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.speedy += 7
                if event.key == pygame.K_a or event.key == pygame.K_LEFT: 
                    player.speedx += 7
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.speedx -= 7
        
        all_sprites.update()
               
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()
        
finally:
    pygame.quit()






















