# Method Müller vs Secant

Nesse programa, é avaliado a eficiência para encontrar as raízes da função do método de Muller versus o método da Secante. 
A função é definida como:

$$
f(x) = (x - 1)(x - 3)(x - 5)(x - 7)(x - 9)
$$

Logo, para isso, as raízes esperadas para ambos os códigos tornam-se o conjunto [1, 3, 5, 7, 9].

Dessa forma, será considerado para ambos os métodos uma estimativa do ponto da raiz por meio de um delta de 0,05 para o método da **Secante**.  

Enquanto isso, para o **método de Müller** será considerado:

$$
x_1 = x_0 + \delta x
$$

$$
x_2 = x_1 + \delta x = x_0 + 2\delta x
$$

Assim, ao avaliar as raízes usando ambos os métodos existe um comparativo do erro avaliado por tempo, conforme:

### Resultados do Método da Secante

<p align="center">
  <img src="https://github.com/arthurhsalgado/M-ller-vs-Secant/raw/main/ResultadosSecantes.png" alt="Resultados da Secante" />
</p>

### Resultados do Método de Müller

<p align="center">
  <img src="https://github.com/arthurhsalgado/M-ller-vs-Secant/raw/main/ResultadosMuller.png" alt="Resultados de Müller" />
</p>
