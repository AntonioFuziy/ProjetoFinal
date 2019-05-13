import pygame
from os import path

img_dir = path.join(path.dirname(__file__),'img')

WIDTH  = 1000
HEIGHT = 800
FPS    = 60
VEL    = 2
BACKGROUND_VEL = VEL*0.95

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game in python")

class Background(pygame.sprite.Sprite):
    def __init__(self):

        BACKGROUND = pygame.image.load(path.join(img_dir,"Imagem de fundo.jpg")).convert()
        self.image = BACKGROUND
        self.image = pygame.transform.scale(BACKGROUND,(WIDTH, HEIGHT))
        self.image.set_colorkey((0,0,0))

        self.rect  = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def move(self, xdir, ydir):
        self.rect.x += xdir*BACKGROUND_VEL
        self.rect.y += ydir*BACKGROUND_VEL


class Player(pygame.sprite.Sprite):
    def __init__(self):

        PERSONAGEM = pygame.image.load(path.join(img_dir,"PersonagemTeste2.png")).convert_alpha()
        self.image = PERSONAGEM
        self.image = pygame.transform.scale(PERSONAGEM,(60,75))
        self.image.set_colorkey((0,0,0))

        #Local do retangulo
        self.rect  = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 610

    def move(self, xdir, ydir):
        self.rect.x += xdir*VEL
        self.rect.y += ydir*VEL


class Bullet(pygame.sprite.Sprite):
    def __init__(self):

        BULLET = pygame.image.load(path.join(img_dir, "Bala.png")).convert_alpha()
        self.image = BULLET
        self.image = pygame.transform.scale(BULLET, (50,40))
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()

        self.speedx = -10

    def shot(self, xdir, ydir):
        self.rect.x += xdir
        if self.rect.right > WIDTH:
            self.kill()

clock      = pygame.time.Clock()

player     = Player()
background = Background()
bullet     = Bullet()

running = True

while running:
    pygame.init()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.shot(1, 0)


    activeKey = pygame.key.get_pressed()
    if activeKey[pygame.K_RIGHT]:
        background.move(-1, 0)
        player.move(1,0)
    if activeKey[pygame.K_LEFT]:
        background.move(1, 0)
        player.move(-1,0)
    if activeKey[pygame.K_DOWN]:
        background.move(0, 1)
    if activeKey[pygame.K_UP]:
        background.move(0, -1)



    #WHERE STUFF HAPPENS

    #Fills the screen
    screen.fill((0,0,0))

    #Draw the background
    screen.blit(background.image, background.rect)

    #Draw the player
    screen.blit(player.image, player.rect)

    #Draw the ammo
    screen.blit(bullet.image, bullet.rect)

    #pygame.draw.rect(surface, color, rectangle, width)
    #pygame.draw.rect(screen, (RGB), (x,y,w,h), thickness of the line)
    #.draw.rect(screen, (255,0,0), (100,100,100,100), 5)
    #pygame.draw.rect(screen, (255,0,0), (100,300,100,100))
    
    #Size of the surface
    #surf = pygame.Surface((150,75))
    #surf.fill((0,255,0))

    #screen.blit(surface, location)
    #screen.blit(Draw this thing, Here)
    #screen.blit(surf, (500,200))

    pygame.display.update()


pygame.QUIT
