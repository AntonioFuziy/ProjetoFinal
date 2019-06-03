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

DELAY_TIRO = 10 # milisegundos
DELAY_HIT  = 1000 # milisegundos
DELAY_SPAWN = random.randint(1,3)

STILL   = 0
WALKING = 1
FALLING = 3
JUMPING = 2
SHOOTING = 4

ROUNDS = 1
DURACAO_ROUNDS = 15000
INTERVALO_ROUNDS = 10000

LEFT = False
RIGHT = False
WALKCOUNT = 0

bala_frente = 'Bala.png'
bala_traz = 'BalaInvertida.png'
personagem_frente = 'PersonagemTeste.png'
personagem_traz = 'PersonagemTesteInvertido.png'
block = 'bloco.png'

LISTA_MONSTROS = ['MobEspadaStop.png','Corsinha.jpg']
LISTA_MONSTROS_INVERTIDO = ['MobEspada.png','CorsinhaInvertido.jpg']
LISTA_ALIADOS = ['CorsinhaInvertido.jpg']

#ANDA_DIREITA = [pygame.image.load('Personagem-1.png.png'),pygame.image.load('Personagem-2.png.png'),pygame.image.load('Personagem-3.png.png'),pygame.image.load('Personagem-4.png.png'),pygame.image.load('Personagem-5.png.png'),pygame.image.load('Personagem-6.png.png'),pygame.image.load('Personagem-7.png.png'),pygame.image.load('Personagem-8.png.png'),pygame.image.load('Personagem-9.png.png')]

VIDA = 10
VIDA_ALIADO = 3
VIDA_MOB = 3

def load_spritesheet(spritesheet,rows,columns):
    sprite_width =spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    sprites = []
    for row in range(rows):
        for column in range(columns):
            x = column*sprite_width
            y = row*sprite_height
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)
            
            image = pygame.Surface((sprite_width, sprite_height))
            
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites
            
