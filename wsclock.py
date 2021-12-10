#Stephanie M. Ramos Camacho

#Working Set Clock Replacement Algorithm

import sys

#variable para el parametro del tamano de las paginas
number_pages = int(sys.argv[1])
# print number_pages

#tau para el tiempo
tau = sys.argv[2]

#para el parametro del file que se ponga
file = sys.argv[3]

#abre y lee el file
file = open(file, "r")
file = file.read()

#quitando el newline para eventualmente quitar el W: y el R: para poner
#solo los numeros en una lista
if "\n" in file:
	lista = file.split("\n")

if " " in file:
	lista = file.split(" ")
print (file)

# virtualPage = []
# for i in lista:
# 	x = i.split(":")
# 	virtualPage.append(int(x[1]))
# print virtualPage

clockFlecha = 0
memoria = {}
tiempo = 0
faults = 0

for pages in lista:
	temp = []
	temp = pages.split(':')

	if len(memoria) == 0:
		temp1 = 