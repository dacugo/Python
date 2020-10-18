"""
items = info.items()

for key, value in items:

    nombre = value['nombres']
    print(nombre)
"""

#nombres y correo

if ' ' in name:
    DosNombres = True
else:
    DosNombres = False


espacio = name.index(' ')
correo = name[0]+ name[espacio + 1]

#quitar tildes

for letra in correo:
    if 'á'==letra:
        correo = correo.replace('á','a')
    elif 'é'==letra:
        correo = correo.replace('é','e')
    elif 'í'==letra:
        correo = correo.replace('í','i')
    elif 'ó'==letra:
        correo = correo.replace('ó','o')
    elif 'ú'==letra:
        correo = correo.replace('ú','u')
    elif 'ñ'==letra:
        correo = correo.replace('ñ','n')

for letra in correo:
    if 'á'==letra or 'é'==letra or 'í'==letra or 'ó'==letra or 'ú'==letra or 'ñ'==letra:
        correo = correo.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ñ','n')
