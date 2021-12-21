#    ===============================================
#	    Operadores lógicos e Estrutura Condicional
#	 ===============================================
#
#	 * Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
#      se digitar outro valor deve aparecer valor inválido.
#

diaSemana = int(input("Digite um número: "))
if diaSemana == 1:
  print("Domingo")
elif diaSemana == 2:
  print("Segunda")
elif diaSemana == 3:
  print("Terça")
elif diaSemana == 4:
  print("Quarta")
elif diaSemana == 5:
  print("Quinta")
elif diaSemana == 6:
  print("Sexta")
elif diaSemana == 7:
  print("Sábado")
else:
  print("Valor Inválido")