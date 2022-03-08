import pygame
pygame.init()

############################################## ESPECIFICAÇÕES ###################################################################
# Tela
largura = 1100
altura = 700
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Palavra-Minada') 

# Clock
clock = pygame.time.Clock()
clock.tick(60)

# Fontes
fonte1 = pygame.font.SysFont('arial', 24, True)
fonte2 = pygame.font.SysFont('arial', 100, True)

# Imagens 
image1 = pygame.image.load('imagens/base.jpg').convert()
timer1 = pygame.image.load('imagens/timer1.jpg').convert()
timer2 = pygame.image.load('imagens/timer2.jpg').convert()
timer3 = pygame.image.load('imagens/timer3.jpg').convert()
imagem_coordenada = pygame.image.load('imagens/coordenada.jpg').convert()
