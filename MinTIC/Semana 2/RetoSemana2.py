"""
informacion={'id_prestamo':'RETOS2_001',
                'casado':'No',
                'dependientes':'1',
                'educacion':'Graduado',
                'independiente':'Si',
                'ingreso_deudor':4692,
                'ingreso_codeudor':0,
                'cantidad_prestamo':106,
                'plazo_prestamo':360,
                'historia_credito':1,
                'tipo_propiedad':'Rural'    
            }

informacion2={'id_prestamo':'RETOS2_002',
                'casado':'No',
                'dependientes':'3+',
                'educacion':'No Graduado',
                'independiente':'No',
                'ingreso_deudor':1830,
                'ingreso_codeudor':0,
                'cantidad_prestamo':100,
                'plazo_prestamo':360,
                'historia_credito':0,
                'tipo_propiedad':'Urbano'    
            }
"""
informacion1 = {"id_prestamo":"RETOS2_001",
               "casado":"No",
               "dependientes":1,
               "educacion":"Graduado",
               "independiente":"Si",
               "ingreso_deudor":4692,
               "ingreso_codeudor":0,
               "cantidad_prestamo":105,
               "plazo_prestamo":360,
               "historia_credito":1,
               "tipo_propiedad":"Rural"}

informacion2 = {"id_prestamo":"RETOS2_002",
               "casado":"No",
               "dependientes":"3+",
               "educacion":"No Graduado",
               "independiente":"No",
               "ingreso_deudor":1850,
               "ingreso_codeudor":0,
               "cantidad_prestamo":100,
               "plazo_prestamo":360,
               "historia_credito":0,
               "tipo_propiedad":"Urbano"}

informacion3 = {"id_prestamo":"RETOS2_003",
               "casado":"No",
               "dependientes":0,
               "educacion":"No Graduado",
               "independiente":"No",
               "ingreso_deudor":3748,
               "ingreso_codeudor":1668,
               "cantidad_prestamo":110,
               "plazo_prestamo":360,
               "historia_credito":1,
               "tipo_propiedad":"Semi Urbano"}

informacion4 = {"id_prestamo":"RETOS2_004",
               "casado":"No",
               "dependientes":"3+",
               "educacion":"Graduado",
               "independiente":"No",
               "ingreso_deudor":3083,
               "ingreso_codeudor":0,
               "cantidad_prestamo":255,
               "plazo_prestamo":360,
               "historia_credito":1,
               "tipo_propiedad":"Rural"}

informacion5 = {"id_prestamo":"RETOS2_005",
               "casado":"Si",
               "dependientes":2,
               "educacion":"Graduado",
               "independiente":"Si",
               "ingreso_deudor":11500,
               "ingreso_codeudor":0,
               "cantidad_prestamo":287,
               "plazo_prestamo":360,
               "historia_credito":0,
               "tipo_propiedad":"Urbano"}

informacion6 = {"id_prestamo":"RETOS2_006",
               "casado":"Si",
               "dependientes":"3+",
               "educacion":"Graduado",
               "independiente":"Si",
               "ingreso_deudor":800,
               "ingreso_codeudor":2000,
               "cantidad_prestamo":100,
               "plazo_prestamo":360,
               "historia_credito":1,
               "tipo_propiedad":"Urbano"}

informacion7 = {"id_prestamo":"RETOS2_007",
               "casado":"Si",
               "dependientes":"3+",
               "educacion":"Graduado",
               "independiente":"Si",
               "ingreso_deudor":800,
               "ingreso_codeudor":1100,
               "cantidad_prestamo":100,
               "plazo_prestamo":360,
               "historia_credito":1,
               "tipo_propiedad":"Urbano"}

informacion8 = {"id_prestamo":"RETOS2_008",
               "casado":"No",
               "dependientes":"3+",
               "educacion":"Graduado",
               "independiente":"Si",
               "ingreso_deudor":1000,
               "ingreso_codeudor":1000,
               "cantidad_prestamo":100,
               "plazo_prestamo":360,
               "historia_credito":0,
               "tipo_propiedad":"Urbano"}

