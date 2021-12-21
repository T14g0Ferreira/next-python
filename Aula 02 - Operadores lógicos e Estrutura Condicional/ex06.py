#    ===============================================
#	    Operadores lógicos e Estrutura Condicional
#	 ===============================================
#
#	 * Complete o código na célula abaixo para imprimir uma mensagem informando se um aluno foi aprovado ou reprovado 
#      em uma disciplina com base em sua nota final. A nota mínima necessária para aprovação é 5 .
#

nota = float(input("Informe a nota do aluno: "))

if nota >= 5 and nota <= 10:
  print("O aluno foi aprovado!")
elif nota < 0 or nota > 10:
  print("Insira uma nota válida!")
else:
  print("O aluno foi reprovado!")