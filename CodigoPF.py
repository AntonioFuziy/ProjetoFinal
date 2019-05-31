import pygame
from os import path
import random
import time


img_dir = path.join(path.dirname(__file__),'img')

WIDTH  = 995
HEIGHT = 654
FPS    = 45

SENTIDO = 1

GROUND = HEIGHT - 120
PONTOS = 0

WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVIDADE  = 2
JUMP_SIZE  = 30
DELAY_TIRO = 1000 # milisegundos
DELAY_HIT  = 1000 # milisegundos

STILL   = 0
JUMPING = 1
FALLING = 2

INITIAL_BLOCKS = 5

bala_frente = 'Bala.png'
bala_traz = 'BalaInvertida.png'
personagem_frente = 'PersonagemTeste.png'
personagem_traz = 'PersonagemTesteInvertido.png'
block = 'bloco.png'

LISTA_MONSTROS = ['MobEspadaStop.png','Corsinha.jpg']
LISTA_MONSTROS_INVERTIDO = ['MobEspada.png','CorsinhaInvertido.jpg']
LISTA_ALIADOS = ['CorsinhaInvertido.jpg']

VIDA = 10
VIDA_ALIADO = 3
VIDA_MOB = 3

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
        
        if self.rect.left > 0:
            self.rect.left = 0
        if self.rect.right < WIDTH:
            self.rect.right = WIDTH

        #print(self.rect,self.speedx)

class Mob(pygame.sprite.Sprite):
    
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        
        mob_image = pygame.image.load(path.join(img_dir,LISTA_MONSTROS[0])).convert_alpha()
        
        self.image = pygame.transform.scale(mob_image,(70,60))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 990
        self.rect.y = HEIGHT - 120
        
        self.speedx = 3
        self.speedy = 0

        self.health = 3
        
        self.player = player
        
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
        
        if self.speedx >= 0:
            mob_image = pygame.image.load(path.join(img_dir,(LISTA_MONSTROS[0]))).convert_alpha()
            self.image = mob_image
            self.image = pygame.transform.scale(mob_image,(50,40))
        
        if self.speedx < 0:
            mob_image = pygame.image.load(path.join(img_dir,(LISTA_MONSTROS[0]))).convert_alpha()
            self.image = mob_image
            self.image = pygame.transform.scale(mob_image,(50,40))
            
        if abs(self.rect.centerx - player.rect.centerx) < 90:
           self.speedx = 0
        if abs(self.rect.centerx - player.rect.centerx) >= 90:
            self.speedx = -3
        
        #if self.health <= 0:

class Mob_aliado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        aliado_image = pygame.image.load(path.join(img_dir,(LISTA_ALIADOS[0]))).convert_alpha()
        
        self.image = aliado_image
        
        self.image = pygame.transform.scale(aliado_image,(70,60))

        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.x = 0
        self.rect.y = HEIGHT - 120
        
        self.speedx = 3
        
        self.health = 2
        
    def update(self):
        
        self.rect.x += self.speedx
        
        if self.rect.bottom > HEIGHT - 120:
            self.rect.bottom = HEIGHT - 120
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        
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

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("MINEEEE!!!")

clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()
previous_time2 = pygame.time.get_ticks()
previous_time3 = pygame.time.get_ticks()

previous_time5 = pygame.time.get_ticks()
previous_time6 = pygame.time.get_ticks()

player = Player()
background = Background()

all_sprites = pygame.sprite.Group()

all_sprites.add(background) 
all_sprites.add(player)

mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
aliados = pygame.sprite.Group()

