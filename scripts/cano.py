import pygame
import random

class Cano:
    def __init__(self, tela):
        self.tela = tela
        self.imagem = pygame.image.load("assets/cano.png").convert_alpha()
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        self.x = tela.get_width()
        self.velocidade = 3
        self.gap = 150  # abertura entre canos
        self.resetar()

    def resetar(self):
        self.altura_base = random.randint(100, self.tela.get_height() - 100)
        # cano de baixo começa em altura_base
        self.baixo_y = self.altura_base
        # cano de cima tem sua imagem invertida e sua Y deve ser altura_base - gap - altura_da_imagem
        self.cima_y = self.altura_base - self.gap - self.altura

    def atualizar(self):
        self.x -= self.velocidade
        if self.x < -self.largura:
            self.x = self.tela.get_width()
            self.resetar()

    def desenhar(self):
        # cano invertido (cima)
        cano_invertido = pygame.transform.flip(self.imagem, False, True)
        self.tela.blit(cano_invertido, (self.x, self.cima_y))
        # cano normal (baixo)
        self.tela.blit(self.imagem, (self.x, self.baixo_y))

    def detectarColisao(self, rectJogador):
        rect_cima = pygame.Rect(self.x, self.cima_y, self.largura, self.altura)
        rect_baixo = pygame.Rect(self.x, self.baixo_y, self.largura, self.altura)
        return rectJogador.colliderect(rect_cima) or rectJogador.colliderect(rect_baixo)
