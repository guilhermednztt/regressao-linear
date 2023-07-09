"""
EXERCICIO PARA CRIACAO DA RETA DE REGRESSA LINEAR.

MATERIAL: USP [https://edisciplinas.usp.br/pluginfile.php/1479289/mod_resource/content/0/regr_lin.pdf], SLIDE 10
"""

import dados as dados
import numpy as np
import matplotlib.pyplot as plt


class RegressaoLinear:

    def __init__(self):
        self.dados = None

    def entradaDados(self):
        """
        Ler o arquivo que serve de base de dados.
        """
        self.dados = dados.dados

    def criarValoresRegressao(self):
        """
        Criar uma lista com par X Y para reta de regressao
        """
        reta = []

        for i in self.dados[0]:
            valorVariavelDependente = self.calcularVariavelDependente(i)
            reta.append(valorVariavelDependente)

        reta = [self.dados[0], reta]

        self.exibirRegressao(reta)

    def calcularVariavelDependente(self, variavelIndependente):
        """
        Calcular resultado da funcao afim (1º grau).\n
        variavel dependente = A + Bx
        """
        valorB = self.calcularB()
        valorA = self.calcularA(valorB)

        resultado = valorA + valorB * variavelIndependente

        return resultado

    def calcularB(self):
        """
        Descobre o valor de B. Onde B = Sxy / Sx²\n
        S = soma\n
        x = x - media(X)\n
        y = y - media(Y)
        """
        produtoXY = self.calcularVarianciaProduto()
        somaQuadradoX = self.calcularQuadrado(self.dados[0])

        B = produtoXY / somaQuadradoX

        return B

    def calcularA(self, valor):
        """
        Descobre o valor de A. Onde A = media(Y) - B*media(X).
        """
        mediaY = np.mean(self.dados[1])
        mediaX = np.mean(self.dados[0])

        A = mediaY - (valor * mediaX)

        return A

    def calcularQuadrado(self, valores):
        """
        Calcula a somatoria do quadrado dos valores (SQT - Soma Total dos Quadrados).\n
        Caso X:\n
        SQT(X) = SOMATORIA( (x - MEDIA(X))² )\n
        x = cada elemento do conjunto X\n
        X = conjunto de valores
        """
        sqt = 0
        media = np.mean(valores)

        for i in valores:
            sqt += (i - media) ** 2

        return sqt

    def calcularVarianciaProduto(self):
        """
        Calcula a somatoria do produto entre X e Y.\n
        xy = (x - media(X)) * (y - media(y))\n
        x = elemento do conjunto de valores X\n
        y = elemento do conjunto de valores Y\n
        """
        produtoxy = 0
        mediaX = np.mean(self.dados[0])
        mediaY = np.mean(self.dados[1])

        for i in range(len(self.dados[0])):
            produtoxy += (self.dados[0][i] - mediaX) * \
                (self.dados[1][i] - mediaY)

        return produtoxy

    def exibirRegressao(self, reta):
        plt.title("REGRESSAO LINEAR - Peso e Rendimento")
        plt.xlabel("PESO")
        plt.ylabel("RENDA DA CARCAÇA (KG)")

        plt.plot(reta[0], reta[1], color='red')
        plt.scatter(self.dados[0], self.dados[1])

        plt.show()


# TESTE
rl = RegressaoLinear()
rl.entradaDados()
rl.criarValoresRegressao()
