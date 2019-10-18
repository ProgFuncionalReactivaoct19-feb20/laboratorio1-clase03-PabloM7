"""
	Problema 4 del Taller
	@pablom7
"""
#Lista de notas a filtrar
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
#Uso de funcion anonima para filtrar los elementos deseados
filtrar = filter(lambda x: x[3]=="Regular"or x[3] == "Bueno", notas)
#Presentacion de resultados
print(list(filtrar))