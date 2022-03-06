# Imports e Loads
import pygame
pygame.init()
import backend

############################################## FUNÇÕES ###################################################################
def proximo_turno():
    tela.fill((255, 255, 255))
    coordenada = fonte1.render(backend.coordenadas[turno], True, (0,0,0))
    tela.blit(coordenada, (300,300))
    pygame.display.update()
    
    turno_on = True
    while turno_on:
        # Botão de fechar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

            # Terminar turno
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    turno_on = False

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


############################################## LOOPING PRINCIPAL ###################################################################
turno = 0
running = True
while running:

    # Cor do fundo
    tela.fill((255, 255, 255))

    # Palavras Selecionadas:
    cabeçalho = fonte1.render(backend.cabeçalho, True, (0,0,0))
    linha1 = fonte1.render(backend.linha1, True, (0,0,0))
    linha2 = fonte1.render(backend.linha2, True, (0,0,0))
    linha3 = fonte1.render(backend.linha3, True, (0,0,0))
    linha4 = fonte1.render(backend.linha4, True, (0,0,0))
    linha5 = fonte1.render(backend.linha5, True, (0,0,0))
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
            if event.key == pygame.K_SPACE:
                proximo_turno()
                turno += 1

    # Atualiza tela
    pygame.display.update()

pygame.quit()
