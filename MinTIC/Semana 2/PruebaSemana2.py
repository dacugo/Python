def parqueadero_buses(cantidad_buses,numero_bus):
    p = cantidad_buses % 3 == 0
    q = numero_bus <= cantidad_buses and numero_bus > 0
    if p and q:
        if numero_bus <= cantidad_buses/3:
            resultado = 1
        else:
            if numero_bus <= cantidad_buses*2/3:
                resultado = 2
            else:
                resultado = 3
    else:
        resultado=-1
    return resultado

print(parqueadero_buses(100,1))
print(parqueadero_buses(99,-3))
print(parqueadero_buses(102,40))
print(parqueadero_buses(30,40))
print(parqueadero_buses(100,1))