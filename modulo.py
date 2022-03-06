import pygame
import backend
import frontend

pygame.init()

def proximo_turno():
    frontend.tela.fill((255, 255, 255))
    coordenada = frontend.fonte1.render(backend.coordenadas[frontend.turno], True, (0,0,0))
    frontend.tela.blit(coordenada, (300,300))
    pygame.display.update()
    
    turno_on = True
    while turno_on:
        # Botão de fechar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frontend.running = False

            # Terminar turno
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    turno_on = False
                    
