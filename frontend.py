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


turno = 0
# Looping principal
running = True
while running:

    # Cor do fundo
    tela.fill((255, 255, 255))

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

    # Botão de fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Proximo Turno
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                tela.fill((255, 255, 255))
                pygame.display.update()
                tela.fill((0,0,0))
                pygame.display.update()
                tela.fill((100,0,0))
                pygame.display.update()
                tela.fill((0,100,0))
                pygame.display.update()
                tela.fill((0,0,100))
                pygame.display.update()
                tela.fill((100,100,100))
                pygame.display.update()
                tela.fill((255, 255, 255))
                while True:
                    coordenada = fonte1.render(modulo.coordenadas[turno], True, (0,0,0))
                    tela.blit(coordenada, (300,300))
                    pygame.display.update()
                    input()
                    break
                turno += 1

    # Atualiza tela
    pygame.display.update()

pygame.quit()