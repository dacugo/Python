"""
diccionario = {"total":55}
print(diccionario)
otrodiccionario={"copia":123.23}
print(otrodiccionario)
"""
def usodeDiccionarios()->dict:
    diccionario2={}
    otrodiccionario={"100":123.23}

#ejemplo del diccionario con la palabra reservada 'dict'
diccionario = dict (total=55, descuento=True, subtotal=15)
print(diccionario)

#diccionarios con espacios diseñados para varios valores
usuario = {
    'nombre':'Nombre del usuario',
    'edad':23,
    'curso':'Curso de Python',
    'skills':{
        'programacion':True,
        'base_de_datos':False
    },
    'No medallas':10
}
print(usuario)
print()
print(usuario['curso'])
print(usuario['skills'])
print(usuario['skills']['base_de_datos'])

diccionario = dict()
print(diccionario)

diccionario['marca']='Mazda'