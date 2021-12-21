#    ===============================================
#	    Operadores lógicos e Estrutura Condicional
#	 ===============================================
#
#	 * Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
#     a. Álcool:
#    até 20 litros, desconto de 3% por litro
#    acima de 20 litros, desconto de 5% por litro
#
#     b. Gasolina:
#    até 20 litros, desconto de 4% por litro
#    acima de 20 litros, desconto de 6% por litro
#
#   Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#   calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é 2.50 o preço do litro do álcool é 1,90.
#

qtdLitros = float(input("Quantos litros foi abastecido: "))
tipoCombustivel = input("Qual o tipo de combustível (A / G)? ")
precoA = 1.90
precoG = 2.50

if tipoCombustivel.upper() == "A":
  if qtdLitros <= 20:
    precoA = precoA - (precoA * 0.03)
    print(f"O valor pago será R${precoA * qtdLitros}")
  else:
    precoA = precoA - (precoA * 0.05)
    print(f"O valor pago será R${precoA * qtdLitros}")
if tipoCombustivel.upper() == "G":
  if qtdLitros <= 20:
    precoG = precoG - (precoG * 0.04)
    print(f"O valor pago será R${precoG * qtdLitros}")
  else:
    precoG = precoG - (precoG * 0.06)
    print(f"O valor pago será R${precoG * qtdLitros}")