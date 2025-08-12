import os
os.system("cls")

print("\n\n\tAlgoritmo que calcula o quanto restará do seu salário após pagar duas contas com uma multa de 2% sobre cada conta")

salario = float(input("\nInforme o seu salário: "))
conta1 = float(input("Informe o valor da sua primeira conta: "))
conta2 = float(input("Informe o valor da sua segunda conta: "))
multa1 = conta1 * 2/100
multa2 = conta2 * 2/100
print(f" Os valores da sua multas serão: R${multa1} e R${multa2}")
nova_conta1 = conta1 + multa1
nova_conta2 = conta2 + multa2
print(f"Os valores da sua nova conta considerando esse aumento de 2% em cada uma serão: R${nova_conta1} e R${nova_conta2}")
resto_do_salario = salario - (nova_conta1 + nova_conta2)
print(f" O que restará do seu salário após pagar as suas contas será um valor de: R$ {resto_do_salario}")