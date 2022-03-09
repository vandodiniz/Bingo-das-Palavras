# Imports e Loads
import funcoes
import cfg
import button
import controle 

############################################## LOOPING PRINCIPAL ###################################################################

running = True
funcoes.sorteador()

while running:         
    
    # Lista de eventos
    for event in cfg.pygame.event.get():

        # Botão de fechar
        if event.type == cfg.pygame.QUIT:
            running = False

        # Botões do Teclado
        if event.type == cfg.pygame.KEYDOWN:

            # Proximo Turno
            if event.key == cfg.pygame.K_SPACE:

                # Fim do jogo e Pontuação
                if controle.turno == 25:
                    funcoes.fim_do_jogo()

                else:
                    funcoes.proximo_turno()
                    print(controle.turno)
        
            # Reiniciar Game
            if event.key == cfg.pygame.K_r:
                funcoes.reiniciar_jogo()
            
        # Clique do Mouse
        for botao in button.botoes:
            if botao.hitbox.collidepoint(cfg.pygame.mouse.get_pos()):
                if event.type == cfg.pygame.MOUSEBUTTONDOWN:
                    mouse_presses = cfg.pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        botao.trigger()
    
    # Desenha tabuleiro
    funcoes.base_do_jogo()

    # Desenha estado dos botões 
    for botao in button.botoes:
        botao.draw()

    # Desenha a sobreposição
    for botao in button.botoes:
        if botao.hitbox.collidepoint(cfg.pygame.mouse.get_pos()):
            cfg.pygame.draw.rect(cfg.tela, (0,0,255), ( botao.pos[0], botao.pos[1],165,80), 3)

    cfg.pygame.display.flip()

cfg.pygame.quit()
