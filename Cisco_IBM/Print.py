#La función 'print' puede aceptar casi cualquier tipo de recurso o variable y mostrarlo en pantalla
print("¡Hola, Mundo!")

#En el segundo módulo del programa se muestra su uso con un dato vacío para dar un salto de línea
print("La Witsi Witsi Araña subió su telaraña.")
print()
print("Vino la lluvia y se la llevó.")

#Sin embargo los saltos de línea se pueden realizar dentro de los parametros de la función 'print'
#Esto se realiza con el carácter de escape '\'
#esta intrucción le dice al sistema que la siguente carácter que se ingrese se lea como una instrucción
#para el caso del salto de línea se emplea '\n', n que proviene de 'newline'
print("\nLa Witsi Witsi Araña\nsubió su telaraña.\n")
print("Vino la lluvia\ny se la llevó.")

#la función print usando multiples argumentos. estos se separan por comas
print("La Witsi Witsi Arañar" , "subió" , "a su telaraña.")

#argumento de palabra clave end en la funcion print
print("Mi nombre es", "Python.", end=" ,")
print("Monty Python.")
print("")
print("Mi nombre es ", end="")
print("Monty Python.")

#argumento de palabra clave sep en la funcion print
print("\nMi", "nombre", "es", "Monty", "Python.", sep="-")

#Ejemplo de ambas pabras clave
print("\nMi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")