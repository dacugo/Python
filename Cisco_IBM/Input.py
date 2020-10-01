#ejemplo de la función input (entrada de datos)
print("Dime algo...")
algo = input()
print("Mmm...", algo, "...¿en serio?")

#no se puede usar directamente con números
"""
cualquierNumero = input("Inserta un número: ")
algo = cualquierNumero ** 2.0
print(cualquierNumero, "al cuadrado es", algo)
"""

#se debe realizar una conversión de datos o casting
algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)

#otro ejemplo con números
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)

#concatenación de cadenas (string)
nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")

#multiplicación de cadenas (se repiten), en el siguiente ejemplo se hace un rectangulo
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#tambien se puede hacer un casting para transformar el formato número (int, float) en cadena (string)
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))