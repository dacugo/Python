#arreglo de numeros
numbers = [1,2,3,4,5]
#          0,1,2,3,4
# impresión de una parte del arreglo, según posición
print(numbers[2])
#arreglo de palabras
colores = ["Verde","Morado","Amarillo"]
print(colores[1])
#Diccionario o array asociativo
person = {"name":"Marines","lastName":"Mendez","age":24}
#impresión de una parte del array asociativo
print(person.get("name"))
#recorrer un arreglo con un ciclo for
for value in colores:
    print(value)
#recorrer un arreglo con un ciclo for mostrando llaves y valores
for key, value in person.items():
    print(key," ",value)

