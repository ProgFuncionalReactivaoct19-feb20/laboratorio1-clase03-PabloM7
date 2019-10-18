"""
	Problema 3 del taller
	@pablom7
"""
#Funcion que evalua la lista
def filtro(y):
	excluir = ["No", "hay", "que", "lo", "que", "no", "la"]
	if y in excluir:
		return True
	else:
		return False
#Variable para almacenar la frase
frase = "No hay medicina que cure lo que no cura la felicidad"
#Usamos la funcion .split para separar la frase y la almacenamos en otra variable
separador = frase.split()
#Se usa el filter para filtrar resultados entre las dos variables
resultado = filter(filtro, separador)
#Presentacion de resultados
print(list(resultado))
