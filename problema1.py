"""
	Problema 1 del taller
	@pablom7
"""
#Arreglo que contiene los promedios de los estudiantes
promedios = [10, 20, 18, 19, 20, 17, 18, 16, 16, 11, 12, 13]
#Se usa filter para obtener los resultados mayores a 16.5
resultado = filter(lambda x: x >= 16.5, promedios)
#Se presentan los resultados como un arreglo
print(list(resultado))