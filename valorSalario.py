import os
os.system ("cls")

print("\n\n\tCálculo salárial")
horas_trabalhadas = int(input("\nInforme o número de horas trabalhadas: "))
salario_minimo = float(input("Informe o valor do salário mínimo: R$"))
valor_hora = salario_minimo / 2
bruto = horas_trabalhadas * valor_hora
imposto = bruto * 3/100
receber = bruto - imposto
print(f"O valor do seu salário é R${receber:.2f}")