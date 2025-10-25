import random
import time
import math

n = 10000000

inicio = time.time()
dentroCircunferencia = 0

for _ in range(n):
    x = random.random()
    y = random.random()

    if x**2 + y**2 <= 1:
        dentroCircunferencia += 1

piEstimado = 4 * dentroCircunferencia/n
final = time.time()
erroAbsoluto = math.fabs(math.pi - piEstimado)

print(f"π: {math.pi} \nπ~: {piEstimado:.4f} \nTempo: {final-inicio:.6f} s")
print(f"Erro absoluto: {erroAbsoluto:.4f}")