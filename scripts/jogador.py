import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.posicao = [x, y]
        self.tamanho = [32, 32]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        # Animação
        self.contador = 0
        self.imagemAtual = 0
        self.tela = tela
        self.listaImagens = []

        # Carrega sprites do pássaro
        for i in range(3):
            imagem = pygame.image.load(f"assets/passaro-{i}.png").convert_alpha()
            imagem = pygame.transform.scale(imagem, self.tamanho)
            self.listaImagens.append(imagem)

        # Físicas
        self.velocidadeAtual = 0
        self.gravidade = 0.4
        self.velocidadeMaxima = 8

    def desenhar(self):
        # Troca de frame a cada 6 ciclos
        self.contador += 1
        if self.contador > 6:
            self.contador = 0
            self.imagemAtual = (self.imagemAtual + 1) % len(self.listaImagens)

        # Desenha sempre
        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    def atualizar(self):
        # Gravidade correta
        self.velocidadeAtual += self.gravidade

        # Limita velocidade para baixo
        if self.velocidadeAtual > self.velocidadeMaxima:
            self.velocidadeAtual = self.velocidadeMaxima

        # Atualiza posição
        self.posicao[1] += self.velocidadeAtual
        self.rect.topleft = (int(self.posicao[0]), int(self.posicao[1]))

        # Pulo
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            self.velocidadeAtual = -self.velocidadeMaxima * 0.9  # pulo suavizado

    def getRect(self):
        return self.rect
