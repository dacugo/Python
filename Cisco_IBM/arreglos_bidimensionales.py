EMPTY = "-"
TORRE = "TORRE"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE

print(tablero)


temps = [[0.0 for h in range(24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#

suma = 0.0

for day in temps:
    suma += day[11]

promedio= suma / 31

print("Temperatura promedio al mediodía:", promedio)


temps = [[0.0 for h in range (24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#

mas_alta = -100.0

for day in temps:
    for temp in day:
        if temp > mas_alta:
            mas_alta = temp

print("La temperatura más alta fue:", mas_alta)



habitaciones =[[[False for r in range(20)] for f in range(15)] for t in range(3)]
habitaciones[1][9][13] = True 
habitaciones[0][4][1] = False 
vacante = 0

for numeroHabitacion in range(20):
    if not habitaciones[2][14][numeroHabitacion]:
        vacante += 1
        
print(habitaciones)


[expresión for elemento in lista if condicional]


for elemento in lista:
    if condicional:
        expresión


cubos = [num ** 3 for num in range (5)]
print(cubos) # salidas: [0, 1, 8, 27, 64]


# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(tabla)
print(tabla [0][0]) # salida: ':('
print(tabla [0][3]) # salida: ':)'


# Cubo - un arreglo tridimensional (3x3x3)

cubo = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cubo)
print(cubo [0][0][0]) # salida: ':('
print(cubo [2][2][0]) # salida: ':)'