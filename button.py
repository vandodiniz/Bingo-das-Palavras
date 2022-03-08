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
botao11 = Button((46,296))
botao12 = Button((214,296))
botao13 = Button((382,296))
botao14 = Button((548,296))
botao15 = Button((713,296))
botao16 = Button((46,384))
botao17 = Button((214,384))
botao18 = Button((382,384))
botao19 = Button((548,384))
botao20 = Button((713,384))
botao21 = Button((46,472))
botao22 = Button((214,472))
botao23 = Button((382,472))
botao24 = Button((548,472))
botao25 = Button((713,472))

botoes = [botao1, botao2, botao3, botao4, botao5, botao6, botao7, botao8, botao9, botao10, botao11, botao12, botao13, botao14, botao15, botao16, botao17, botao18, botao19, botao20, botao21, botao22, botao23, botao24, botao25]
