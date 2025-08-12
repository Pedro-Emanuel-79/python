import os
os.system ("cls")

print("\n\n\tAlgoritmo que calcula o segundos em minutos")
segundos = int(input("\nInforme os segundos: "))
minutos = segundos // 60
seg = segundos % 60
print(f"Você transformou {segundos} segundos em {minutos} minutos e {seg} segundos")