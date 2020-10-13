#aerolinea con mayor numero de vuelos en el listado de vuelos
vuelosEjemplo = [{"aerolinea": "AVIANCA", 'codigo': "AHF21", "origen": "BOG", "destino": "CTG", "distancia": 295, "retraso": 5, "duracion": 120, "salida":600},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "BOG", "destino": "CTG", "distancia": 295, "retraso": 2, "duracion": 115, "salida":555},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF21", "origen": "CTG", "destino": "BOG", "distancia": 295, "retraso": 15, "duracion": 120, "salida":830},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "CTG", "destino": "PEI", "distancia": 325, "retraso": 5, "duracion": 135, "salida":800},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF23", "origen": "BOG", "destino": "CLO", "distancia": 255, "retraso": 25, "duracion": 170, "salida":605},
                 {"aerolinea": "VIVAAIR", 'codigo': "VVE01", "origen": "PEI", "destino": "BOG", "distancia": 220, "retraso": 5, "duracion": 60, "salida":1030},
                 {"aerolinea": "AVIANCA", 'codigo': "AHF23", "origen": "CLO", "destino": "CTG", "distancia": 400, "retraso": 20, "duracion": 160, "salida":1200}]

#crear diccionarios a partir de conjuntos
aeropuertos = set()

for vuelo in vuelosEjemplo:
    aeropuertos.add(vuelo["origen"])
    aeropuertos.add(vuelo["destino"])

#alistar los espacios de memoria para llenar con valores
miDiccionario = {}
for aeropuerto in aeropuertos:
    miDiccionario[aeropuerto]=[0,0]

#realizar la acumulación de las duraciones de los vuelos
for aeropuerto in aeropuertos:
    for vuelo in vuelosEjemplo:
        if aeropuerto == vuelo["origen"] or aeropuerto == vuelo["destino"]:
            miDiccionario[aeropuerto][0] = miDiccionario[aeropuerto][0] + int(vuelo["duracion"])
            miDiccionario[aeropuerto][1] = miDiccionario[aeropuerto][1] + 1

#calcular el promedio
miDiccionarioSalida = {}
for aeropuerto in aeropuertos:
    miDiccionarioSalida[aeropuerto]=miDiccionario[aeropuerto][0]/miDiccionario[aeropuerto][1]

print(miDiccionarioSalida)