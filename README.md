<h1 align="center">Regressão Linear</h1>
<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2103/2103601.png" width="80" height="80">
</p>

<!-- CONTEXTO -->
<p>
  <b>Contexto:</b> O algoritmo de regressão linear simples foi desenvolvido com base no material da USP. Nesse material, é explicado os cálculos para uma regressão simples para Peso corporal e Rendimento de carcaça, aos 4 meses de idade, de 10 cordeiros da raça Hampshire Down. O desenvolvimento consiste na programação dos métodos matemáticos apresentados no material.
</p>

<!-- REVISAO TEORICA -->
## 1. Revisão Matemática
Abaixo, segue as notações matemáticas obtidas:

<p>
  ✔️ <b>Soma dos Produtos:</b> Dado o conjunto de dados, temos a lista dos valores de X e Y. Foi desenvolvido a função que faz a soma do produto (resultado da multiplicação) entre os valores X e Y. Como interessa a covariância entre as duas variáveis, o cálculo foi feito da seguinte forma:<br>
  
  <b>&#8721; (x - &#772;x) * (y - &#772;y)</b> , isto é, o somatório de cada valor individual de X subtraído pela média de X, multiplicado pela somatória de cada valor de Y subtraído pela média de Y.

  ```py
  def calcularVarianciaProduto(self):
        produtoxy = 0
        mediaX = np.mean(self.dados[0])
        mediaY = np.mean(self.dados[1])

        for i in range(len(self.dados[0])):
            produtoxy += (self.dados[0][i] - mediaX) * \
                (self.dados[1][i] - mediaY)

        return produtoxy
  ```

  <br>✔️ <b>Somatória Total dos Quadrados:</b> Para verificar a variação dos valores em relação à média geral, foi aplicado nos valores de X a seguinte fórmula:<br>
  <b>&#8721; (x - &#772;x)²</b> , isso significa a somatória do quadrado de todos os valores de X subtraídos pela média de X. Por tanto:

  ```py
  def calcularQuadrado(self, valores):
        sqt = 0
        media = np.mean(valores)

        for i in valores:
            sqt += (i - media) ** 2

        return sqt
  ```

<br>✔️ <b>Coeficiente Angular de B:</b> Uma vez calculado os Produtos verificando a covariância e calculado o somatório dos quadrados, o coeficiente angular de B, que indica sua inclinação na reta, é feito pela divisão dos dois resultados:

```py
def calcularB(self):
      produtoXY = self.calcularVarianciaProduto()
      somaQuadradoX = self.calcularQuadrado(self.dados[0])

      B = produtoXY / somaQuadradoX

      return B
```

<br>✔️ <b>Coeficiente Linear (Intercepto):</b> Por fim, calcula-se o intercepto que será o valor da variável dependente (alvo):

```py
def calcularA(self, valor):
      mediaY = np.mean(self.dados[1])
      mediaX = np.mean(self.dados[0])

      A = mediaY - (valor * mediaX)

      return A
```
<br>

## 2. Resultados
No momento em que coloquei em lista os valores de X e Y usados no material em que o desenvolvimento se baseou, foi necessário chegar ao mesmo resultado. Segue:

| Material da Aula | Resultado do desenvolvimento |
| --- | --- |
| <img src="https://github.com/guilhermednztt/regressao-linear/blob/main/images/img1.png?raw=true"> | <img src="https://github.com/guilhermednztt/regressao-linear/blob/main/images/img2.png?raw=true"> | 

<br>

## 3. Referência
Conforme mencionado, o desenvolvimento foi baseado no material de matemática da USP:

<ul>
  <li><b>Regressão Linear Simples</b> - Stela Vayego<br>
  Acesso: <a href="https://edisciplinas.usp.br/pluginfile.php/1479289/mod_resource/content/0/regr_lin.pdf">link aqui</a>.</li>
</ul>

Outras instruções foram obtidas pela material de pós graduação em Inteligência Artificial e Machine Learning.

</p>

<br>

<p align="center">
  <a href="https://sol.sbc.org.br/journals/index.php/reic/article/view/2144">
    Python, Matplotlib, Regressão Linear Simples.<br>
    <b>Guilherme Donizetti - 2023</b>
  </a>
</p>
