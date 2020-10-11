
distancias={('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27, ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117, ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199, ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19, ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31, ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}
ruta_inicial=['H', 'B', 'E', 'A', 'C', 'D', 'H']

def calcularDistanciaRuta (distancias,ruta_final):
    distanciafinal=0
    for i in range (0,len(ruta_final)-1):
        puntoA = ruta_final[i]
        puntoB = ruta_final[i+1]
        indice=(puntoA,puntoB)
        distanciafinal = distanciafinal + distancias[indice]
    return distanciafinal

def validarDatosEntrada(distancias,ruta_inicial)->bool:
    contadorValidacion = 0
    for i in range (0,len(ruta_inicial)-1):
        puntoA = ruta_inicial[i]
        for j in range (0,len(ruta_inicial)-1):
            puntoB = ruta_inicial[j]
            indice=(puntoA,puntoB)
            if (puntoA==puntoB and distancias[indice]!=0) or distancias[indice]<0:
                contadorValidacion += 1
    if contadorValidacion > 0:
        return False
    else:
        return True

def ruteo(distancias: dict, ruta_inicial: list)-> dict:

    validacionDatos = validarDatosEntrada(distancias, ruta_inicial)

    ruta_final = ruta_inicial.copy()
    
    distanciaInicial = calcularDistanciaRuta(distancias,ruta_final)
    distanciaProvisional = distanciaInicial - 1
    
    salida={}
    posibleRutas=[]
    

    if validacionDatos==True:
        while distanciaProvisional<distanciaInicial:
            distanciaInicial = distanciaProvisional
            for i in range (1,len(ruta_final)-2):
                for j in range (i+1,len(ruta_final)-1):
                    ruta_provisional=ruta_final.copy()
                    temp1 = ruta_provisional[i]
                    temp2 = ruta_provisional[j]
                    ruta_provisional[i] = temp2
                    ruta_provisional[j] = temp1               
                    posibleRutas.append(ruta_provisional)                 
            distanciaRutas=[]
            for i in range (0,len(posibleRutas)):
                distanciaRutas.append(calcularDistanciaRuta(distancias,posibleRutas[i]))
            distanciaProvisional=min(distanciaRutas)
            ruta_provisional=posibleRutas[distanciaRutas.index(distanciaProvisional)].copy()
            ruta_final = ruta_provisional.copy()
            ruta=''
            for i in range (0,len(ruta_final)):
                if i==(len(ruta_final)-1):
                    ruta += ruta_final[i]
                else:
                    ruta += ruta_final[i]+"-"
            salida={'ruta':ruta,'distancia':calcularDistanciaRuta(distancias,ruta_final)}
        return salida
            
    else:
        return "Por favor revisar los datos de entrada."
    return salida

print(ruteo(distancias,ruta_inicial))


print(ruteo({('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241, ('A', 'H'):
127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41, ('B', 'H'): 153, ('B', 'A'): 252, ('B',
'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C',
'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194,
('D', 'F'): 109, ('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119, ('F', 'H'):
267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0},['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']))

#{'ruta': 'H-A-F-B-D-C-E-H', 'distancia': 458}