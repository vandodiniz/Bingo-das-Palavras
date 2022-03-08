import random as rd
import cfg
import button

############################################## FUNÇÕES ###################################################################


def base_do_jogo(escolhidas, tela):
    tela.blit(cfg.image, (0, 0))
    escolhida1 = cfg.fonte1.render(escolhidas[0], True, (0,0,0))
    escolhida2 = cfg.fonte1.render(escolhidas[1], True, (0,0,0))
    escolhida3 = cfg.fonte1.render(escolhidas[2], True, (0,0,0))
    escolhida4 = cfg.fonte1.render(escolhidas[3], True, (0,0,0))
    escolhida5 = cfg.fonte1.render(escolhidas[4], True, (0,0,0))
    escolhida6 = cfg.fonte1.render(escolhidas[5], True, (0,0,0))
    escolhida7 = cfg.fonte1.render(escolhidas[6], True, (0,0,0))
    escolhida8 = cfg.fonte1.render(escolhidas[7], True, (0,0,0))
    escolhida9 = cfg.fonte1.render(escolhidas[8], True, (0,0,0))
    escolhida10 = cfg.fonte1.render(escolhidas[9], True, (0,0,0))
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
    coordenada = cfg.fonte1.render(coordenadas[turno], True, (0,0,0))
    tela.blit(coordenada, (300,300))
    cfg.pygame.display.flip()
    
    turno_on = True
    while turno_on:
        
        for event in cfg.pygame.event.get():
           
            # Botão de fechar
            if event.type == cfg.pygame.QUIT:
                running = False
                exit()

            # Terminar turno
            if event.type == cfg.pygame.KEYDOWN:
                if event.key == cfg.pygame.K_SPACE:
                    turno_on = False
            
def reiniciar_jogo(escolhidas, coordenadas, listas):
    sorteador(escolhidas, coordenadas, listas)
    for botao in button.botoes:
        botao.cliques = 0