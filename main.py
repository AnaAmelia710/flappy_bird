import pygame
#from scripts.jogador import Jogador
#from scripts.cano import Cano
from scripts.cenas import Partida
from scripts.cenas import Menu

pygame.init()
tamanhoTela = [600, 400]
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("FlappyBird Clone")
relogio = pygame.time.Clock()
corFundo = (86, 200, 214)
#jog = Jogador(tela, 100, 100)
#cano = Cano(tela)
listaCenas = {
    'partida':Partida(tela),
    'menu': Menu(tela)
}
cenaAtual = 'menu'
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    tela.fill(corFundo)

   # jog.atualizar()
    #jog.desenhar()
    #cano.atualizar()
    #cano.desenhar()
    cenaAtual = listaCenas[cenaAtual].atualizar()

    relogio.tick(60)
    pygame.display.flip()
    #Parei no 2.4.2 - Menu