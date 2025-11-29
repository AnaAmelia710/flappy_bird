import pygame
from scripts.jogador import Jogador
from scripts.cano import Cano
from scripts.interfaces import Texto, Botao

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = "partida"
        self.pontosValor = 0
        self.contador = 0
        self.pontosTexto = Texto(tela, str(self.pontosValor), 10, 10, (255,255,255), 30)

    def atualizar(self):
        self.estado = "partida"
        self.jogador.atualizar()
        self.cano.atualizar()

        # Pontuação baseada em tempo (um jeito simples)
        self.contador += 1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))

        self.pontosTexto.desenhar()

        if self.cano.detectarColisao(self.jogador.getRect()):
            # reset simples e volta para menu
            self.estado = 'menu'
            self.jogador.posicao = [100, 100]
            self.jogador.velocidadeAtual = 0
            self.cano.x = self.tela.get_width()
            self.pontosValor = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))

        self.jogador.desenhar()
        self.cano.desenhar()

        return self.estado


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.estado = "menu"
        self.titulo = Texto(tela, "Flappy Bird", 100, 40, (255,255,255), 60)
        self.botao_jogar = Botao(tela, "Jogar", 200, 180, 40, (0, 180, 0), (255,255,255))

    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.botao_jogar.desenhar()

        if self.botao_jogar.get_click():
            return 'partida'

        return self.estado
