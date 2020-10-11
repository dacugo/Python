distancias={('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27, ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117, ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199, ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19, ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31, ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}
ruta_inicial=['H', 'B', 'E', 'A', 'C', 'D', 'H']

#validar distancias iguales
validacion_iguales=distancias.keys()
contadorA = 0

for puntoA in validacion_iguales:
    for puntoB in validacion_iguales:
    indice=(puntoA,puntoB)
    if puntoA==puntoB and distancias(indice) != 0:
        contadorA

#extraer valores del diccionario 'distancias'
validacion_informacion=distancias.values()
contadorB = 0
#verificar si se puede continuar con los datos ingresados
for valor in validacion_informacion:
    if valor < 0:
        contador += 1
        
if contadorA > 0 or contadorB > 0:
    validar_ruta = False
else:
    validar_ruta = True
#si todos los datos son mayores o iguales a 0 se valida la información
if validar_ruta==True:
    i = 0
    while i <= len(ruta_inicial) - 1:
        puntoA = ruta_inicial[i]
        puntoB = ruta_inicial[i+1]
        indice = (puntoA,puntoB)
        print(indice)

        i += 1

        if (i == len(ruta_inicial)-1):
            i = len(ruta_inicial)+1
else:
    print("Por favor revisar los datos de entrada.")