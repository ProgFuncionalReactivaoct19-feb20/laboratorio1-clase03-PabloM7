"""
	Problema 2 del taller
	@pablom7
"""
#Lista de notas a sumar
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
#Uso de función anónima para sumar los elementos de la lista
suma = lambda x: x[0] + x[1] + x[2]
#Uso de list para presentar el resultado como una lista y de map para iterar la funcion en la lista notas
print(list(map(suma,notas)))