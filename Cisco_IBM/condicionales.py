"""
if contadordeOvejas >= 120: #evalúa una expresión de prueba.
    dormirSoñar() #se ejecuta si la expresión de prueba es Verdadera.

if condición_true_or_false:
    ejecuta_si_condición_true
 else: 
    ejecuta_si_condición_false

#declaraciones anidadas
if climaEsBueno:
    if encontramosBuenRestaurante:
        almorzar()
    else:
        comerSandwich() 
else:
    if hayBoletosDisponibles:
        irAlCine()
    else:
        irDeCompras()  
#declarión el_if
if climaBueno:
    iraCaminar()
elif hayBoletosDisponibles:
    IralCine()
elif mesasLibres:
    almorzar()
else:
    jugarAjedrezEnCasa()
"""
"""
#lee dos números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado
print("El número más grande es:", nmasGrande)
"""


#lee tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)

#RESUMEN MODULO
#declaración if
x = 10

if x == 10: # condición
    print("x es igual a 10") # ejecutado si la condición es verdadera

x = 10

if x > 5: # condición uno
    print("x es mayor que 5") # ejecutado si la condición uno es verdadera

if x <10: # condición dos
    print("x es menor que 10") # ejecutado si la condición dos es verdadera

if x == 10: # condición tres
     print("x es igual a 10") # ejecutado si la condición tres es verdadera

#Ejemplo if - else

x = 10

if x < 10: # condición
    print ("x es menor que 10") # ejecutado si la condición es Verdadera

else:
    print ("x es mayor o igual a 10") # ejecutado si la condición es False

#serie de if
x = 10

if x > 5: # Verdadero
    print("x > 5")

if x > 8: # Verdadero
    print("x > 8")

if x > 10: # Falso
    print("x > 10")

else:
    print("Se ejecutará el else")

#Declaración if, elif, else

 x = 10

if  x == 10: # Verdadero
    print("x == 10")

if x > 15: # Falso
    print("x > 15")

elif x > 10: # Falso
    print("x > 10")

elif x > 5: # Verdadero
    print("x > 5")

else:
    print("No se ejecutará el else")

#Declaraciones anidadas
x = 10

if x > 5: # Verdadero
    if x == 6: # Falso
        print("anidado: x == 6")
    elif x == 10: # Verdadero
        print("anidado: x == 10")
    else:
        print("anidado: else")
else:
    print("else")

#EJERCICIOS
#ejercicio 1
x = 5
y = 10
z = 8

print(x > y)
print(y > z)

#ejercicio 2
x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x) 

#ejercicio 3
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x) 

#ejercicio 4
x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

#ejercicio 5
x = "1"

if x == 1:
    print("uno")
elif x == "1":
    if int (x)> 1:
        print("dos")
    elif int (x) < 1:
        print("tres")
    else:
        print("cuatro")
if int (x) == 1:
    print("cinco")
else:
    print("seis") 

#ejercicio 6
x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")
if y == int (z):
    print("dos")
elif x == y:
    print("tres")
else:
    print("cuatro")