font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 32)
text = font.render("Pontos: {0}".format(PONTOS), True, YELLOW)
textRect = text.get_rect()
textRect.center = (WIDTH // 2, 50)

for i in range(1):
    mob=Mob(player)
    all_sprites.add(mob)
    mobs.add(mob)

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
                
                if event.key == pygame.K_SPACE:
                    current_time = pygame.time.get_ticks()
                    if current_time - previous_time > DELAY_TIRO:
                        previous_time = current_time
                        if SENTIDO == 1:
                            bullet = Bullet(player.rect.right, player.rect.centery, 7)
                            bala = pygame.image.load(path.join(img_dir, bala_frente)).convert_alpha() 
                            bullet.image = bala
                            bullet.image = pygame.transform.scale(bullet.image,(50,40))
                            all_sprites.add(bullet)
                            bullets.add(bullet)
                           
                        if SENTIDO == 2:
                            bullet = Bullet(player.rect.left, player.rect.centery, -7)
                            bala = pygame.image.load(path.join(img_dir, bala_traz)).convert_alpha() 
                            bullet.image = bala
                            bullet.image = pygame.transform.scale(bullet.image,(50,40))
                            all_sprites.add(bullet)
                            bullets.add(bullet)
            if PONTOS >= 5:        
                if event.key == pygame.K_w:
                    #aliado_image = pygame.image.load(path.join(img_dir,(LISTA_ALIADOS[0]))).convert_alpha()
                    #Mob_aliado.image = pygame.transform.scale(Mob_aliado.image,(70,60))
                    aliado = Mob_aliado()
                    all_sprites.add(aliado)
                    aliados.add(aliado)
                    PONTOS -= 5 
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    player.speedx = 0
                    background.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                    background.speedx = 0
        
        all_sprites.update()
        
        hits = pygame.sprite.groupcollide(mobs, bullets, False, True)
        
        for mob in hits:
            mob.health -= 1
            if mob.health <= 0:
                mob.kill()
                PONTOS += 5
                mob=Mob(player)
                #all_sprites.add(mob)
                #mobs.add(mob)
        text = font.render("Pontos: {0}".format(PONTOS), True, YELLOW)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, 50)

        current_time = pygame.time.get_ticks()
        if len(mobs) < 1 and current_time - previous_time2 > 5000:
            previous_time2 = current_time
            mob=Mob(player)
            mob.image = pygame.image.load(path.join(img_dir,(LISTA_MONSTROS[1])))
            mob.image = pygame.transform.scale(mob.image,(50,40))
            all_sprites.add(mob)
            mobs.add(mob)
        
        hits = pygame.sprite.groupcollide(aliados,mobs,False,False)
        
        for aliado in hits:
            aliados.health -= 1
            if aliados.health <= 0:
                aliados.kill()
                aliado=Mob_aliado()
#            current_time5 = pygame.time.get_ticks()
#            if current_time5 - previous_time5 > DELAY_HIT and VIDA_ALIADO > 0:
#                previous_time5 = current_time5
#                VIDA_ALIADO -= 1   
#                
#            if VIDA_ALIADO <= 0:
#                aliados.kill()
#            
#            current_time6 = pygame.time.get_ticks()
#            if current_time6 - previous_time6 > DELAY_HIT and VIDA_MOB > 0:
#                previous_time6 = current_time6
#                VIDA_MOB -= 1
#            
#            if VIDA_MOB <= 0:
#                mobs.kill()
#            
        hits = pygame.sprite.spritecollide(player,mobs,False,pygame.sprite.collide_circle)
        
        if hits:
            current_time2 = pygame.time.get_ticks()
            if current_time2 - previous_time3 > DELAY_HIT and VIDA > 0:
                previous_time3 = current_time2
                VIDA -= 1
                #print(current_time2 - previous_time3)
                print(VIDA)
            if VIDA <= 0:
                running = False
            mob.image = pygame.image.load(path.join(img_dir,('MobEspada.png'))).convert_alpha()
            MobEspada = mob.image
            mob.image = pygame.transform.scale(MobEspada,(50,40))
            all_sprites.add(mob)
            mobs.add(mob)
            #mob.speedx = 0
            #mob.rect.x += 100
            #time.sleep(1)
            
        screen.fill(BLACK)
        screen.blit(background.image, background.rect)
        screen.blit(text, textRect)
        all_sprites.draw(screen)
        pygame.display.flip()

finally:
    pygame.quit()