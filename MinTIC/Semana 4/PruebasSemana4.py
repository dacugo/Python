def reemplazar(palabra:str)->str:
    palabra1=palabra
    palabra2=palabra1.replace("á","a")
    palabra3=palabra2.replace("é","e")
    palabra4=palabra3.replace("í","i")
    palabra5=palabra4.replace("ó","o")
    palabra6=palabra5.replace("ú","u")
    palabra7=palabra6.replace(",","")
    palabra8=palabra7.replace("ñ","n")
    return palabra8        
########################################################################

def correos(info:dict,posicion:int)->list:
    llaves=list(info.keys())  
    Nombre=info[llaves[posicion]]['nombres']
    CantidadNombres=len(Nombre.split())
    correo=[]
    if CantidadNombres==2:  
        correo.append(Nombre[0].lower())
        correo.append(Nombre[Nombre.index(' ')+1].lower())
        correo.append('.')
        Apellidos=info[llaves[posicion]]['apellidos'].split()
        Apellido1=Apellidos[1].lower()
        correo.append(reemplazar(Apellido1))  
    else:
         correo.append(Nombre[0].lower())
         Apellidos=info[llaves[posicion]]['apellidos'].split()
         Apellido1=Apellidos[1].lower()
         correo.append(Apellido1[0])
         correo.append('.')
         apellido2=Apellidos[0].lower()
         correo.append(reemplazar(apellido2))
    cadena=str(info[llaves[posicion]]['documento'])
    correo.append(cadena[-2:])  
                      
    return ''.join(correo)
##########################################################################

def promedio_facultades(info:dict,contando_externos:bool = True)->tuple:
    llaves=list(info.keys())
    totalestudiantes=len(llaves)
    facultades=set()
    for i in range(totalestudiantes):
        materiasestudiante=len(info[llaves[i]]["materias"])
        for j in range(materiasestudiante):
            facultades.add(info[llaves[i]]["materias"][j]["facultad"])
            
    facultades=list(facultades)
    facultades1=sorted(facultades)
    numfacultades=len(facultades)
        
    CorreoEstudiantes=list()
    Promediosf=dict()
    Promediosf=dict.fromkeys(facultades1)

    for i in range(numfacultades):
        notasporcredito=0
        sumacreditos=0
        Promediosf[facultades1[i]]=[notasporcredito,sumacreditos]
    
    if contando_externos:
		for i in range(totalestudiantes):
			contactar=False     # Bandera para contactar
			materiasestudiante=len(info[llaves[i]]["materias"]) # Número de materias del estudiante
			for j in range(materiasestudiante):
				Retirada=info[llaves[i]]["materias"][j]["retirada"]
				NumCre=info[llaves[i]]["materias"][j]["creditos"]
				Facultad=info[llaves[i]]["materias"][j]["facultad"]
				if Retirada == 'No' and NumCre != 0 :
					try:
						contactar = True
						nota=info[llaves[i]]["materias"][j]["nota"]
						Promediosf[Facultad][0]=nota*NumCre+Promediosf[Facultad][0]
						Promediosf[Facultad][1]=NumCre+Promediosf[Facultad][1]
					except:
						return "Error numérico."
			if contactar == True:
				CorreoEstudiantes.append(correos(info,i))
        	#except:
            	#return "Error numérico."
    else:
        #try:
		for i in range(totalestudiantes):
			codigo=str(llaves[i])
			vacacional=codigo[4:6]
			Programa=info[llaves[i]]["programa"]  # Str del programa
			longitudcodigoprograma=len(Programa)
			if vacacional !='05':
				contactar=False     # Bandera para contactar
				materiasestudiante=len(info[llaves[i]]["materias"]) # Número de materias del estudiante
				for j in range(materiasestudiante):
					CodigoMateria=info[llaves[i]]["materias"][j]["codigo"]
					CodMateria=CodigoMateria[0:longitudcodigoprograma]
					if Programa==CodMateria:
						Retirada=info[llaves[i]]["materias"][j]["retirada"]
						NumCre=info[llaves[i]]["materias"][j]["creditos"]
						Facultad=info[llaves[i]]["materias"][j]["facultad"]
						try:
							if Retirada == 'No' and NumCre != 0 :
								contactar = True
								nota=info[llaves[i]]["materias"][j]["nota"]
								Promediosf[Facultad][0]=nota*NumCre+Promediosf[Facultad][0]
								Promediosf[Facultad][1]=NumCre+Promediosf[Facultad][1]
						except:
							return "Error numérico."
				if contactar == True:
					CorreoEstudiantes.append(correos(info,i))
        #except :
            #return "Error numérico."
    PromediosFinal= Promediosf.copy()
    for i in facultades1:
        PromediosFinal[i]=round(Promediosf[i][0]/ Promediosf[i][1],2)
    CorreoEstudiantes=sorted(CorreoEstudiantes)
    return((PromediosFinal,CorreoEstudiantes))


