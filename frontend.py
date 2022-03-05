# Imports e Loads
import pygame
pygame.init()
import modulo

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

# Looping principal
running = True
while running:

    # Cor do fundo
    tela.fill((255, 255, 255))

    # Botão de fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Proximo Turno
        if event.type == 

    # Palavras Selecionadas:
    cabeçalho = fonte1.render(modulo.cabeçalho, True, (0,0,0))
    linha1 = fonte1.render(modulo.linha1, True, (0,0,0))
    linha2 = fonte1.render(modulo.linha2, True, (0,0,0))
    linha3 = fonte1.render(modulo.linha3, True, (0,0,0))
    linha4 = fonte1.render(modulo.linha4, True, (0,0,0))
    linha5 = fonte1.render(modulo.linha5, True, (0,0,0))
    tela.blit(cabeçalho, (20, 100))
    tela.blit(linha1, (20, 150))
    tela.blit(linha2, (20, 200))
    tela.blit(linha3, (20, 250))
    tela.blit(linha4, (20, 300))
    tela.blit(linha5, (20, 350))
    


    # for c in range(5,10):
    #     fonte1.render(modulo.escolhidas[c], True, (0,0,0))
    #     tela.blit(texto, (500, y))
    #     y+=75
    
    # Atualiza tela
    pygame.display.update()

pygame.quit()