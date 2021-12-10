#Stephanie M. Ramos Camacho

#Working Set Clock Replacement Algorithm

import sys
from types import SimpleNamespace

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

	#para saber si la memoria esta vacia
	if len(memoria) ==0:
		xtemp = SimpleNamespace(r = 1, m = 0, t = tiempo, v = temp[1])
		memoria[clockFlecha] = (xtemp.r, xtemp.m, xtemp.t, xtemp.v)

		#incrementando
		clockFlecha = (clockFlecha + 1) %number_pages
		faults = faults + 1
		tiempo = tiempo + 1

	#para cuando no este llena la memoria o vacia
	elif len(memoria) < number_pages:
		guardadas = []

		for index in range(0, len(memoria)):
			guardadas.append(memoria[index][3])

		#no esta en memoria
		if temp[1] not in guardadas:
			#la agrega al final
			clockFlecha = len(memoria)

			if temp[0] == 'W':
				xtemp = SimpleNamespace (r = 1, m = 1, t = tiempo, v = temp[1])
			else:
				xtemp = SimpleNamespace (r = 1, m = 0, t = tiempo, v = temp[1])

			memoria[clockFlecha] = (xtemp.r, xtemp.m, xtemp.t, xtemp.v)

			#incrementando
			clockFlecha = (clockFlecha + 1) % number_pages
			faults = faults + 1
			tiempo = tiempo + 1

		#ya esta en memoria
		else:
			for key in memoria:
			# 	# print (key)
				# if memoria[key[3]] == temp[1]:
					key1 = key
					break

			#Rbit 1
			if memoria[key1][0]:
				temp_r = (memoria[key1][0] + 1) % 2
				temp_m = memoria[key1][1]
				temp_t = tiempo
				temp_v = memoria[key1][3]
				xtemp = SimpleNamespace(r = temp_r, m = temp_m, t = temp_t, v = temp_v)
				memoria[key1] = (xtemp.r, xtemp.m, xtemp.t, xtemp.v)

				#incrementando
				tiempo = tiempo + 1
				clockFlecha = (key1 + 1) % number_pages

			#Rbit 0
			else:
				age = tiempo - memoria[key1][2]

				if age > int(tau):
					#cuando se cambia a 1
					if memoria[key1][1]:
						temp_r = memoria[key1][0]
						temp_m = (memoria[key1][1] + 1) % 2
						temp_t = tiempo
						temp_v = memoria[key1][3]
						xtemp = SimpleNamespace(r = temp_r, m = temp_m, t = temp_t, v = temp_v)
						memoria[key1] = (xtemp.r,xtemp.r,xtemp.t,xtemp.v)

				#cuando cambia a 0 y cambia el valor de la pagina
				else:
					if temp[0] == 'W':
						xtemp = SimpleNamespace(r = 1, m = 1, t = tiempo, v = temp[1])
					else:
						xtemp = SimpleNamespace(r = 1, m = 0, t = tiempo, v = temp[1])

				memoria[key1] = (xtemp.r, xtemp.m, xtemp.t, xtemp.v)

				#incrementando
				clockFlecha = (key1 + 1) % number_pages
				tiempo = tiempo + 1
	#memoria llena
	else:
		guardadas = []

		for index in range(0, len(memoria)):
			guardadas.append(memoria[index][3])

		#no esta en memoria
		if temp[1] not in guardadas:
			for key in memoria:
			#si ambos son 0
				if not memoria[key][0] and not memoria[key][1]:
					clockFlecha = key
					break

			if temp[0] == 'W':
				xtemp = SimpleNamespace(r = 1, m = 1, t = tiempo, v = temp[1])
			else:
				xtemp = SimpleNamespace(r = 1, m = 0, t = tiempo, v = temp[1])
			
			memoria[clockFlecha] = (xtemp.r, xtemp.m, xtemp.t, xtemp.v)

			#incrementando
			clockFlecha = (clockFlecha + 1) % number_pages
			faults = faults + 1
			tiempo = tiempo + 1

		#ya en memoria
		else:
			for key in  memoria:
				if memoria[key][3] == temp[1]:
					key1 = key
					break

			#Rbit 1
			if memoria[key1][0]:
				temp_r = (memoria[key1][0] + 1) % 2
				temp_m = memoria[key1][1]
				temp_t = tiempo
				temp_v = memoria[key1][3]
				xtemp = SimpleNamespace(r = temp_r, m = temp_m, t = temp_t, v = temp_v)
				memoria[key1] = (xtemp.r, xtemp.m, xtemp.t, xtemp.v)

				#incrementando
				tiempo = tiempo + 1
				clockFlecha = (key1 + 1) % number_pages

			#Rbit 0
			else:
				age = tiempo - memoria[key1][2]

				if age > int(tau):
					#si se modifica a 1
					if memoria[key1][1]:
						temp_r = memoria[key1][0]
						temp_m = (memoria[key1][1] + 1) % 2
						temp_t = tiempo
						temp_v = memoria[key1][3]
						xtemp = SimpleNamespace(r = temp_r, m = temp_m, t = temp_t, v = temp_v)
						memoria[key1] = (xtemp.r, xtemp.m, xtemp.t, xtemp.v)

				#si se modifica a 0, cambia el valor de la pagina
				else:
					if temp[0] == 'W':
						xtemp = SimpleNamespace(r = 1, m = 1, t = tiempo, v = temp[1])
					else:
						xtemp = SimpleNamespace(r = 1, m = 0, t = tiempo, v = temp[1])

				memoria[key1] = (xtemp.r, xtemp.m, xtemp.t, xtemp.v)

				#incrementando
				clockFlecha = (key1 + 1) % number_pages
				tiempo = tiempo + 1

#imprimiendo los page faults
print ("PF: %s" % (faults))