print(promedio_facultades({
					20170136837:{
								"nombres" : "Jorge Juan",
								"apellidos" : "Moreno, López",
								"documento" : 88481595,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-8218",
												"nota" : 4.49,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 2.97,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-5048",
												"nota" : 4.26,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20130225137:{
								"nombres" : "Sara Carolina",
								"apellidos" : "Gómez, Fernández",
								"documento" : 58770043,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7738",
												"nota" : 3.36,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-9115",
												"nota" : 2.62,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7698",
												"nota" : 1.59,
												"creditos" : 4,
												"retirada" : "Si",
												},
											]
								},
					20110274333:{
								"nombres" : "Carolina Paula",
								"apellidos" : "Ochoa, López",
								"documento" : 82364435,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7972",
												"nota" : 3.15,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20200116062:{
								"nombres" : "Sara Camila",
								"apellidos" : "Martínez, Gómez",
								"documento" : 40079000,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9331",
												"nota" : 4.0,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-3530",
												"nota" : 3.4,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-8548",
												"nota" : 3.1,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9771",
												"nota" : 3.91,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20100379147:{
								"nombres" : "Jorge Juan",
								"apellidos" : "Romero, López",
								"documento" : 39344921,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9511",
												"nota" : 2.38,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-6043",
												"nota" : 3.71,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1720",
												"nota" : 2.5,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20200126220:{
								"nombres" : "Sofia",
								"apellidos" : "Cordoba, Romero",
								"documento" : 90333325,
								"programa" : "IQUI",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4982",
												"nota" : 4.57,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4982",
												"nota" : 2.8,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-6947",
												"nota" : 2.47,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-2248",
												"nota" : 3.43,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20130271126:{
								"nombres" : "Gabriela",
								"apellidos" : "Alvarez, García",
								"documento" : 72857337,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-4963",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 3.9,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-1221",
												"nota" : 4.37,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20160219974:{
								"nombres" : "Daniela Sara",
								"apellidos" : "Cuellar, Guitiérrez",
								"documento" : 80398132,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-3557",
												"nota" : 3.91,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-5158",
												"nota" : 3.83,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7543",
												"nota" : 3.41,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190264705:{
								"nombres" : "Julio Nicolas",
								"apellidos" : "Fernández, Ramírez",
								"documento" : 42697671,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-7888",
												"nota" : 4.68,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20150222512:{
								"nombres" : "Mateo Gabriel",
								"apellidos" : "Niño, Romero",
								"documento" : 12964051,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-3683",
												"nota" : 3.6,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4014",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-1670",
												"nota" : 4.75,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					}))

# ({'Arquitectura': 3.81, 'Diseño': 3.58, 'Ingenieria': 3.63, 'Medicina': 3.08}, ['cp.lopez35', 'ds.guitierrez32', 'gg.alvarez37', 'jj.lopez21', 'jj.lopez95', 'jn.ramirez71', 'mg.romero51', 'sc.fernandez43', 'sc.gomez00', 'sr.cordoba25'])

# Prueba 2:
print(promedio_facultades({
					20170116008:{
								"nombres" : "Sofia Natalia",
								"apellidos" : "Martinez, Alvarez",
								"documento" : 86056697,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-3145",
												"nota" : 3.79,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-1882",
												"nota" : 3.02,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-4916",
												"nota" : 3.99,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-9576",
												"nota" : 3.2,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-7401",
												"nota" : 4.08,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20180181912:{
								"nombres" : "Julian Andres",
								"apellidos" : "Fernández, Gómez",
								"documento" : 38203099,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-4822",
												"nota" : 3.99,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-6559",
												"nota" : 3.09,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20170131506:{
								"nombres" : "Laura Camila",
								"apellidos" : "Cuellar, Pérez",
								"documento" : 15755411,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-7857",
												"nota" : 3.19,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1857",
												"nota" : 2.62,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1415",
												"nota" : 2.83,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1720",
												"nota" : 2.58,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20100240601:{
								"nombres" : "Andres Julian",
								"apellidos" : "Ochoa, Romero",
								"documento" : 81959788,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-7472",
												"nota" : 3.6,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-5465",
												"nota" : 2.58,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8357",
												"nota" : 4.69,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-9511",
												"nota" : 2.51,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3379",
												"nota" : 4.31,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20160386484:{
								"nombres" : "Julio",
								"apellidos" : "Sánchez, Fernández",
								"documento" : 95423746,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3008",
												"nota" : 2.83,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3008",
												"nota" : 2.53,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2620",
												"nota" : 4.06,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20190365550:{
								"nombres" : "Catalina Valentina",
								"apellidos" : "García, López",
								"documento" : 88933669,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5278",
												"nota" : 3.45,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-1857",
												"nota" : 4.56,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9835",
												"nota" : 3.93,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9442",
												"nota" : 4.46,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20150173830:{
								"nombres" : "Catalina Valentina",
								"apellidos" : "Fernández, Guitiérrez",
								"documento" : 36216549,
								"programa" : "DISE",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-3520",
												"nota" : 2.71,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5596",
												"nota" : 4.7,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6981",
												"nota" : 2.79,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5596",
												"nota" : 2.51,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-5161",
												"nota" : 2.36,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20100383099:{
								"nombres" : "Juan Pablo",
								"apellidos" : "Moreno, Cordoba",
								"documento" : 17911136,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-9115",
												"nota" : 4.18,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-6074",
												"nota" : 3.73,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20090198116:{
								"nombres" : "Sofia Gabriela",
								"apellidos" : "Diaz, Moreno",
								"documento" : 62587112,
								"programa" : "ICIV",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-1157",
												"nota" : 2.45,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-7915",
												"nota" : 4.17,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-5962",
												"nota" : 4.49,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190262931:{
								"nombres" : "Paula Natalia",
								"apellidos" : "Torres, Jiménez",
								"documento" : 18534577,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2081",
												"nota" : 4.43,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-8458",
												"nota" : 4.77,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-1258",
												"nota" : 3.15,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190299456:{
								"nombres" : "Natalia Paula",
								"apellidos" : "Moreno, Alvarez",
								"documento" : 89771722,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7322",
												"nota" : 4.27,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-5808",
												"nota" : 3.19,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4470",
												"nota" : 2.26,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7972",
												"nota" : 3.66,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20150172603:{
								"nombres" : "Catalina Paula",
								"apellidos" : "Pérez, Diaz",
								"documento" : 59641117,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8636",
												"nota" : 4.65,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-1999",
												"nota" : 2.52,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3063",
												"nota" : 2.95,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20160197253:{
								"nombres" : "Julian Mateo",
								"apellidos" : "Jiménez, Fernández",
								"documento" : 41016120,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9348",
												"nota" : 4.55,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9306",
												"nota" : 2.77,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-1836",
												"nota" : 3.66,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20160174103:{
								"nombres" : "Mateo Julio",
								"apellidos" : "Diaz, López",
								"documento" : 88132707,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-2104",
												"nota" : 4.55,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-3425",
												"nota" : 3.98,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4686",
												"nota" : 4.97,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-9455",
												"nota" : 2.43,
												"creditos" : 0,
												"retirada" : "Si",
												},
											]
								},
					20150384070:{
								"nombres" : "Carolina Natalia",
								"apellidos" : "López, Gómez",
								"documento" : 33424549,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7322",
												"nota" : 2.49,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-4101",
												"nota" : 3.14,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-8021",
												"nota" : 2.97,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7470",
												"nota" : 4.77,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					}, False ))
"""
# Expected return:
# ({'Arquitectura': 3.84, 'Diseño': 3.37, 'Historia del Arte': 3.66, 'Ingenieria': 3.88, 'Medicina': 3.45}, ['aj.romero88', 'cn.gomez49', 'cp.diaz17', 'cv.guitierrez49', 'cv.lopez69', 'jf.sanchez46', 'jm.fernandez20', 'jp.cordoba36', 'lc.perez11', 'mj.lopez07', 'np.alvarez22', 'pn.jimenez77', 'sg.moreno12', 'sn.alvarez97'])
"""
#Prueba 5:
print(promedio_facultades({
					20180234491:{
								"nombres" : "Julio Juan",
								"apellidos" : "López, Cuellar",
								"documento" : 89783030,
								"programa" : "ICIV",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-2983",
												"nota" : 3.65,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-4627",
												"nota" : 3.34,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-6267",
												"nota" : 3.29,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-7182",
												"nota" : 2.83,
												"creditos" : 2,
												"retirada" : "Si",
												},
											]
								},
					20180111599:{
								"nombres" : "Camilo Julián",
								"apellidos" : "Cuellar, Sánchez",
								"documento" : 25501871,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-1258",
												"nota" : 3.77,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-4066",
												"nota" : 2.76,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-5285",
												"nota" : 3.74,
												"creditos" : 0,
												"retirada" : "Si",
												},
											]
								},
					20130111233:{
								"nombres" : "Camilo Jorge",
								"apellidos" : "Pérez, Díaz",
								"documento" : 68407479,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-7278",
												"nota" : 2.48,
												"creditos" : 1,
												"retirada" : "Si",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-2625",
												"nota" : 3.52,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-2553",
												"nota" : 2.24,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9490",
												"nota" : 4.64,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180270894:{
								"nombres" : "Camila",
								"apellidos" : "Guitiérrez, Pardo",
								"documento" : 88027774,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-1626",
												"nota" : 3.99,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-4277",
												"nota" : 4.29,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-2430",
												"nota" : 2.77,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180221472:{
								"nombres" : "Nicolas Oscar",
								"apellidos" : "Niño, Ramírez",
								"documento" : 83313299,
								"programa" : "ISIS",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6515",
												"nota" : 2.34,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-3961",
												"nota" : 3.19,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20170229508:{
								"nombres" : "Daniel Nicolas",
								"apellidos" : "Guitiérrez, Álvarez",
								"documento" : 50548066,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-6043",
												"nota" : 3.25,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-1173",
												"nota" : 3.66,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-2252",
												"nota" : 2.63,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-8962",
												"nota" : 2.37,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-9838",
												"nota" : 2.43,
												"creditos" : 2,
												"retirada" : "Si",
												},
											]
								},
					20190373561:{
								"nombres" : "Julio Camilo",
								"apellidos" : "Romero, Sánchez",
								"documento" : 89277860,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-1882",
												"nota" : 3.1,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-9435",
												"nota" : 2.47,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-7355",
												"nota" : 2.57,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-8141",
												"nota" : 2.47,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20200234229:{
								"nombres" : "Mateo Daniel",
								"apellidos" : "Gómez, Díaz",
								"documento" : 92448136,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-8238",
												"nota" : 2.34,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-9958",
												"nota" : 1.68,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-7355",
												"nota" : 2.15,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-1882",
												"nota" : 2.88,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190184788:{
								"nombres" : "Julián Camilo",
								"apellidos" : "Torres, Sánchez",
								"documento" : 28707171,
								"programa" : "ICIV",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-6894",
												"nota" : 4.56,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-2619",
												"nota" : 2.96,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-8615",
												"nota" : 2.76,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20170269592:{
								"nombres" : "Oscar Jorge",
								"apellidos" : "Ramírez, Córdoba",
								"documento" : 51020471,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-4916",
												"nota" : 2.51,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-3145",
												"nota" : 3.72,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-1882",
												"nota" : 4.96,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-7667",
												"nota" : 1.79,
												"creditos" : 2,
												"retirada" : "Si",
												},
											]
								},
					20080261436:{
								"nombres" : "Sara Camila",
								"apellidos" : "Jiménez, Suárez",
								"documento" : 10308626,
								"programa" : "IQUI",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-3859",
												"nota" : 4.14,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-3745",
												"nota" : 2.81,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20200272073:{
								"nombres" : "Laura Daniela",
								"apellidos" : "Jiménez, Hernández",
								"documento" : 24876698,
								"programa" : "ISIS",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-2276",
												"nota" : 2.98,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-6328",
												"nota" : 2.48,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-5465",
												"nota" : 2.79,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-8238",
												"nota" : 3.79,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180197073:{
								"nombres" : "Pablo Juan",
								"apellidos" : "García, Díaz",
								"documento" : 97713967,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-7837",
												"nota" : 2.44,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-2013",
												"nota" : 2.56,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-5036",
												"nota" : 4.04,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20200137719:{
								"nombres" : "Paula Gabriela",
								"apellidos" : "Jiménez, Gómez",
								"documento" : 67419825,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-9271",
												"nota" : 3.17,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-4773",
												"nota" : 4.33,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-1670",
												"nota" : 4.26,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-6433",
												"nota" : 3.61,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20170181765:{
								"nombres" : "Juan Jorge",
								"apellidos" : "Hernández, Ochoa",
								"documento" : 53243230,
								"programa" : "ISIS",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-3961",
												"nota" : 4.0,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-6565",
												"nota" : 4.35,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20150366721:{
								"nombres" : "Gabriel Andres",
								"apellidos" : "Díaz, Jiménez",
								"documento" : 73184770,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9442",
												"nota" : 2.82,
												"creditos" : 0,
												"retirada" : "Si",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-2593",
												"nota" : 3.28,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9348",
												"nota" : 2.3,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5889",
												"nota" : 3.83,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20150332990:{
								"nombres" : "Gabriela Maria",
								"apellidos" : "Ramírez, García",
								"documento" : 63768613,
								"programa" : "ICIV",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-4689",
												"nota" : 3.34,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-6673",
												"nota" : 2.73,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-2747",
												"nota" : 2.45,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20150157579:{
								"nombres" : "Juan Andres",
								"apellidos" : "Sánchez, López",
								"documento" : 57433656,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-7771",
												"nota" : 3.05,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-7732",
												"nota" : 4.55,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-4275",
												"nota" : 4.58,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-8291",
												"nota" : 4.4,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20180112245:{
								"nombres" : "Camilo Daniel",
								"apellidos" : "García, Díaz",
								"documento" : 56019795,
								"programa" : "ISIS",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-3843",
												"nota" : 3.9,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-8189",
												"nota" : 4.14,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-1419",
												"nota" : 3.57,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20100133656:{
								"nombres" : "Camila Laura",
								"apellidos" : "Ramírez, Sánchez",
								"documento" : 18406646,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2433",
												"nota" : 2.86,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-3640",
												"nota" : 3.44,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-5327",
												"nota" : 3.64,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20180168437:{
								"nombres" : "Sofia Sara",
								"apellidos" : "García, Ochoa",
								"documento" : 33993048,
								"programa" : "ARQU",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-4664",
												"nota" : 4.59,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-2113",
												"nota" : 4.89,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-9271",
												"nota" : 2.0,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-4773",
												"nota" : 2.39,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20190267075:{
								"nombres" : "Jorge Camilo",
								"apellidos" : "Martínez, Guitiérrez",
								"documento" : 16066073,
								"programa" : "DIGR",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-1584",
												"nota" : 4.34,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-2531",
												"nota" : 4.5,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-4810",
												"nota" : 1.52,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-2432",
												"nota" : 3.39,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20180275287:{
								"nombres" : "Catalina Carolina",
								"apellidos" : "Guitiérrez, Moreno",
								"documento" : 93402879,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-2169",
												"nota" : 3.06,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5889",
												"nota" : 2.97,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5278",
												"nota" : 4.64,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-7278",
												"nota" : 1.76,
												"creditos" : 1,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-7665",
												"nota" : 4.16,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180121110:{
								"nombres" : "Gabriela Sara",
								"apellidos" : "Torres, Torres",
								"documento" : 38538468,
								"programa" : "DISE",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-4446",
												"nota" : 4.67,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-7393",
												"nota" : 4.23,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-1276",
												"nota" : 3.51,
												"creditos" : 3,
												"retirada" : "Si",
												},
											]
								},
					20190292733:{
								"nombres" : "Gabriel Nicolas",
								"apellidos" : "Pérez, Martínez",
								"documento" : 95898448,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-5194",
												"nota" : 2.79,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7589",
												"nota" : 4.03,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-8218",
												"nota" : 4.49,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-5405",
												"nota" : 4.34,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20180157756:{
								"nombres" : "Daniela Paula",
								"apellidos" : "Cuellar, Moreno",
								"documento" : 73658922,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4554",
												"nota" : 2.96,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4554",
												"nota" : 4.94,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-7698",
												"nota" : 3.33,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8942",
												"nota" : 3.8,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-1968",
												"nota" : 3.12,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20200284956:{
								"nombres" : "Andrea Sofia",
								"apellidos" : "Gómez, Moreno",
								"documento" : 24588765,
								"programa" : "HAMO",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-8141",
												"nota" : 4.45,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-9576",
												"nota" : 3.47,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-3502",
												"nota" : 1.61,
												"creditos" : 3,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-6328",
												"nota" : 4.93,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20180276186:{
								"nombres" : "Gabriel Julio",
								"apellidos" : "Romero, Álvarez",
								"documento" : 53452997,
								"programa" : "ISIS",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-1419",
												"nota" : 3.59,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-4601",
												"nota" : 2.66,
												"creditos" : 4,
												"retirada" : "Si",
												},
											]
								},
					20130117729:{
								"nombres" : "Camilo Juan",
								"apellidos" : "Pardo, Niño",
								"documento" : 51804513,
								"programa" : "IIND",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-9484",
												"nota" : 4.5,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IIND-9484",
												"nota" : 3.19,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-7278",
												"nota" : 3.8,
												"creditos" : 1,
												"retirada" : "No",
												},
											]
								},
					20170191084:{
								"nombres" : "Nicolas Gabriel",
								"apellidos" : "Niño, Martínez",
								"documento" : 17307732,
								"programa" : "DIMD",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-5431",
												"nota" : 3.87,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7666",
												"nota" : 3.49,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-7666",
												"nota" : 2.48,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-2837",
												"nota" : 4.96,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20150296881:{
								"nombres" : "Gabriela",
								"apellidos" : "Fernández, Ochoa",
								"documento" : 19409088,
								"programa" : "ISIS",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-2485",
												"nota" : 3.04,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-9950",
												"nota" : 4.28,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-7601",
												"nota" : 4.21,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-8189",
												"nota" : 2.45,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20090184597:{
								"nombres" : "Sofia Catalina",
								"apellidos" : "García, Martínez",
								"documento" : 35888833,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-2593",
												"nota" : 3.82,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-4627",
												"nota" : 3.6,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20140224557:{
								"nombres" : "Jose Pablo",
								"apellidos" : "Pardo, Hernández",
								"documento" : 44536160,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-1186",
												"nota" : 4.73,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-8291",
												"nota" : 3.96,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-6400",
												"nota" : 1.66,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-2339",
												"nota" : 4.43,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20150149472:{
								"nombres" : "Catalina Sara",
								"apellidos" : "Córdoba, García",
								"documento" : 89107372,
								"programa" : "HART",
								"materias" : [
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-9958",
												"nota" : 1.74,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-4066",
												"nota" : 3.87,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-8458",
												"nota" : 3.09,
												"creditos" : 3,
												"retirada" : "Si",
												},
											]
								},
					20130134592:{
								"nombres" : "Gabriela Camila",
								"apellidos" : "Sánchez, Sánchez",
								"documento" : 80992197,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-7888",
												"nota" : 3.43,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-3496",
												"nota" : 2.59,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-4822",
												"nota" : 4.72,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20190188795:{
								"nombres" : "Juan",
								"apellidos" : "Cuellar, García",
								"documento" : 90411603,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5644",
												"nota" : 4.15,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9442",
												"nota" : 4.77,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-2072",
												"nota" : 3.45,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20180158032:{
								"nombres" : "Mateo Gabriel",
								"apellidos" : "López, Jiménez",
								"documento" : 72342554,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-6232",
												"nota" : 2.76,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HAMO-9535",
												"nota" : 2.54,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-9114",
												"nota" : 2.58,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5889",
												"nota" : 4.29,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20180568756:{
								"nombres" : "Sofia Natalia",
								"apellidos" : "Romero, Álvarez",
								"documento" : 90763295,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-9838",
												"nota" : 2.34,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIGR-1403",
												"nota" : 2.27,
												"creditos" : 4,
												"retirada" : "Si",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-5158",
												"nota" : 1.88,
												"creditos" : 4,
												"retirada" : "Si",
												},
											]
								},
					20160296549:{
								"nombres" : "Camilo Daniel",
								"apellidos" : "Ramírez, Ramírez",
								"documento" : 51519517,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-5158",
												"nota" : 2.9,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ICIV-7003",
												"nota" : 2.38,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-3583",
												"nota" : 4.77,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-9442",
												"nota" : 3.62,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20200184437:{
								"nombres" : "Gabriel Julián",
								"apellidos" : "García, Ochoa",
								"documento" : 73923971,
								"programa" : "IBIO",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-5465",
												"nota" : 3.24,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-8126",
												"nota" : 3.16,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4502",
												"nota" : 2.52,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IBIO-4502",
												"nota" : 4.7,
												"creditos" : 3,
												"retirada" : "No",
												},
											]
								},
					20100235453:{
								"nombres" : "Maria Natalia",
								"apellidos" : "Cuellar, Martínez",
								"documento" : 32133868,
								"programa" : "ISIS",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-6565",
												"nota" : 3.92,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-4155",
												"nota" : 3.77,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-4305",
												"nota" : 4.95,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "ISIS-5216",
												"nota" : 1.77,
												"creditos" : 2,
												"retirada" : "Si",
												},
											]
								},
					20090136443:{
								"nombres" : "Mateo Oscar",
								"apellidos" : "Ochoa, Gómez",
								"documento" : 26803289,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5889",
												"nota" : 2.52,
												"creditos" : 0,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-2668",
												"nota" : 2.67,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-1652",
												"nota" : 2.15,
												"creditos" : 2,
												"retirada" : "Si",
												},
												{
												"facultad" : "Historia del Arte",
												"codigo" : "HART-4996",
												"nota" : 2.71,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20150362232:{
								"nombres" : "Jorge Camilo",
								"apellidos" : "Moreno, Hernández",
								"documento" : 61143392,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-1115",
												"nota" : 4.88,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-4328",
												"nota" : 3.72,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					20160127320:{
								"nombres" : "Gabriela Catalina",
								"apellidos" : "Ochoa, Pardo",
								"documento" : 40733914,
								"programa" : "IQUI",
								"materias" : [
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-3898",
												"nota" : 2.89,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-9815",
												"nota" : 2.95,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Ingenieria",
												"codigo" : "IQUI-4677",
												"nota" : 3.22,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20150164760:{
								"nombres" : "Andres Oscar",
								"apellidos" : "Jiménez, Moreno",
								"documento" : 96466972,
								"programa" : "MEDI",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQU-8159",
												"nota" : 4.96,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9490",
												"nota" : 4.65,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MEDI-9771",
												"nota" : 4.32,
												"creditos" : 2,
												"retirada" : "No",
												},
											]
								},
					20110215919:{
								"nombres" : "Juan Camilo",
								"apellidos" : "Pérez, Gómez",
								"documento" : 51702064,
								"programa" : "ICIV",
								"materias" : [
											]
								},
					20190181470:{
								"nombres" : "Mateo Nicolas",
								"apellidos" : "Torres, Díaz",
								"documento" : 70114652,
								"programa" : "DISE",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-1626",
												"nota" : 2.37,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-1995",
												"nota" : 4.83,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-9978",
												"nota" : 3.29,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DISE-6981",
												"nota" : 4.86,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20170135873:{
								"nombres" : "Jose Daniel",
								"apellidos" : "Romero, Ramírez",
								"documento" : 61689275,
								"programa" : "MENF",
								"materias" : [
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-2072",
												"nota" : 2.43,
												"creditos" : 2,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-2593",
												"nota" : 3.22,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-6067",
												"nota" : 4.58,
												"creditos" : 1,
												"retirada" : "No",
												},
												{
												"facultad" : "Medicina",
												"codigo" : "MENF-5889",
												"nota" : 2.59,
												"creditos" : 0,
												"retirada" : "No",
												},
											]
								},
					20190287188:{
								"nombres" : "Daniela Sofia",
								"apellidos" : "García, Córdoba",
								"documento" : 75179813,
								"programa" : "ARQD",
								"materias" : [
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-1564",
												"nota" : 2.72,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-3420",
												"nota" : 2.46,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-1864",
												"nota" : 3.94,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Arquitectura",
												"codigo" : "ARQD-1564",
												"nota" : 3.14,
												"creditos" : 3,
												"retirada" : "Si",
												},
											]
								},
					20170294793:{
								"nombres" : "Jorge Nicolas",
								"apellidos" : "Cuellar, Jiménez",
								"documento" : 49162279,
								"programa" : "DIIN",
								"materias" : [
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-2355",
												"nota" : 3.31,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIMD-4014",
												"nota" : 3.88,
												"creditos" : 3,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-3467",
												"nota" : 2.69,
												"creditos" : 4,
												"retirada" : "No",
												},
												{
												"facultad" : "Diseño",
												"codigo" : "DIIN-3467",
												"nota" : 2.54,
												"creditos" : 4,
												"retirada" : "No",
												},
											]
								},
					}))
                              
# Expected return:
# ({'Arquitectura': 3.5, 'Diseño': 3.51, 'Historia del Arte': 3.32, 'Ingenieria': 3.57, 'Medicina': 3.84}, ['ao.moreno72', 'as.moreno65', 'cc.moreno79', 'cd.diaz95', 'cd.ramirez17', 'cj.diaz79', 'cj.nino13', 'cl.sanchez46', 'cp.guitierrez74', 'dn.alvarez66', 'dp.moreno22', 'ds.cordoba13', 'ga.jimenez70', 'gc.pardo14', 'gc.sanchez97', 'gj.alvarez97', 'gj.ochoa71', 'gm.garcia13', 'gn.martinez48', 'go.fernandez88', 'gs.torres68', 'ja.lopez56', 'jc.guitierrez73', 'jc.hernandez92', 'jc.sanchez60', 'jc.sanchez71', 'jd.ramirez75', 'jg.cuellar03', 'jj.cuellar30', 'jj.ochoa30', 'jn.jimenez79', 'jp.hernandez60', 'ld.hernandez98', 'md.diaz36', 'mg.jimenez54', 'mn.diaz52', 'mn.martinez68', 'mo.gomez89', 'ng.martinez32', 'no.ramirez99', 'oj.cordoba71', 'pg.gomez25', 'pj.diaz67', 'sc.martinez33', 'sc.suarez26', 'sn.alvarez95', 'ss.ochoa48']) 
