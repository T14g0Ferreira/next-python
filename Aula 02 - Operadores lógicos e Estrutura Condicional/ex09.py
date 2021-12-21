#    ===============================================
#	    Operadores lógicos e Estrutura Condicional
#	 ===============================================
#
#	 * Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#
#      a. par ou ímpar;
#      b. positivo ou negativo;
#      c. inteiro ou decimal.
#

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
escolha = input("Escolha a operação desejada (+, -, /, *): ")

def checar():
    if (resultado // 1 == resultado):
        print("Inteiro")
    else:
      print("Decimal")
    if resultado % 2 == 0:
      print("Par")
    else:
      print("Impar")
    if resultado > 0:
      print("Positivo")
    else:
      print("Negativo")
      
if escolha == "+":
  resultado = num1 + num2
  print("Resultado: ", resultado)
  checar()
elif escolha == "-":
  resultado = num1 - num2
  print("Resultado: ", resultado)
  checar()
elif escolha == "/":
  resultado = num1 / num2
  print("Resultado: ", resultado)
  checar()
elif escolha == "*":
  resultado = num1 * num2
  print("Resultado: ", resultado)
  checar()
else:
  print("Valor inválido!")