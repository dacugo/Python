numeros = [ 10, 5, 7, 2, 1]

numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original.

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior.

numeros[1] = numeros[4]  # copiando el valor del quinto elemento al segundo
print("Nuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual.

###

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

###

numeros = [111, 7, 2, 1]
print(numeros[-1])
print(numeros[-2])

numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

###

numeros.append(4)

print(len(numeros))
print(numeros)

###

numeros.insert(0,222)
print(len(numeros))
print(numeros)

#

miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)


#RESUMEN SECCIÓN

miLista  = [1, 1, None, True, 'Soy una cadena', 256, 0]
print(miLista [3]) # salida: soy una cadena
print(miLista  [-1]) # salida: 0

miLista  [1] = '?'
print (miLista) # salida: [1, '?', True, 'Soy una cadena', 256, 0]

miLista.insert (0, "first")
miLista.append ("last")
print (miLista ) # salida: ['first', 1, '?', True, 'Soy una cadena', 256, 0, 'last'] 


miLista = [1, 'a', ["lista", 64, [0, 1], False]]

miLista = [1, 2, 3, 4]
del miLista[2]
print(miLista) # salida: [1, 2, 4]

del miLista  # borra toda la lista 

miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in miLista :
    print(color) 

miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(miLista)) # la salidas es 5

del miLista[2]
print (len(miLista)) # la salidas es 4 

lst = [1, 2, 3, 4, 5]
lst2 = []
agregar = 0

for number in lst:
    agregar += number
    lst2.append (agregar)

print(lst2) 

lst = []
del lst
print(lst) 

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)


miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort ()
print(lst) # salida: [1, 2, 3, 4, 5]

lst = [5, 3, 1, 2, 4]
print(lst)
    
lst.reverse()
print (lst) # salida: [4, 2, 1, 3, 5]

lst = ["D", "F", "A", "Z"]
lst.sort ()

print(lst)

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort ()

print(lst)

a = "A"
b = "B"
c = "C"
d = ""

lst = [a, b, c, d]
lst.reverse ()

print(lst)

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)

miLista = [10, 8, 6, 4, 2]
nuevLista = miLista  [:] 
print(nuevLista)

miLista = [10, 8, 6, 4, 2]
del miLista[1:3] 
print(miLista)

miLista = [0, 3, 12, 8, 2]

print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)

miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)

miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")


#RESUMEN SECCIÓN

vehiculosUno = ['carro', 'bicicleta', 'moto']
print(vehiculosUno) # salida: ['carro', 'bicicleta', 'moto']

vehiculosDos = vehiculosUno
del vehiculosUno[0] # borra 'carro'
print(vehiculosDos) # salida: ['bicicleta', 'moto']



colores = ['rojo', 'verde', 'naranja']

copiaTodosColores = colores[:] # copia la lista completa
copiaParteColores = colores[0:2] # copia parte de la lista


listaMuestra = ["A", "B", "C", "D", "E"]
nuevaLista = listaMuestra[2:-1]
print(nuevaLista) # salida: ['C', 'D']

miLista = [1, 2, 3, 4, 5]
rodajaUno = miLista [2:]
rodajaDos = miLista [:2]
rodajaTres = miLista [-2:]

print(rodajaUno) # salidas: [3, 4, 5]
print(rodajaDos) # salidas: [1, 2]
print(rodajaTres) # salidas: [4, 5]

miLista = [1, 2, 3, 4, 5]
del miLista [0:2]
print(miLista) # salida: [3, 4, 5]

del miLista[:]
print(miLista) # elimina el contenido de la lista, genera: []

miLista = ["A", "B", 1, 2]

print("A" in miLista) # salida: True
print("C" not in miLista) # salida: False
print(2 not in miLista) # salidas: False

l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[0]

print(l3)

l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2

print(l3)

l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[:]

print(l3)

l1 = ["A", "B", "C"]
l2 = l1[:]
l3 = l2[:]

del l1[0]
del l2[0]

print(l3)

miLista = [1, 2, "in", True, "ABC"]

print(1 ??? miLista) # salida True
print("A" ??? miLista) # salida True
print(3 ??? miLista) # salida True
print(False ??? miLista) # salida False