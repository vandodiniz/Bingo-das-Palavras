# 🎲 Bingo das Palavras
## 🔎 Sobre o Projeto
### Introdução
O `Bingo das Palavras` é inspirado em um jogo de cartas. O objetivo do jogo é os jogadores cooperarem entre si e alcançarem o maior número de acertos possíveis.
A cada turno um jogador vira o mediador da partida. Este mediador então recebe uma coordenada, e precisa com apenas uma palavra, fazer com que os outros jogadores descubram qual a coordenada do turno.   

Para que isso seja possível, cada coluna e fila do tabuleiro contam com uma palavra. O objetivo do mediador então é associar essas duas palavras relacionadas a sua coordenada e pensar em uma dica de uma palavra que faça com os os demais jogadores consigam marcar no turno. 

Foi implementado de forma a ter uma forte interação com o usuário através do teclado e mouse, sendo utilizados conceitos de modularização e tendo as seguintes funcionalidades:

* Interação com o teclado para avançar os turnos
* Sensibilidade do ponteiro do mouse com o tabuleiro;
* Atualização da interface gráfica em tempo real;
* Resetar o jogo;
* Sair do jogo;

### Dataa de implementação
Março de 2022

### Responsável
Vando Carlos Diniz Reis

---
## 📚 Estrutura de Diretórios 
```
-> Bingo das Palavras
    -> app
    -> codigo
         -> button.py
         -> cfg.py
         -> controle.py
         -> funcoes.py
         -> jogar.py
    -> extras
    -> imagens
    -> .gitatribbutes
    -> README.md
```
__-> Bingo das Palavras__
- Pasta onde ficará todo o código do projeto, sendo ele dividido da seguinte forma:

  __-> app__
  - Pasta contendo o executável.
  
  __-> codigo__
  - Pasta contendo os arquivos python criados no projeto.
  
    - __button.py__
    
      Arquivo responsável por toda a lógica de botões do jogo. Nele é criado a classe ´Button´ e todos os objetos do tipo botão são instanciados. 
      
    - __cfg.py__
    
      Arquivo responsável por definir as configurações e requisitos do jogo, como tamanho da tela, fontes, imagens etc
      
    - __controle.py__
    
      Arquivo responsável por conter as principais variáveis do jogo, como o turno atual, as coordenadas e o banco de palavras.
      
    - __funcoes.py__
    
      Arquivo responsável por armazenar as diversas funções poupa tempo, como a de redesenhar o tabuleiro, reiniciar o jogo, sortear novas palavras, etc.
      
    - **jogar.py**
    
      Arquivo principal. Ele contém o looping principal do jogo e toda a lógica de interação com o mouse/teclado, além de nele ser chamado as funções existentes no ´funcoes.py´.
      
  __-> extras__
  - Pasta contendo as licenças utilizadas no jogo.
  
  __-> imagens__
  - Pasta contendo as imagens utilizadas no jogo.


---
## ❔ Como jogar
Abra o executável na pasta `app`. Caso isso não funcione, com o `Python` e a biblioteca `pygame` instalados no seu computador, compile o arquivo `jogar.py` na pasta `codigos`.

O seguinte tabuleiro irá aparecer em sua tela: 

![image](https://user-images.githubusercontent.com/53914839/157916241-616d5cea-104e-43d2-a419-3453ed507b93.png)

- A tecla ESPAÇO avança o turno. Apertá-la faz com que uma coordenada apareça na tela.
- A tecla V mostra a coordenada novamente caso o jogador tenha a pulado sem querer ou a esquecido.
- Cada botão do tabuleiro interage com seu mouse. Um clique nele o colore de verde, demonstrando um acerto. Dois cliques o colore de vermelho, demonstrando um erro. Três cliques o fazem voltar pro estado inicial.
- A tecla R reinicia o jogo. Novas palavras são colocadas no tabuleiro e todos os botões voltam para o estado inicial.

### Exemplo de turno:
Coordenada do turno: E4 - (Pão e Banana)

Dica do mediador: Comida

Caso os demais jogadorem acertem a coordenada, clique uma vez no botão associado a ela. Caso contrário, clique duas vezes no botão.

---
