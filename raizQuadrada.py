import math
import os
os.system ("cls")

print("\n\n\tCálculo da Raiz quadrada que recebe um número positivo")
numero = float(input("\nColoque o número: "))
quadrado = numero ** 2
raiz = math.sqrt(numero)
print(f"O {numero} ao quadrado é igual a {quadrado:.0f} e o valor da raiz vai ser {raiz:.0f}")