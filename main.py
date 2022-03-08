# Imports e Loads
import pygame
pygame.init()
import funcoes

############################################## BANCO DE PALAVRAS ###################################################################

escolhidas = []
coordenadas = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']
lugares = ['Casa', 'Internet', 'Praia', 'Cinema', 'Clube', 'Restaurante', 'Aeroporto', 'Parque']
animais = ['Gato', 'Cachorro', 'Coelho', 'Tubarão', 'Camelo', 'Tartaruga', 'Tigre', 'Rato', 'Porco', 'Cavalo']
comidas = ['Pão', 'Cenoura', 'Carne', 'Banana', 'Semente', 'Maça', 'Macarrão', 'Arroz', 'Hambúrguer', 'Pizza']
objetos = ['Calculadora', 'Mesa', 'Sofá', 'Computador', 'TV', 'Geladeira', 'Celular', 'Pia', 'Chuveiro']
extras = ['Estrela', 'Basquete', 'Futebol', 'LOL', 'Guerra', 'Nação', 'Médico', 'Xadrez', 'Livro']
listas = [lugares, animais, comidas, objetos, extras]


############################################## ESPECIFICAÇÕES ###################################################################
# Tela
largura = 1000
altura = 600
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Palavra-Minada')


############################################## LOOPING PRINCIPAL ###################################################################
funcoes.sorteador(escolhidas, coordenadas, listas)
turno = 0
score = 0
running = True
while running:

    funcoes.base_do_jogo(escolhidas, tela) 
    
    # Botão de fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Proximo Turno
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                funcoes.proximo_turno(coordenadas, turno, tela)
                turno += 1

    # Atualiza tela
    pygame.display.flip()

    # Fim do jogo e Pontuação
    if turno == 25:
        print('FIM')
        running = False

pygame.quit()
