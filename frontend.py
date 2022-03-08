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

# Imagens 
image = pygame.image.load('imagens/base.jpg')


############################################## LOOPING PRINCIPAL ###################################################################
turno = 0
score = 0
running = True
while running:

    # Palavras Selecionadas:
    tela.blit(image, (0, 0))
    escolhida1 = fonte1.render(backend.escolhidas[0], True, (0,0,0))
    escolhida2 = fonte1.render(backend.escolhidas[1], True, (0,0,0))
    escolhida3 = fonte1.render(backend.escolhidas[2], True, (0,0,0))
    escolhida4 = fonte1.render(backend.escolhidas[3], True, (0,0,0))
    escolhida5 = fonte1.render(backend.escolhidas[4], True, (0,0,0))
    escolhida6 = fonte1.render(backend.escolhidas[5], True, (0,0,0))
    escolhida7 = fonte1.render(backend.escolhidas[6], True, (0,0,0))
    escolhida8 = fonte1.render(backend.escolhidas[7], True, (0,0,0))
    escolhida9 = fonte1.render(backend.escolhidas[8], True, (0,0,0))
    escolhida10 = fonte1.render(backend.escolhidas[9], True, (0,0,0))
    tela.blit(escolhida1, (60, 80))
    tela.blit(escolhida2, (230, 80))
    tela.blit(escolhida3, (400, 80))
    tela.blit(escolhida4, (570, 80))
    tela.blit(escolhida5, (725, 80))
    tela.blit(escolhida6, (885, 150))
    tela.blit(escolhida7, (885, 235))
    tela.blit(escolhida8, (885, 315))
    tela.blit(escolhida9, (885, 405))
    tela.blit(escolhida10, (885, 490))


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

    # Fim do jogo e Pontuação
    if turno == 25:
        print('FIM')
        running = False

pygame.quit()
