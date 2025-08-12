import os
os.system ("cls")

print("\n\n\t Algoritmo que calcula que vai ser o consumo médio de um automóvel")
km = float(input("\nQuantos km você percorreu: "))
litros = float(input("Quantos litros o carro consumiu: "))
consumo = km/litros
print(f"O consumo médio foi {consumo:.2f} KM/L")