from os import path

img_dir = path.join(path.dirname(__file__),'img')

WIDTH = 995
HEIGHT = 654
FPS = 45

SENTIDO = 1

GROUND = HEIGHT - 120
pontos=0

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
MONSTRO = 'PersonagemTesteInvertido.png'

VIDA = 3
