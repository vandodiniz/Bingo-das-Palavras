import random as rd
import pygame
pygame.init()

############################################## ESPECIFICAÇÕES ###################################################################

# Clock
clock = pygame.time.Clock()
clock.tick(60)

# Fontes
fonte1 = pygame.font.SysFont('arial', 24, True)

# Imagens 
image = pygame.image.load('imagens/base.jpg')

############################################## FUNÇÕES ###################################################################

def base_do_jogo(escolhidas, tela):
    tela.blit(image, (0, 0))
    escolhida1 = fonte1.render(escolhidas[0], True, (0,0,0))
    escolhida2 = fonte1.render(escolhidas[1], True, (0,0,0))
    escolhida3 = fonte1.render(escolhidas[2], True, (0,0,0))
    escolhida4 = fonte1.render(escolhidas[3], True, (0,0,0))
    escolhida5 = fonte1.render(escolhidas[4], True, (0,0,0))
    escolhida6 = fonte1.render(escolhidas[5], True, (0,0,0))
    escolhida7 = fonte1.render(escolhidas[6], True, (0,0,0))
    escolhida8 = fonte1.render(escolhidas[7], True, (0,0,0))
    escolhida9 = fonte1.render(escolhidas[8], True, (0,0,0))
    escolhida10 = fonte1.render(escolhidas[9], True, (0,0,0))
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

def sorteador(escolhidas, coordenadas, listas):
    escolhidas.clear()
    for lista in listas:
        for c in range(0,2):
            palavra = lista[rd.randint(0,len(listas)-1)]
            while palavra in escolhidas:
                palavra = lista[rd.randint(0,len(listas)-1)]
            escolhidas.append(palavra)
    rd.shuffle(escolhidas)
    rd.shuffle(coordenadas)

def proximo_turno(coordenadas, turno, tela):
    tela.fill((255, 255, 255))
    coordenada = fonte1.render(coordenadas[turno], True, (0,0,0))
    tela.blit(coordenada, (300,300))
    pygame.display.flip()
    
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