def crear_tablero(Filas,Columnas):
	tablero = []
	for i in range(Filas):
		fila = []
		for j in range(Columnas):
			fila.append("*")
		tablero.append(fila)
	return tablero
def mostrar_tablero(tablero):
	print()
	for i in range(len(tablero)):
		for j in range(len(tablero[i])):
			print(tablero[i][j], end=" ")
		print()

	print()
	for i in range(len(tablero[0])):
		print(i,end=' ')
	print()
def check_columna(tablero,i,j):
	return j+3 < len(tablero[0]) and tablero[i][j] == tablero[i][j+1] == tablero[i][j+2] == tablero[i][j+3] != "*"

def check_fila(tablero,i,j):
	return i+3 < len(tablero) and tablero[i][j] == tablero[i+1][j] == tablero[i+2][j] == tablero[i+3][j] != "*"

def es_ganador(tablero):
	#busco 4 fichas iguales en sentido vertical y horizontal
	#recorro filas
	for i in range(len(tablero)):
		#recorro columnas
		for j in range(len(tablero[0])):
			if(check_columna(tablero,i,j)):
				return True
			if(check_fila(tablero,i,j)):
				return True

	#si llegue aqui es porque no habian 4 conectados
	return False
def fin_juego(tablero):
	#reviso si quedan movimientos disponibles
	#recorro filas
	for i in range(len(tablero)):
		#recorro columnas
		for j in range(len(tablero[0])):
			if(tablero[i][j] == "*"):
				return False
	return True

def jugar(player1,player2):
	#se crea el tablero
	Filas = 6
	Columnas = 7
	tablero = crear_tablero(Filas,Columnas)
	
	x = player1[0]
	o = player2[0]
	turno = x

	while(True):
		mostrar_tablero(tablero)
		pos = int(input("Juega " + turno + " (elija numero de columna): "))
		if(pos <= Columnas):

			#agrego jugada
			for i in range(Filas):
				if(tablero[Filas-1-i][pos] == "*"):
					tablero[Filas-1-i][pos] = turno
					break

			#verifico si turno ganó
			if(es_ganador(tablero)):
				print("\nGanó",turno)
				break

			#verifico si es empate
			if(fin_juego(tablero)):
				print("\nEmpate!")
				break

			#Cambio de turno
			if(turno == x): turno = o
			else: turno = x
		elif(pos > Columnas):
			print("es un valor entre 0 y 6")
	mostrar_tablero(tablero)
	
print("Bienvenidos a conecta 4")
player1 = input("Jugador 1 ingrese nombre")
player2 = input("Jugador 2 ingrese nombre")
jugar(player1,player2)