informacion9 = {"id_prestamo":"RETOS2_009",
               "casado":"No",
               "dependientes":"3+",
               "educacion":"Graduado",
               "independiente":"Si",
               "ingreso_deudor":2000,
               "ingreso_codeudor":2000,
               "cantidad_prestamo":100,
               "plazo_prestamo":360,
               "historia_credito":0,
               "tipo_propiedad":"Urbano"}

informacion10 = {"id_prestamo":"RETOS2_010",
               "casado":"No",
               "dependientes":"3+",
               "educacion":"Graduado",
               "independiente":"Si",
               "ingreso_deudor":2000,
               "ingreso_codeudor":2000,
               "cantidad_prestamo":190,
               "plazo_prestamo":360,
               "historia_credito":0,
               "tipo_propiedad":"Urbano"}

informacion11 = {"id_prestamo":"RETOS2_011",
               "casado":"No",
               "dependientes":1,
               "educacion":"No Graduado",
               "independiente":"No",
               "ingreso_deudor":2000,
               "ingreso_codeudor":2000,
               "cantidad_prestamo":190,
               "plazo_prestamo":360,
               "historia_credito":0,
               "tipo_propiedad":"Urbano"}

informacion12 = {"id_prestamo":"RETOS2_012",
               "casado":"No",
               "dependientes":1,
               "educacion":"Graduado",
               "independiente":"No",
               "ingreso_deudor":1200,
               "ingreso_codeudor":1200,
               "cantidad_prestamo":100,
               "plazo_prestamo":360,
               "historia_credito":0,
               "tipo_propiedad":"Urbano"}

informacion13 = {"id_prestamo":"RETOS2_013",
               "casado":"No",
               "dependientes":1,
               "educacion":"Graduado",
               "independiente":"No",
               "ingreso_deudor":1200,
               "ingreso_codeudor":1100,
               "cantidad_prestamo":100,
               "plazo_prestamo":360,
               "historia_credito":0,
               "tipo_propiedad":"Urbano"}

def prestamo(informacion:dict)->dict:
    id_prestamo=informacion['id_prestamo']
    c=informacion['casado']
    e=informacion['educacion']
    i=informacion['independiente']
    d=informacion['dependientes']
    i_d=informacion['ingreso_deudor']
    i_c=informacion['ingreso_codeudor']
    c_p=informacion['cantidad_prestamo']
    p_p=informacion['plazo_prestamo']
    h_c=informacion['historia_credito']
    t_p=informacion['tipo_propiedad']
    
    if(d=='3+'):
        d=3
    else:
        d=int(d)

    #historia de credito verdadera
    if(h_c==1):
        if(i_c>0 and i_d/9>c_p):
            prestamo=True
        else:
            if(d>2 and i=='Si'):
                if((i_c/12)>c_p):
                    prestamo=True
                else:
                    prestamo=False
            else:
                if(c_p<200):
                    prestamo=True
                else:
                    prestamo=False
    #historia de crédito falsa
    else:
        if(i=='Si'):
            if(not(c=='Si' and d>1)):
                if(i_d/10>c_p or i_c/10>c_p):
                    if(c_p<180):
                        prestamo=True
                    else:
                        prestamo=False
                else:
                    prestamo=False
            else:
                prestamo=False
        else:
            if(t_p!='Semiurbano' and d<2):
                if(e=='Graduado'):
                    if(i_d/11>c_p and i_c/11>c_p):
                        prestamo=True
                    else:
                        prestamo=False
                else:
                    prestamo=False
            else:
                prestamo=False

    if(prestamo==True):
        return {'id_prestamo':id_prestamo, 'aprobado':True}
    else:
        return {'id_prestamo':id_prestamo, 'aprobado':False}

print(prestamo(informacion1))
print(prestamo(informacion2))
print(prestamo(informacion3))
print(prestamo(informacion4))
print(prestamo(informacion5))
print(prestamo(informacion6))
print(prestamo(informacion7))
print(prestamo(informacion8))
print(prestamo(informacion9))
print(prestamo(informacion10))
print(prestamo(informacion11))
print(prestamo(informacion12))
print(prestamo(informacion13))