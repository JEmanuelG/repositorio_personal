Algoritmo puntos_equipo
	Escribir "Ingresa cant partidos perdidos:"
	Leer partidos_perdidos
	Escribir "Ingresa cant partidos empatados:"
	Leer partidos_empatados
	Escribir "Ingresa cant partidos ganados:"
	Leer partidos_ganados
	
	puntos <- 0
	
	Si partidos_empatados > 0 Entonces
		puntos = puntos + partidos_empatados
	Fin Si
	
	Si partidos_ganados > 0 Entonces
		puntos = puntos + (partidos_ganados * 3)
	Fin Si
	
	Escribir "La cantidad de puntos que sumo tu equipo en el campeonato: ", puntos
FinAlgoritmo
