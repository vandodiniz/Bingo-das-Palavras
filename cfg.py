import pygame
pygame.init()

############################################## ESPECIFICAÇÕES ###################################################################
# Tela
largura = 1000
altura = 600
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Palavra-Minada') 

# Clock
clock = pygame.time.Clock()
clock.tick(60)

# Fontes
fonte1 = pygame.font.SysFont('arial', 24, True)

# Imagens 
image = pygame.image.load('imagens/base.jpg')