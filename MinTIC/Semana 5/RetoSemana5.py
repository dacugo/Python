import pandas as pd


#ruta_archivo_csv = r"owid-covid-data.csv"
#leer la información
#ruta_archivo_csv = pd.read_csv(r'C:\Users\Daniel CG\Documents\Programación\Python\PraticasPython\MinTIC\Semana 5\owid-covid-data.csv')
ruta_archivo_csv = r'C:\Users\Daniel CG\Documents\Programación\Python\PraticasPython\MinTIC\Semana 5\owid-covid-data.csv'

import pandas as pd

def caso_who(ruta_archivo_csv: str)-> dict:
        if ruta_archivo_csv[-4:] == '.csv':
                try:
                        datos = pd.read_csv(ruta_archivo_csv)
                except:
                        return 'Error al leer el archivo de datos.'
                #Organizar la información con ayuda de las series
                datosCalculos = pd.DataFrame({'fechas':datos['date'],
                                'casos_por_millon':datos['total_cases_per_million'],
                                        'poblacion':datos['population'],
                        'camas_hospital_por_miles':datos['hospital_beds_per_thousand'],
                        'continente':datos['continent']
                        })
                #tranformar el formato de fechas
                datosCalculos['fechas'] = pd.to_datetime(datosCalculos['fechas'])
                datosCalculos.set_index('fechas',inplace=True)
                #calcular la razón
                try:
                        datosCalculos['casos_totales'] = (datosCalculos['casos_por_millon'] * datosCalculos['poblacion'])/1000000
                        datosCalculos['total_camas'] = (datosCalculos['camas_hospital_por_miles'] * datosCalculos['poblacion'])/1000
                        datosCalculos['razon'] = datosCalculos['casos_totales'] / datosCalculos['total_camas']
                except:
                        
                #agrupar en un dataframe
                df_resultado = datosCalculos.groupby(['fechas','continente'])['razon'].mean().unstack()
                #transformar el dataframe en diccionario
                return df_resultado.to_dict()
        else:
                return 'Extensión inválida.'

print(caso_who(ruta_archivo_csv))