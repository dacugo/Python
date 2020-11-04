"""
def suma(a,b):
    suma = a + b
    print (suma)

a=int(input('ingrese primer valor '))
b=int(input('ingrese segundo valor '))

resultado = suma(a,b)

print (resultado)


diccionario = {}

cantidadPersonas = int(input('ingrese la cantidad de personas a registrar: '))

i = 0

while i < cantidadPersonas:
    documento = int(input('ingrese el documento de la persona: '))
    nombre = input('ingrese el nombre de la persona: ')
    diccionario[documento] = nombre
    i += 1

print (diccionario)

consulta = int(input('ingrese el documento de la consulta: '))
print(diccionario[consulta])


def numeroMayor(listNumeros):
    listNumeros.sort(reverse=True)
    print(listNumeros[0])
    
    
def ingresarNumeros():
    listNumeros = []
    for i in range (0,3):
        numero = int(input('ingrese un numero: '))
        listNumeros.append(numero)
    return numeroMayor(listNumeros)

print(ingresarNumeros())
"""
menu = """
class Presentacion:

    def __init__(self):"""

print(menu)
        












