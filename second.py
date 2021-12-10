#Stephanie M. Ramos Camacho

#Second Chance Algorithm

import sys

#variable para el parametro del tamano de las paginas
number_pages = int(sys.argv[1])
# print (number_pages)

#para el parametro del file que se ponga
file = sys.argv[2]

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

virtualPage = []
for i in lista:
	x = i.split(":")
	virtualPage.append(int(x[1]))
print (virtualPage)

memoria = []
bit = {}
faults = 0

#inicializando Rbit a las paginas
for pages in virtualPage:
	bit[pages] = 1
	rbit = bit[pages]

	if pages in memoria:
		if rbit == 0:
			rbit = 1

		else:
			x = memoria.index(pages)
			t = memoria.pop(x)
			memoria.append(t)
			rbit = 0

	#para las que no estan en memoria
	else:
		faults = faults + 1
		if len(memoria) < number_pages:
			memoria.append(pages)
		else:
			memoria.pop(0)
			memoria.append(pages)

#imprime los page faults
print ("PF: %s" % (faults))
