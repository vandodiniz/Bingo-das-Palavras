import cfg

class Button:
    def __init__(self, pos):
        self.cliques = 0
        self.pos = pos
        self.hitbox = cfg.pygame.draw.rect(cfg.tela, (0, 0, 0), (pos[0],pos[1],165,80))
    
    def trigger(self):
        self.cliques+=1
        if self.cliques > 2:
            self.cliques = 0

    def draw(self):
        if self.cliques == 0:
            cfg.pygame.draw.rect(cfg.tela, (255, 255, 255), (self.pos[0], self.pos[1],165,80))
        
        elif self.cliques == 1:
            cfg.pygame.draw.rect(cfg.tela, (0, 255, 0), (self.pos[0], self.pos[1],165,80))
            
        elif self.cliques == 2:
            cfg.pygame.draw.rect(cfg.tela, (255, 0, 0), (self.pos[0], self.pos[1],165,80))
            
        

botao1 = Button((45,120))
botao2 = Button((216,120))
botao3 = Button((387,120))
botao4 = Button((558,120))
botao5 = Button((729,120))
botao6 = Button((45,209))
botao7 = Button((216,209))
botao8 = Button((387,209))
botao9 = Button((558,209))
botao10 = Button((729,209))
botao11 = Button((45,298))
botao12 = Button((216,298))
botao13 = Button((387,298))
botao14 = Button((558,298))
botao15 = Button((729,298))
botao16 = Button((45,387))
botao17 = Button((216,387))
botao18 = Button((387,387))
botao19 = Button((558,387))
botao20 = Button((729,387))
botao21 = Button((45,476))
botao22 = Button((216,476))
botao23 = Button((387,476))
botao24 = Button((558,476))
botao25 = Button((729,476))

botoes = [botao1, botao2, botao3, botao4, botao5, botao6, botao7, botao8, botao9, botao10, botao11, botao12, botao13, botao14, botao15, botao16, botao17, botao18, botao19, botao20, botao21, botao22, botao23, botao24, botao25]
