import os
os.system ("cls")

print("\n\n\tAlgoritmo que recebe o ano de nascimento e o ano atual e calcula a idade atual e a idade em 2030")
nascimento = int(input("\nInforme o seu ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))
idade_atual = ano_atual - nascimento
idade_futura = 2030 -nascimento
print(f"A sua idade atual é {idade_atual} anos, e em 2030 você vai ter {idade_futura} anos")