# Bingo das Palavras
## Introdução

O 'Bingo das Palavras' é inspirado em um jogo de cartas. O objetivo do jogo é os jogadores cooperarem entre si e alcançarem o maior número de acertos possíveis.
A cada turno um jogador vira o mediador da partida. Este mediador então recebe uma coordenada, e precisa com apenas uma palavra, fazer com que os outros jogadores descubram qual a coordenada do turno.   

Para que isso seja possível, cada coluna e fila do tabuleiro contam com uma palavra. O objetivo do mediador então é associar essas duas palavras relacionadas a sua coordenada e pensar em uma dica de uma palavra que faça com os os demais jogadores consigam marcar no turno. 

---
## Como jogar
Com o python e a biblioteca 'pygame' instalados no seu computador, compile o arquivo 'jogar.py'. Feito isso, execute o jogo.

O seguinte tabuleiro irá aparecer em sua tela: 

![image](https://user-images.githubusercontent.com/53914839/157489358-800b93c5-2f9a-4c8c-993f-4dad20decf7d.png)

- A tecla ESPAÇO avança o turno. Apertá-la faz com que uma coordenada apareça na tela.
- Cada botão do tabuleiro interage com seu mouse. Um clique nele o colore de verde, demonstrando um acerto. Dois cliques o colore de vermelho, demonstrando um erro. Três cliques o fazem voltar pro estado inicial.
- A tecla R reinicia o jogo. Novas palavras são colocadas no tabuleiro e todos os botões voltam para o estado inicial.

---
### Exemplo de turno:
Coordenada do turno: E4 - (Pão e Banana)

Dica do mediador: Comida

Caso os demais jogadorem acertem a coordenada, clique uma vez no botão associado a ela. Caso contrário, clique duas vezes no botão.
