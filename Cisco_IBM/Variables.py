#ejemplos de nombres correctos pero no convenientes
#MiVariable, i, t34, Tasa_Cambio, contador, DiasParaNavidad, ElNombreEsTanLargoQueSeCometeranErroresConEl, _.

#ejemplos de nombres incorrectos
#10t (no comienza con una letra), Tasa Cambio (contiene un espacio)

#las palabras clave o reservadas no pueden ser usadas como nombre de variables, algunos ejemplos
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#creación de variable e imprimiendola
var = 1
print(var)

var = 1
balance_cuenta = 1000.0
nombreCliente = 'John Doe'
print(var, balance_cuenta, nombreCliente)
print(var)

var = "3.7.1"
print("Versión de Python: " + var)

#asignar un nuevo valor a una variable existente
var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

#problemas matematicos simples, hipotenusa
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#operadores abreviados
x = x * 2
x *= 2
oveja = oveja + 1
oveja+= 1

#Ejercicio  "pasando de kilometros a millas"
kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

#ejercicio de función
# codifica aquí tus datos de prueba.
x = float(0)
y=(3*x**3)-(2*x**2)+(3*x)-1
# escribe tu código aquí.
print("y =", y)

"""
Esto es
un comentario
en varias líneas

"""
