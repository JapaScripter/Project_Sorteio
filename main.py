# =====Sortear Mega-Sena=====#
import random

# Gera aleatoriamente 6 números distintos entre 1 e 60
numeros = random.sample(range(1, 61), 6)

# Exibe os números sorteados
print("Os números sorteados na Mega-Sena são: ", end="")
for numero in sorted(numeros):
	print(numero, end=" ")
print("\n")  # Pula duas linhas
# =====Sortear Mega-Sena=====#

# =====Sortear Quina=====#
import random

# Gera aleatoriamente 5 números distintos entre 1 e 80
numeros = random.sample(range(1, 81), 5)

# Exibe os números sorteados
print("Os números sorteados na Quina são: ", end="")
for numero in sorted(numeros):
	print(numero, end=" ")
print("\n")  # Pula duas linhas
# =====Sortear Quina=====#

# =====Sortear Lotofácil=====#
import random

# Gera aleatoriamente 15 números distintos entre 1 e 25
numeros = random.sample(range(1, 26), 15)

# Exibe os números sorteados
print("Os números sorteados na Lotofácil são: ", end="")
for numero in sorted(numeros):
	print(numero, end=" ")
print("\n")  # Pula duas linhas
# =====Sortear Lotofácil=====#

# =====Sortear Lotomania=====#
import random

# Gera aleatoriamente 50 números distintos entre 0 e 99
numeros = random.sample(range(0, 100), 50)

# Exibe os números sorteados
print("Os números sorteados na Lotomania são: ", end="")
for numero in sorted(numeros):
	print(numero, end=" ")
print("\n")  # Pula duas linhas
# =====Sortear Lotomania=====#