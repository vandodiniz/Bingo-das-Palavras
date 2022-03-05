import random as rd
import pygame
pygame.init() 

# BANCO DE PALAVRAS
lugares = ['Casa', 'Internet', 'Praia', 'Cinema', 'Clube', 'Restaurante', 'Aeroporto', 'Parque']
animais = ['Gato', 'Cachorro', 'Coelho', 'Tubarão', 'Camelo', 'Tartaruga', 'Tigre', 'Rato', 'Porco', 'Cavalo']
comidas = ['Pão', 'Cenoura', 'Carne', 'Banana', 'Semente', 'Maça', 'Macarrão', 'Arroz', 'Hambúrguer', 'Pizza']
objetos = ['Calculadora', 'Mesa', 'Sofá', 'Computador', 'TV', 'Geladeira', 'Celular', 'Pia', 'Chuveiro']
extras = ['Estrela', 'Basquete', 'Futebol', 'LOL', 'Guerra', 'Nação', 'Médico', 'Xadrez', 'Livro']
listas = [lugares, animais, comidas, objetos, extras]

# SELEÇÃO DAS PALAVRAS
escolhidas = []
for lista in listas:
    for c in range(0,2):
        palavra = lista[rd.randint(0,len(listas)-1)]
        while palavra in escolhidas:
            palavra = lista[rd.randint(0,len(listas)-1)]
        escolhidas.append(palavra)
rd.shuffle(escolhidas)

cabeçalho = f'{escolhidas[0].center(20)}{escolhidas[1].center(20)}{escolhidas[2].center(20)}{escolhidas[3].center(20)}{escolhidas[4].center(20)}'
linha1 = f'''{''.center(150)}{escolhidas[5].ljust(20)}'''
linha2 = f'''{''.center(150)}{escolhidas[6].ljust(20)}'''
linha3 = f'''{''.center(150)}{escolhidas[7].ljust(20)}'''
linha4 = f'''{''.center(150)}{escolhidas[8].ljust(20)}'''
linha5 = f'''{''.center(150)}{escolhidas[9].ljust(20)}'''