#    ===============================================
#	    Operadores lógicos e Estrutura Condicional
#	 ===============================================
#
#	 * Crie um programa para um circo, no qual dada a idade de uma pessoa, seja indicado o valor do ingresso segundo as regras:
#
#       a) A entrada para qualquer pessoa com menos de 4 anos ou maior que 60 é gratuita;
#       b) a entrada para qualquer pessoa com idade entre 4 e 18 custa 20 reais;
#       c) a entrada para qualquer pessoa com 18 ou mais custa 30 reais;
#       d) estudantes e professores pagam meia-entrada.
#

idade = int(input("Digite a sua idade: "))

if idade < 4 or idade > 60:
  print("A entrada é gratuita")
else:
  classe = input("Você é professor ou estudante (Sim/Não)? ")
  classe = classe.upper()

if idade >= 4 and idade < 18:
  if classe == "SIM":
    print("A entrada é R$10,00")
  else:
    print("A entrada é R$20,00")
elif idade >= 18 and idade < 60:
  if classe == "SIM":
    print("A entrada é R$15,00")
  else:
    print("A entrada é R$30,00")