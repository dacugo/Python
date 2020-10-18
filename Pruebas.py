"""
vals = [1,2,3]
vals[0], vals[1] = vals[1], vals[2]
print(vals)


for i in range(1):
    print("#")

else:
    print("#")


var = 0
while var<6:
    var += 1
    if var %2 == 0:
        continue
    print("#")



var = 1
while var<10:
    print("#")
    var = var<<1
    print(var)


a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c+d+e)



lst = [3,1,-2]
print(lst[lst[-1]])



vals = [0,1,2]
vals.insert (0,1)
del vals[1]
print(vals)


nums = [1,2,3]
vals = nums
del vals[1:2]
print(nums)
print(vals)

lst1 = [1,2,3]
lst2 = []
for v in lst1:
    lst2.insert(0,v)
print (lst2)



lst = [1,2,3]
for v in range (len(lst)):
    lst.insert(1,lst[v])
print (lst)

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range (3):
    s += t[i][i]
print (s)



lst = [[0,1,2,3] for i in range(2)]
print (lst[2][0])


lst = ['a','b','c','d']

dic = {'a':0,'b':1,'c':2,'d':3}

i=0

while i <= len(lst)-1:
    print(dic[lst[i]])
    i += 1


"""

def listaFacultades (info:dict)->dict:
	#Función que se encarga de crear y ordenar la lista de las facultades
	facultades = set()
	for value in info.values():
		materias = value['materias']
		i = 0
		while i <= len(materias) - 1:
			facultad = materias[i]['facultad']
			facultades.add(facultad)
			i += 1
	facultades = sorted(facultades)
	return facultades

def crearCorreo (nombres:str, apellidos:str, documento:int)->str:
	if ' ' in nombres:
		espacioNombre = nombres.index(' ')
		inicialNombre = nombres[0]+ nombres[espacioNombre + 1]
		espacioApellido = apellidos.index(' ')
		apellido = apellidos[espacioApellido + 1:len(apellidos)]	
		digitosDocumento = str(documento)[-2:]
		correo = inicialNombre + "." + apellido + digitosDocumento
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
		correo = correo.lower()
		return correo
	else:
		espacioApellido = apellidos.index(' ')
		inicialNombre = nombres[0] + apellidos[espacioApellido+1]
		apellido = apellidos[0:espacioApellido-1]	
		digitosDocumento = str(documento)[-2:]
		correo = inicialNombre + "." + apellido + digitosDocumento
		correo = correo.lower()
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
		return correo

def listaDiccionario(lista:list)->dict:
	diccionario = dict()
	for i in range(len(lista)):
		diccionario[lista[i]]=0
	return diccionario

def promedio_facultades(info: dict, contando_externos : bool = True ) -> tuple:
	
	notaCredito = dict()
	sumaCredito = dict() 

	listaCorreos = set() #ordenar alfabeticamente
	
	facultades = listaFacultades(info)#crear lista de facultades

	facultades = listaDiccionario(facultades)

	notaCredito = facultades.copy()
	sumaCredito = facultades.copy()


	if contando_externos==True:
		informacionEstudiante = info.items()
		for key,value in informacionEstudiante:
			materias = value['materias']
			if len(materias) == 0:
				continue
			
			try:
				i = 0
				while i <= len(materias) - 1:
					facultad = materias[i]['facultad']
					nota = materias[i]['nota']
					creditos = materias[i]['creditos']
					retirada = materias[i]['retirada']
					if creditos!=0 and retirada=='No':
						producto = nota * creditos
						notaCredito[facultad] = notaCredito[facultad] + producto
						sumaCredito[facultad] = sumaCredito[facultad] + creditos
						listaCorreos.add(crearCorreo(value['nombres'],value['apellidos'],value['documento']))
					i += 1
			except:
				return "Error numérico."
	else:
		informacionEstudiante = info.items()
		for key,value in informacionEstudiante:
			key = str(key)
			codigo = key [4:6] #no considerar estudiante externo, con código 05 después del año
			if codigo != '05':
				programa = value['programa'] #no tener en cuenta materias de otro programa
				materias = value['materias']
				if len(materias) == 0:
					continue
				try:
					i = 0
					while i <= len(materias) - 1:
						facultad = materias[i]['facultad']
						nota = materias[i]['nota']
						creditos = materias[i]['creditos']
						retirada = materias[i]['retirada']
						veriPrograma = str(materias[i]['codigo'])
						veriPrograma = veriPrograma[0:len(programa)]
						if creditos!=0 and retirada=='No' and veriPrograma==programa:
							producto = nota * creditos
							notaCredito[facultad] = notaCredito[facultad] + producto
							sumaCredito[facultad] = sumaCredito[facultad] + creditos						
							listaCorreos.add(crearCorreo(value['nombres'],value['apellidos'],value['documento']))
						i += 1
				except:
					return "Error numérico."
			else:
				continue
	listaCorreos = sorted(listaCorreos)

	listaTemporalFacultades = list(facultades.keys())
	i=0
	while i <= len(listaTemporalFacultades)-1:
		facultades[listaTemporalFacultades[i]]=round(notaCredito[listaTemporalFacultades[i]]/sumaCredito[listaTemporalFacultades[i]],2)
		i += 1		
	tuplaResultado = (facultades,listaCorreos)
	return tuplaResultado