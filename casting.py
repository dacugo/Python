print("Ingresa el primer valor")
num1 = float (input())
print("Ingresa el segundo valor")
num2 = float (input())

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

#probando casting, cambiar de str(string) a int(entero) y viceversa
print("El resultado es: " + str(suma))
#repitiendo cadena de caracteres
print("Repetir" * int(suma))
print(multiplicacion)
print(division)