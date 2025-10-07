import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x-1)*(x-3)*(x-5)*(x-7)*(x-9)

# Método de Muller 

# Valores iniciais
x_0 = np.array([0.5, 2.0, 4.2, 6.5, 8.4])
del_x = 0.05
tol = 1e-6
max_iter = 100

for i in range(len(x_0)):
    # três pontos iniciais
    x0 = x_0[i]
    x1 = x0 + 0.05
    x2 = x1 + 0.05
    
    Ea = 1.0
    it = 0
    erros = []

    while Ea > tol and it < max_iter:
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0)) / h0
        d1 = (f(x2) - f(x1)) / h1

        a = (d1 - d0) / (h1 + h0)
        b = a*h1 + d1
        c = f(x2)

        rad = np.sqrt(b**2 - 4*a*c)

        # evita cancelamento numérico
        if abs(b + rad) > abs(b - rad):
            den = b + rad
        else:
            den = b - rad

        dx_r = -2*c / den
        x3 = x2 + dx_r

        Ea = abs(dx_r/x3)
        erros.append(Ea)

        # avança os pontos
        x0, x1, x2 = x1, x2, x3
        it += 1

    print(f"Raiz aproximada partindo de {x_0[i]}: {x3:.6f} em {it} iterações")

 # plot do erro em escala log
    plt.semilogy(range(1, len(erros)+1), erros, marker='o', label=f"x0 = {x_0[i]}")

plt.xlabel("Iteração")
plt.ylabel("Erro relativo (Ea)")
plt.title("Convergência do Método de Müller")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()