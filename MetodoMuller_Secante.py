import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x-1)*(x-3)*(x-5)*(x-7)*(x-9)

# Método da Secante

# Valores iniciais
x_0 = np.array([0.5, 2.0, 4.2, 6.5, 8.4])
del_x = 0.05
tol = 1e-6
max_iter = 100

for i in range(len(x_0)):
    Ea = 1.0
    x = x_0[i]
    erros = []   # lista para armazenar os erros
    it = 0
    
    while Ea > tol and it < max_iter:
        x_old = x
        # Fórmula da secante modificada
        x = x - (f(x) * del_x) / (f(x) - f(x - del_x))
        
        Ea = abs((x - x_old) / x)
        erros.append(Ea)
        it += 1
    
    print(f"Raiz aproximada partindo de {x_0[i]}: {x:.6f} em {it} iterações")
    
    # plotar o erro em escala log
    plt.semilogy(range(1, len(erros)+1), erros, marker='o', label=f"x0 = {x_0[i]}")

plt.xlabel("Iteração")
plt.ylabel("Erro relativo (Ea)")
plt.title("Convergência da Secante Modificada")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()
# Método de Müller

