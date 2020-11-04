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

def promedio_facultades(info:dict,contando_externos:bool)->tuple:
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
    
    if contando_externos :
        try:
            for i in range(totalestudiantes):
                contactar=False     # Bandera para contactar
                materiasestudiante=len(info[llaves[i]]["materias"]) # Número de materias del estudiante
                for j in range(materiasestudiante):
                    Retirada=info[llaves[i]]["materias"][j]["retirada"]
                    NumCre=info[llaves[i]]["materias"][j]["creditos"]
                    Facultad=info[llaves[i]]["materias"][j]["facultad"]
                    if Retirada == 'No' and NumCre != 0 :
                        contactar = True
                        nota=info[llaves[i]]["materias"][j]["nota"]
                        Promediosf[Facultad][0]=nota*NumCre+Promediosf[Facultad][0]
                        Promediosf[Facultad][1]=NumCre+Promediosf[Facultad][1]
                if contactar == True:
                    CorreoEstudiantes.append(correos(info,i))
        except:
            return "Error numérico."
    else:
        try:
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
                            if Retirada == 'No' and NumCre != 0 :
                                contactar = True
                                nota=info[llaves[i]]["materias"][j]["nota"]
                                Promediosf[Facultad][0]=nota*NumCre+Promediosf[Facultad][0]
                                Promediosf[Facultad][1]=NumCre+Promediosf[Facultad][1]
                    if contactar == True:
                        CorreoEstudiantes.append(correos(info,i))
        except :
            return "Error numérico."
    
    PromediosFinal= Promediosf.copy()
    for i in facultades1:
        PromediosFinal[i]=round(Promediosf[i][0]/ Promediosf[i][1],2)
    CorreoEstudiantes=sorted(CorreoEstudiantes)
    return((PromediosFinal,CorreoEstudiantes))
    
    
            
    







