import time
import math
import numba
from numba import njit, prange
import numpy as np

n = 10000000

def monte_carlo_puro():
    dentroCircunferencia = 0

    for _ in range(n):
        x = np.random.random()
        y = np.random.random()

        if x**2 + y**2 <= 1:
            dentroCircunferencia += 1

    return 4 * dentroCircunferencia/n

@njit(parallel=True)
def monte_carlo_numba():
    dentroCircunferencia = 0

    for _ in prange(n):
        x = np.random.random()
        y = np.random.random()

        if x ** 2 + y ** 2 <= 1:
            dentroCircunferencia += 1

    return 4 * dentroCircunferencia / n

@numba.jit(parallel=True,cache=True)
def monte_carlo_numba_cache():
    dentroCircunferencia = 0

    for _ in prange(n):
        x = np.random.random()
        y = np.random.random()

        if x ** 2 + y ** 2 <= 1:
            dentroCircunferencia += 1

    return  4 * dentroCircunferencia / n

def calculos(piEstimado):
    erroAbsoluto = math.fabs(math.pi - piEstimado)
    erroPercentual = ((math.pi - piEstimado) / math.pi) * 100

    print(f"Valor n: {n}")
    print(f"π: {math.pi} \nπ Estimado: {piEstimado:.4f}")
    print(f"Erro absoluto: {erroAbsoluto:.4f}")
    print(f"Erro percentual: {erroPercentual:.4f}\n")


print("Puro")
inicio = time.time()
puro = monte_carlo_puro()
final = time.time()
print(f"Tempo: {final - inicio:.6f} s")
calculos(puro)

print("Otimizado")
monte_carlo_numba()
inicio = time.time()
numba = monte_carlo_numba()
final = time.time()
print(f"Tempo: {final - inicio:.6f} s")
calculos(numba)


print("Otimizado com Cache")
monte_carlo_numba_cache()
inicio = time.time()
cache = monte_carlo_numba_cache()
final = time.time()
print(f"Tempo: {final - inicio:.6f} s")
calculos(cache)
