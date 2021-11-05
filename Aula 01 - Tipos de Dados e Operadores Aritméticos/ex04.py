#    ===========================================
#	   Tipos de Dados e Operadores Aritméticos
#	 ===========================================
#
#	 * Faça um Programa que peça as 4 notas bimestrais e mostre a média.
#


nota1 = float(input('Nota do 1º bimestre: '))
nota2 = float(input('Nota do 2º bimestre: '))
nota3 = float(input('Nota do 3º bimestre: '))
nota4 = float(input('Nota do 4º bimestre: '))

notafinal = (nota1+nota2+nota3+nota4)/4
print(f'A sua média foi: {notafinal}')
