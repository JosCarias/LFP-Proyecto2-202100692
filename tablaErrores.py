import webbrowser
import os
from analizadorLexico import cargar_archivo_txt,analizador,tokens,palabrasReservadas,filas,columnas,errores,erColumnas,erFilas

def tablaErrores():
    tabla_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte</title>
</head>
<body>'''
    tabla_html+='''<table border="1" cellborder="1" cellspacing="0" style="position: absolute; left: 50%;">\n'''
    tabla_html+='''    <tr>
        <td>Token</td>
        <td>Filas</td>
        <td>Columna</td>           
    </tr>\n'''
    i=0
    for i in range(len(errores)):
        tabla_html+='    <tr>\n'
        tabla_html+='       <td>'+str(errores[i])+'</td>\n'
        tabla_html+='       <td>'+str(erFilas[i])+'</td>\n'
        tabla_html+='       <td>'+str(erColumnas[i])+'</td>\n'
        tabla_html+='    </tr>\n'     
    tabla_html+='''</table>\n'''
    tabla_html+='''</body>\n</html>'''

    # Agregar el contenido HTML en un archivo
    with open("tablaEr.html", "w", encoding="utf-8") as f:
        f.write(tabla_html)

    # Abrir el archivo en el navegador
    ruta_absoluta = os.path.abspath("tablaEr.html")
    webbrowser.open("file://" + ruta_absoluta)
    
#contenido=cargar_archivo_txt("entrada.txt")
#analizador(contenido)
#tablaErrores()
    