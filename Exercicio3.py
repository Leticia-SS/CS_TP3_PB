import time
import math
import numba
from numba import njit, prange
import numpy as np
import concurrent.futures
from multiprocessing import cpu_count

n = 1000000


def monte_carlo_puro():
    dentroCircunferencia = 0

    for _ in range(n):
        x = np.random.random()
        y = np.random.random()

        if x ** 2 + y ** 2 <= 1:
            dentroCircunferencia += 1

    return 4 * dentroCircunferencia / n


@numba.jit(parallel=True, cache=True)
def monte_carlo_numba_cache():
    dentroCircunferencia = 0

    for _ in prange(n):
        x = np.random.random()
        y = np.random.random()

        if x ** 2 + y ** 2 <= 1:
            dentroCircunferencia += 1

    return 4 * dentroCircunferencia / n


def monte_carlo_worker(chunk_size):
    dentroCircunferencia = 0
    for _ in range(chunk_size):
        x = np.random.random()
        y = np.random.random()
        if x ** 2 + y ** 2 <= 1:
            dentroCircunferencia += 1
    return dentroCircunferencia


def monte_carlo_parallelo():
    num_workers = cpu_count()
    chunk_size = n // num_workers
    restante = n % num_workers

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for i in range(num_workers):
            size = chunk_size + (restante if i == num_workers - 1 else 0)
            futures.append(executor.submit(monte_carlo_worker, size))

        dentroCircunferencia = 0
        for future in concurrent.futures.as_completed(futures):
            dentroCircunferencia += future.result()

    return 4 * dentroCircunferencia / n


def calculos(piEstimado):
    erroAbsoluto = math.fabs(math.pi - piEstimado)
    erroPercentual = ((math.pi - piEstimado) / math.pi) * 100

    print(f"Valor n: {n}")
    print(f"π: {math.pi} \nπ Estimado: {piEstimado:.4f}")
    print(f"Erro absoluto: {erroAbsoluto:.4f}")
    print(f"Erro percentual: {erroPercentual:.4f}\n")

if __name__ == '__main__':
    print("Puro")
    inicio = time.time()
    puro = monte_carlo_puro()
    final = time.time()
    print(f"Tempo: {final - inicio:.6f} s")
    calculos(puro)

    print("Otimizado com Cache")
    monte_carlo_numba_cache()
    inicio = time.time()
    cache = monte_carlo_numba_cache()
    final = time.time()
    print(f"Tempo: {final - inicio:.6f} s")
    calculos(cache)

    print("Concurrent.futures")
    inicio = time.time()
    parallel = monte_carlo_parallelo()
    final = time.time()
    print(f"Tempo: {final - inicio:.6f} s")
    calculos(parallel)