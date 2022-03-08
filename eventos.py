import 

# Proximo Turno
        if event.type == cfg.pygame.KEYDOWN:
            if event.key == cfg.pygame.K_SPACE:
                funcoes.proximo_turno(coordenadas, turno, cfg.tela)
                turno += 1
        
        # Reiniciar Game
            if event.key == cfg.pygame.K_r:
                turno = 0
                funcoes.reiniciar_jogo(escolhidas, coordenadas, listas)