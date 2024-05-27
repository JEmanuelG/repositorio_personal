Algoritmo presupuesto_pintor
	Escribir "Ingresa ancho de la pared:"
	Leer ancho_pared
	Escribir "Ingresa alto de la pared"
	Leer alto_pared
	Escribir "Ingresa el precio por m2"
	Leer precio_m
	
	superficie <- ancho_pared * alto_pared
	costo_pared <- precio_m * superficie
	
	Escribir "El costo para pintar la pared es: $", costo_pared
FinAlgoritmo
