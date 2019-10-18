"""
	Problema 5 del taller
	@pablom7
"""

def filtro(x):
	black_edades = [10, 14, 30, 32, 40, 16]
	if x in black_edades:
		return False
	else:
		return True

edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
white_edades = filter(filtro, edades)
print(list(white_edades))