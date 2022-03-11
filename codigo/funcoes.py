import sys
import time
import random as rd
import cfg
import button
import controle

############################################## FUNÇÕES ###################################################################


def base_do_jogo():
    cfg.tela.blit(cfg.image1, (0, 0))
    escolhida1 = cfg.fonte1.render(controle.escolhidas[0], True, (0,0,0))
    escolhida2 = cfg.fonte1.render(controle.escolhidas[1], True, (0,0,0))
    escolhida3 = cfg.fonte1.render(controle.escolhidas[2], True, (0,0,0))
    escolhida4 = cfg.fonte1.render(controle.escolhidas[3], True, (0,0,0))
    escolhida5 = cfg.fonte1.render(controle.escolhidas[4], True, (0,0,0))
    escolhida6 = cfg.fonte1.render(controle.escolhidas[5], True, (0,0,0))
    escolhida7 = cfg.fonte1.render(controle.escolhidas[6], True, (0,0,0))
    escolhida8 = cfg.fonte1.render(controle.escolhidas[7], True, (0,0,0))
    escolhida9 = cfg.fonte1.render(controle.escolhidas[8], True, (0,0,0))
    escolhida10 = cfg.fonte1.render(controle.escolhidas[9], True, (0,0,0))
    cfg.tela.blit(escolhida1, (68, 80))
    cfg.tela.blit(escolhida2, (238, 80))
    cfg.tela.blit(escolhida3, (408, 80))
    cfg.tela.blit(escolhida4, (578, 80))
    cfg.tela.blit(escolhida5, (740, 80))
    cfg.tela.blit(escolhida6, (905, 150))
    cfg.tela.blit(escolhida7, (905, 235))
    cfg.tela.blit(escolhida8, (905, 320))
    cfg.tela.blit(escolhida9, (905, 410))
    cfg.tela.blit(escolhida10, (905, 495))

def sorteador():
    controle.escolhidas.clear()
    for lista in controle.listas:
        for c in range(0,2):
            palavra = lista[rd.randint(0,len(controle.listas)-1)]
            while palavra in controle.escolhidas:
                palavra = lista[rd.randint(0,len(controle.listas)-1)]
            controle.escolhidas.append(palavra)
    rd.shuffle(controle.escolhidas)
    rd.shuffle(controle.coordenadas)
    print(controle.coordenadas)

def proximo_turno():
    cfg.tela.fill((255, 255, 255))
    
    cfg.tela.blit(cfg.timer3, (0, 0))
    cfg.pygame.display.flip() 
    cfg.pygame.time.delay(1000)

    cfg.tela.blit(cfg.timer2, (0, 0))
    cfg.pygame.display.flip()
    cfg.pygame.time.delay(1000)

    cfg.tela.blit(cfg.timer1, (0, 0))
    cfg.pygame.display.flip()
    cfg.pygame.time.delay(1000)

    cfg.tela.blit(cfg.imagem_coordenada, (0, 0))
    coordenada = cfg.fonte2.render(controle.coordenadas[controle.turno], True, (0,0,0))
    cfg.tela.blit(coordenada, (475,350))
    cfg.pygame.display.flip()
    
    cfg.pygame.event.get().clear  
    controle.turno +=1

    turno_on = True
    while turno_on:
        
        for event in cfg.pygame.event.get():
           
            # Botão de fechar
            if event.type == cfg.pygame.QUIT:
                running = False
                cfg.pygame.quit()
                sys.exit()

            # Terminar turno
            if event.type == cfg.pygame.KEYDOWN:
                if event.key == cfg.pygame.K_SPACE:
                    turno_on = False

def mostra_coordenada():
    cfg.tela.fill((255, 255, 255))
    
    cfg.tela.blit(cfg.timer3, (0, 0))
    cfg.pygame.display.flip() 
    time.sleep(1)

    cfg.tela.blit(cfg.timer2, (0, 0))
    cfg.pygame.display.flip()
    time.sleep(1)

    cfg.tela.blit(cfg.timer1, (0, 0))
    cfg.pygame.display.flip()
    time.sleep(1)

    cfg.tela.blit(cfg.imagem_coordenada, (0, 0))
    coordenada = cfg.fonte2.render(controle.coordenadas[controle.turno], True, (0,0,0))
    cfg.tela.blit(coordenada, (475,350))
    cfg.pygame.display.flip()
    
    controle.turno +=1
    cfg.pygame.event.get().clear  

    coordenada_on = True
    while coordenada_on:
        
        for event in cfg.pygame.event.get():
           
            # Botão de fechar
            if event.type == cfg.pygame.QUIT:
                cfg.pygame.quit()
                sys.exit()

            # Voltar pro tabuleiro turno
            if event.type == cfg.pygame.KEYDOWN:
                if event.key == cfg.pygame.K_SPACE:
                    coordenada_on = False

def reiniciar_jogo():
    sorteador()
    controle.turno = 0
    for botao in button.botoes:
        botao.cliques = 0

def fim_do_jogo():

    score = 0
    for botao in button.botoes:
        if botao.cliques == 1:
            score += 1


    cfg.tela.fill((255,255,255))
    mensagem = f'Parabéns, sua pontuação foi de {score}/25'
    mensagem_formatada = cfg.fonte3.render(mensagem, True, (0,0,0))
    ret_msg = mensagem_formatada.get_rect()
    ret_msg.center = (cfg.largura/2,cfg.altura/2)
    cfg.tela.blit(mensagem_formatada, ret_msg)

    mensagem = f'Aperte ESPAÇO para fechar o jogo'
    mensagem_formatada = cfg.fonte4.render(mensagem, True, (0,0,0))
    ret_msg = mensagem_formatada.get_rect()
    ret_msg.center = (cfg.largura/2,600)
    cfg.tela.blit(mensagem_formatada, ret_msg)

    mensagem = f'Aperte R para reiniciar o jogo'
    mensagem_formatada = cfg.fonte4.render(mensagem, True, (0,0,0))
    ret_msg = mensagem_formatada.get_rect()
    ret_msg.center = (cfg.largura/2,650)
    cfg.tela.blit(mensagem_formatada, ret_msg)

    cfg.pygame.display.flip()



    controle = True
    while controle:

        # Lista de eventos
        for event in cfg.pygame.event.get():

            # Botão de fechar
            if event.type == cfg.pygame.QUIT:
                cfg.pygame.quit()
                sys.exit()
                
             # Botões do Teclado
            if event.type == cfg.pygame.KEYDOWN:

                # Finalizar Jogo
                if event.key == cfg.pygame.K_SPACE:
                    cfg.pygame.quit()
                    sys.exit()
                    
        
                # Reiniciar Jogo
                if event.key == cfg.pygame.K_r:
                    controle = False
                    reiniciar_jogo()
            