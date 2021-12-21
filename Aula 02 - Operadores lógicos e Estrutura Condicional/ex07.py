#    ===============================================
#	    Operadores lógicos e Estrutura Condicional
#	 ===============================================
#
#	 *  Construa uma pequena chave dicotômica para identificar uma determinada planta como membro de um dos 
#       principais grupos: Bryophyta, Pteridophyta, Gymnospermae ou Angiospermae. A identificação se dá com base na presença (1) ou ausência (0)
#       de três caracteres: vascularização, sementes e flores. Utilize a tabela abaixo como referência.
#
#              Grupo 	    Vascularização 	 Sementes 	 Flores
#           ====================================================
#            Bryophyta 	        0 	            0 	        0
#            Pteridophyta 	    1 	            0 	        0
#            Gymnospermae 	    1 	            1 	        0
#            Angiospermae 	    1 	            1 	        1
#

"""Lógica 01"""
vasc = 1
sem = 1
flor = 0

if flor:
  tipo = "Angiospermae"
else:
  if sem:
    tipo = "Gymnospermae"
  else:
    tipo = "Pteridophyta" if vasc else "Bryophyta"

print(tipo)

"""Lógica 2"""
# vasc = 1
# sem = 1
# flor = 1

# if vasc == 0 and sem == 0 and flor == 0:
#   print("Pertence ao grupo Bryophyta.")
# elif vasc == 1 and sem == 0 and flor == 0:
#   print("Pertence ao grupo Pteridophyta.")
# elif vasc == 1 and sem == 1 and flor == 0:
#   print("Pertence ao grupo Gymnospermae.")
# elif vasc == 1 and sem == 1 and flor == 1:
#   print("Pertence ao grupo Angiospermae.")
# else:
#   print("Não pertece a nenhum dos grupos.")