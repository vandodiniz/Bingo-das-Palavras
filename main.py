# Imports e Loads
import funcoes
import cfg
import button 

############################################## BANCO DE PALAVRAS ###################################################################

escolhidas = []
coordenadas = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']
lugares = ['Casa', 'Internet', 'Praia', 'Cinema', 'Clube', 'Restaurante', 'Aeroporto', 'Parque']
animais = ['Gato', 'Cachorro', 'Coelho', 'Tubarão', 'Camelo', 'Tartaruga', 'Tigre', 'Rato', 'Porco', 'Cavalo']
comidas = ['Pão', 'Cenoura', 'Carne', 'Banana', 'Semente', 'Maça', 'Macarrão', 'Arroz', 'Hambúrguer', 'Pizza']
objetos = ['Calculadora', 'Mesa', 'Sofá', 'Computador', 'TV', 'Geladeira', 'Celular', 'Pia', 'Chuveiro']
extras = ['Estrela', 'Basquete', 'Futebol', 'LOL', 'Guerra', 'Nação', 'Médico', 'Xadrez', 'Livro']
listas = [lugares, animais, comidas, objetos, extras]

############################################## LOOPING PRINCIPAL ###################################################################
funcoes.sorteador(escolhidas, coordenadas, listas)
turno = 0
score = 0
running = True
while running:

    # Desenha tabuleiro
    funcoes.base_do_jogo(escolhidas, cfg.tela) 
    
    # Sobreposições dos botões
    for botao in button.botoes:
        if botao.hitbox.collidepoint(cfg.pygame.mouse.get_pos()):
            cfg.pygame.draw.rect(cfg.tela, (0,0,255), ( botao.pos[0], botao.pos[1],165,80), 3)
            cfg.pygame.display.flip()

   
    for event in cfg.pygame.event.get():

        # Botão de fechar
        if event.type == cfg.pygame.QUIT:
            running = False

        # Proximo Turno
        if event.type == cfg.pygame.KEYDOWN:
            if event.key == cfg.pygame.K_SPACE:
                	
                funcoes.proximo_turno(coordenadas, turno, cfg.tela)
                turno += 1

        



    # Atualiza tela
    cfg.pygame.display.flip()

    # Fim do jogo e Pontuação
    if turno == 25:
        print('FIM')
        running = False

cfg.pygame.quit()
