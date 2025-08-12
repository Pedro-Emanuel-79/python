import math
import os
os.system ("cls")

print("\n\n\tCálculo da Hipotebusa")
cateto_1 = float(input("\nInforme o valor do primeiro cateto: "))
cateto_2 = float(input("Informe o valor do segundo cateto: "))
hipotenusa = math.sqrt(cateto_1 ** 2 + cateto_2 ** 2)
print(f"O valor da Hipotenusa é {hipotenusa:.3f}")