# Imports
import pygame
pygame.init()

# Tela
largura = 600
altura = 800
screen = pygame.display.set_mode([altura, largura])

# Looping principal
running = True
while running:

    # Botão de fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cor do fundo
    screen.fill((255, 255, 255))

    # Atualiza tela
    pygame.display.flip()

pygame.quit()