import os
os.system ("cls")

print("\n\n\tAlgoritmo que calcula o novo salário considerando um percentual de aumento")
salario = float(input("\nInforme o seu salário: "))
percentual = float(input("Informe o percentual do aumento: "))
aumento = salario + percentual/100
novo_salario = aumento + salario
print(f"O seu novo salário é {novo_salario:.2f}")