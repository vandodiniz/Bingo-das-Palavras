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

# COORDENADAS
coordenadas = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']
rd.shuffle(coordenadas)
print(coordenadas)

# FONTE
cabeçalho = f'{escolhidas[0].center(20)}{escolhidas[1].center(20)}{escolhidas[2].center(20)}{escolhidas[3].center(20)}{escolhidas[4].center(20)}'
linha1 = f'''{''.center(150)}{escolhidas[5].ljust(20)}1'''
linha2 = f'''{''.center(150)}{escolhidas[6].ljust(20)}2'''
linha3 = f'''{''.center(150)}{escolhidas[7].ljust(20)}3'''
linha4 = f'''{''.center(150)}{escolhidas[8].ljust(20)}4'''
linha5 = f'''{''.center(150)}{escolhidas[9].ljust(20)}5'''
