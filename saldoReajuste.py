import os
os.system ("cls")

print("\n\n\tAlgoritmo que leia o saldo e cria um novo saldo considerando um reajuste de 15%")
saldo = float(input("\nInforme o seu saldo: "))
novo_saldo = saldo + saldo * 15/100
print(f"O seu novo saldo com o reajuste de 15% é {novo_saldo:.2f}")