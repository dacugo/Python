def inicio_reaccion(codigo: str, hora_terminacion: int, minuto_terminacion: int, duracion_horas:int, duracion_minutos:int, duracion_segundos:int) -> str: 
    
    hora_finalizacion_segundos= hora_terminacion * 3600 + minuto_terminacion * 60
    duracionEnSegundos = duracion_horas * 3600 + duracion_minutos * 60
    diferencia_segundos = hora_finalizacion_segundos - duracion_segundos

    horasEnSegundos_decimales = diferencia_segundos / 3600
    horasEnSegundos_enteras = int(horasEnSegundos_decimales)

    horas=str(horasEnSegundos_enteras).zfill(2) #Salida horas

    minutosEnSegundos_decimales = (horasEnSegundos_decimales - horasEnSegundos_enteras) / 60
    minutosEnSegundos_enteras = int(minutosEnSegundos_decimales)

    minutos=str(minutosEnSegundos_enteras).zfill(2)  #Salida minutos

    segundos_decimales = (minutosEnSegundos_decimales-minutosEnSegundos_enteras) * 60
    segundos_enteros = int(segundos_decimales)

    segundos=str(segundos_enteros).zfill(2)    #Salida segundos

    return "La reacción {} debe iniciarse a las {} horas, {} minutos con {} segundos para que esté lista en en el momento requerido".format(codigo,horas,minutos,segundos)

print(inicio_reaccion("HHA01",16,30,4,11,23))