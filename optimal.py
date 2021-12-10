#Stephanie M. Ramos Camacho

#Optimal Replacement Algorithm

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
hit = {}
faults = 0

#repeticiones de las paginas a 0 y lo simula una vez
for pages in virtualPage:
	hit[pages] = 0

	if pages in memoria:
		hit[pages] = hit[pages] + 1

	else:
		faults = faults + 1
		if len(memoria) < number_pages:
			memoria.append(pages)

		#tratar de predicir cual se repite y no se va a usar en un tiempo	
		else:
			minPages = min(hit.keys(), key = (lambda k: hit[k]))
			
			for este in range(0, len(memoria)):
				if memoria[este] == minPages:
					memoria[este] = pages

#la segunda vez que lo hace
memoria = []
faults = 0
for pages in virtualPage:
	if pages not in memoria:
		faults = faults + 1
		if len(memoria) < number_pages:
			memoria.append(pages)

		#se supone que se sepa cual no se va a mantener	
		else:
			minPages = min(hit.keys(), key=(lambda k: hit[k]))

			for este in range(0, len(memoria)):
				if memoria[este] == minPages:
					memoria[este] = pages

#imprime los page faults
print ("PF: %s" % (faults))




#funcion para abrir, leer el file y poner los pages en una lista
# def listaPages():
# 	with open(file, "r") as txt:
# 		#separando por espacios el file
# 		file = txt.read().replace('\n', ' ')
# 		file = txt.read().replace('W:', ' ')
# 		file = txt.read().replace('R:', ' ')
# 		file = file.split(' ')
# 		print (file)
# # 		n = 0
# 		#recorriendo el file
# 		while n < 50:
# 			#toma el primero, segundo, tercero, ect. del file
# 			letter = file[n]
# 			#toma el tercer caracter
# 			pages = letter[2]
# 			# prueba = (pages)
# 			#crea la lista y guarda ese tercer caracter
# 			lista = list()
# 			lista.append(pages)
# 			# print pages
# 			print lista
# 			n += 1
# listaPages()
# print pages