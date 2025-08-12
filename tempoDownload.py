import os
os.system ("cls")

print("\n\n\tAlgoritmo que calcula o tempo de download do arquivo")
tamanho = int(input("\nInforme o tamanho do arquivo em Bits: "))
velocidade = float(input("Informe a velocidade do download em Bits/s: "))
tempo = tamanho / velocidade
print(f"O tempo de download do seu arquivo é {tempo:.2f} Bits/s")