class Player(pygame.sprite.Sprite):
    def __init__(self, player_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        
        player_sheet = pygame.transform.scale(player_sheet,(480,480))
        
        spritesheet = load_spritesheet(player_sheet,4,4)
        self.animations = {
            WALKING: spritesheet[0:7],
            STILL: spritesheet[7:12],
            SHOOTING: spritesheet[12:18],
            }
        
        self.state = STILL
        
        self.animation = self.animations[self.state]
        
        self.frame = 0
        self.image = self.animation[self.frame]
        
        #personagem = pygame.image.load(path.join(img_dir,personagem_frente)).convert_alpha()
        
        #self.image = personagem
        #self.image = pygame.transform.scale(personagem,(80,100))
        #self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 120
        
        self.speedx = 0
        self.speedy = 0
        
        self.radius =  int(self.rect.width * .85 / 2)
        self.health = 3
        
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 300
        
    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

    def update(self):
#        if self.speedx < 0:
#            player_sheet = pygame.transform.scale(player_sheet,(200,200))
        
#            spritesheet = load_spritesheet(player_sheet,3,3)
            
#            self.animations = {
#            STILL: spritesheet[0:3], 
#            WALKING: spritesheet[0:9],
#            JUMPING: spritesheet[6:9],
#            }
            
        now = pygame.time.get_ticks()
        
        elapsed_ticks = now - self.last_update
        
        if elapsed_ticks > self.frame_ticks:
            
            self.last_update = now
            
            self.frame += 1
            
            self.animation = self.animations[self.state]
            
        if self.frame >= len(self.animation):
            self.frame = 0
        
        center = self.rect.center
        
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        self.rect.x += self.speedx
        
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


class Mob(pygame.sprite.Sprite):
    
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        
        mob_image = pygame.image.load(path.join(img_dir,LISTA_MONSTROS[0])).convert_alpha()
        
        self.image = pygame.transform.scale(mob_image,(70,60))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = HEIGHT - 120
        
        self.speedx = 3
        self.speedy = 0

        self.health = 3
        
        self.player = player
        
    def update(self):
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy        
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = -self.speedx
        
        if self.rect.bottom > HEIGHT - 120:
            self.rect.bottom = HEIGHT - 120

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
        
        self.rect.x = -100
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
previous_time7 = pygame.time.get_ticks()
previous_time8 = pygame.time.get_ticks()

player_sheet = pygame.image.load(path.join(img_dir,'Personagem_GIF_Frente.png')).convert_alpha()

player = Player(player_sheet)
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
                    player_sheet = pygame.image.load(path.join(img_dir,'Personagem_GIF_Frente.png')).convert_alpha()
                    player.state = WALKING
                    SENTIDO = 1
                    player.speedx += 5
                    background.speedx -= 7
                    #player.image = pygame.image.load(path.join(img_dir, 'PersonagemTeste.png')).convert_alpha()
                    #player.image = pygame.transform.scale(player.image,(80,100))
                    
                if event.key == pygame.K_LEFT:
                    SENTIDO = 2
                    player_sheet = pygame.image.load(path.join(img_dir,'Personagem_GIF_Frente.png')).convert_alpha()
                    player.state = STILL
                    player.speedx -= 5
                    background.speedx += 7
                    personagem = pygame.image.load(path.join(img_dir, personagem_traz))
                    #player.image = personagem
                    #player.image = pygame.transform.scale(personagem,(80,100))
        
                if event.key == pygame.K_UP:
                    player.jump()
                
                if event.key == pygame.K_SPACE:
                    current_time = pygame.time.get_ticks()
                    if current_time - previous_time > DELAY_TIRO:
                        previous_time = current_time
                        if SENTIDO == 1:
                            player.state = SHOOTING
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
                if event.key == pygame.K_w:
                    if PONTOS >= 5:        
                        #aliado_image = pygame.image.load(path.join(img_dir,(LISTA_ALIADOS[0]))).convert_alpha()
                        #Mob_aliado.image = pygame.transform.scale(Mob_aliado.image,(70,60))
                        aliado = Mob_aliado()
                        all_sprites.add(aliado)
                        aliados.add(aliado)
                        PONTOS -= 5 
                            
            if event.type == pygame.KEYUP:
                player.state = STILL
                if event.key == pygame.K_LEFT: 
                    player.speedx = 0
                    background.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.state = WALKING
                    player.speedx = 0
                    background.speedx = 0
            
        #Spawn e sistema de Rounds
        current_time7 = pygame.time.get_ticks()
        if current_time7 - previous_time7 > random.randint(1,3) *1000:
            previous_time7 = current_time7
            mob.image = pygame.image.load(path.join(img_dir,('MobEspada.png')))
            mob.image = pygame.transform.scale(mob.image,(70,60))
            mob=Mob(player)
            current_time8 = pygame.time.get_ticks()
            if current_time8 - previous_time8 < INTERVALO_ROUNDS:
                all_sprites.add(mob)
                mobs.add(mob)
                if len(mobs) == 0:
                    ROUNDS += 1
                    INTERVALO_ROUNDS +=  current_time8 - previous_time8 + 5000

                    
            #elif current_time8 - previous_time8 > DURACAO_ROUNDS:
            
        print(len(mobs))
        
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

        
        hits = pygame.sprite.groupcollide(aliados,mobs,False,False)
        
        for aliado in hits:
            aliado.health -= 1
            #mob.image = pygame.image.load(path.join(img_dir,(LISTA_MONSTROS[1])))
            #mob.image = pygame.transform.scale(mob.image,(70,60))
            for mob in hits[aliado]:
                mob.health -= 1
                if aliado.health <= 0:
                    aliado.kill()
                    aliado=Mob_aliado()
                elif mob.health <= 0:
                    mob.kill()
                    mob=Mob(player)
                    PONTOS += 1
                
        hits = pygame.sprite.spritecollide(player,mobs,False,pygame.sprite.collide_circle)
        
        if hits:
            current_time2 = pygame.time.get_ticks()
            if current_time2 - previous_time3 > DELAY_HIT and VIDA > 0:
                previous_time3 = current_time2
                VIDA -= 1
                print(VIDA)
            if VIDA <= 0:
                running = False
            mob.image = pygame.image.load(path.join(img_dir,('MobEspada.png'))).convert_alpha()
            MobEspada = mob.image
            mob.image = pygame.transform.scale(MobEspada,(70,60))
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