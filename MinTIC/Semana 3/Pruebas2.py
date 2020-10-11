
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


def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    #validar información ingresada
    contadorValidacion = 0

    for i in range (0,len(ruta_inicial)-1):
        puntoA = ruta_inicial[i]
        for j in range (0,len(ruta_inicial)-1):
            puntoB = ruta_inicial[j]
            indice=(puntoA,puntoB)
            if (puntoA==puntoB and distancias[indice]!=0) or distancias[indice]<0:
                contadorValidacion += 1

    ruta_final = ruta_inicial.copy()
    salida={}
    ruta_provisional=[]
    
    if contadorValidacion==0:
        while ruta_final!=ruta_provisional:
            for i in range (1,len(ruta_final)-1):
                for j in range (i,len(ruta_final)-1):
                    for k in range(j+1,len(ruta_final)-1):
                        distancia1 = calcularDistanciaRuta(distancias, ruta_final)
                        ruta_provisional=ruta_final.copy()
                        temp1 = ruta_provisional[k]
                        temp2 = ruta_provisional[j]
                        ruta_provisional[k] = temp2
                        ruta_provisional[j] = temp1               
                        distancia2 = calcularDistanciaRuta(distancias, ruta_provisional)
                        if distancia2 < distancia1:
                            ruta_final=ruta_provisional.copy()
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