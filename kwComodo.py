import os
os.system ("cls")

print("\n\n\t Algoritmo que calcula o KW para um comodo")
largura = int(input("\nQual a largura do seu cômodo em metros: "))
comprimento = int(input("Qual o comprimento do seu cômodo em metros: "))
metro_quadrado = largura * comprimento
luz = metro_quadrado * 18 
print(f" A área do seu cômodo terá {metro_quadrado} metros quadrados e será necessário {luz} KW para iluminar esse cômodo")