from analizadorLexico import errores

def erroresSin():
    cadena=""
    for error in errores:
        cadena+=error+"\n"
    return cadena
    