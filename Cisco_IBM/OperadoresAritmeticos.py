#exponenciación
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#multiplicación

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#división, este operador siempre arroja como resultado un número flotante
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#división entera, en este caso, si la división no contiene parte decimal, el resultado es de tipo entero
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

#operador de residuo o módulo
print(12 % 4.5)

#operador suma
print(-4 + 4)
print(-4. + 8)

#operador resta
print(-4 - 4)
print(4. - 8)
print(-1.1)

#cuando se combinan los operadores, estos se ejecutan de manera jerarquica
#en el caso de operadores con la misma jerarquia el programa se ejecuta de izquierda a derecha,o visceversa
#dependiendo de hacia donde se encuentre enlazado
#enlazado a la izquierda
print(9 % 6 % 2)
#enlazado a la derecha
print(2 ** 2 ** 3)

#para evitar errores es mejor hacer uso de los parentesis, estos definen el orden de la ejecución
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)