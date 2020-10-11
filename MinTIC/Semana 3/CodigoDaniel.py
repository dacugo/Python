distancias={('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27, ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117, ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199, ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19, ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31, ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}
ruta_inicial=['H', 'B', 'E', 'A', 'C', 'D', 'H']

def distanciarecorrida(distancias:dict,ruta:list)->int:
    numerovisitas=len(ruta)
    contadordistancia=0
    for i in range(0,numerovisitas-1):
        contadordistancia=contadordistancia+distancias[(ruta[i],ruta[i+1])]
    return contadordistancia

def ruteo(distancias:dict,ruta_inicial:list)->dict:
    convertir_dict=distancias.items()
    for key,value in convertir_dict:
        if key[0]==key[1] and value != 0:
            return "Por favor revisar los datos de entrada."
        if value<0:
            return "Por favor revisar los datos de entrada."

    ruta=ruta_inicial.copy()
    numerovisitas=len(ruta)
    distancia=distanciarecorrida(distancias,ruta_inicial)
    distanciacalculada=distancia-1
    listarutasprovisional=[]

    while distanciacalculada<distancia:
        distancia=distanciacalculada
        for i in range(1,numerovisitas-2):
            for j in range (i+1,numerovisitas-1):
                rutaintercambio=ruta.copy()
                a=ruta[i]
                b=ruta[j]
                rutaintercambio[i]=b
                rutaintercambio[j]=a
                listarutasprovisional.append(rutaintercambio)
        distanciasp=[]
        for i in range (0,len(listarutasprovisional)):
            distanciasp.append(distanciarecorrida(distancias,listarutasprovisional[i]))
        
        distanciacalculada=min(distanciasp)
        rutacalculada=listarutasprovisional[distanciasp.index(min(distanciasp))].copy()
    
    juntar='-'.join(ruta)
    mi_diccionario={'ruta':juntar, 'distancia':distanciacalculada}
    return mi_diccionario

print(ruteo(distancias,ruta_inicial))