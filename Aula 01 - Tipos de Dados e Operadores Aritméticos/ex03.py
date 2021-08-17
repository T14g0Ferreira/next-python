#    ===========================================
#	   Tipos de Dados e Operadores Aritméticos
#	 ===========================================
#
#	 * Faça um Programa que peça dois números e imprima a soma.
#    

import math
numero1 = float(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

resultado = numero1 + numero2

print("A soma dos valores é: " + str(resultado))
print("A soma dos valores é: %i"  %(resultado))
print(f"A soma dos valores é: {resultado}")
print(resultado)