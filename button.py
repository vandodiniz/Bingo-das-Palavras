import cfg

class Button:
    def __init__(self, pos):
        self.cliques = 0
        self.pos = pos
        self.hitbox = cfg.pygame.draw.rect(cfg.tela, (0, 0, 0), (pos[0],pos[1],165,80))

    
    def trigger(self):
        self.cliques+=1
        if self.cliques > 3:
            self.cliques = 0

botao1 = Button((45,120))
botao2 = Button((213,120))
botao3 = Button((381,120))
botao4 = Button((547,120))
botao5 = Button((712,120))
botao6 = Button((45,208))
botao7 = Button((213,209))
botao8 = Button((381,209))
botao9 = Button((547,209))
botao10 = Button((712,209))
botoes = [botao1, botao2, botao3, botao4, botao5, botao6, botao7, botao8, botao9, botao10]
