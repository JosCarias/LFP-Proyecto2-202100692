tokens=[]
columnas=[]
filas=[]
errores=[]
erColumnas=[]
erFilas=[]
palabrasReservadas=["CrearBD",
                    "EliminarBD",
                    "CrearColeccion",
                    "EliminarColeccion"
                    ]

# Función para cargar el archivo .txt
def cargar_archivo_txt(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.readlines()
    return contenido

def analizador(contenido):
    memoria=[]
    for linea in contenido:
        lineaSinSangria = linea.strip()
        palabras = lineaSinSangria.split()     
        memoria.extend(palabras)
        
    
    i=0    
    for palabra in memoria:
        if palabra==palabrasReservadas[0]:
            tokens.append(palabrasReservadas[0])
            tokens.append(memoria[i+1])
            tokens.append(memoria[i+2])
            tokens.append(memoria[i+3])
            tokens.append(palabrasReservadas[0])
            tokens.append('(')
            tokens.append(")")
            tokens.append(';')
        if palabra==palabrasReservadas[1]:
            tokens.append(palabrasReservadas[1])
            tokens.append(memoria[i+1])
            tokens.append(memoria[i+2])
            tokens.append(memoria[i+3])
            tokens.append(palabrasReservadas[1])
            tokens.append('(')
            tokens.append(")")
            tokens.append(';')
        if palabra==palabrasReservadas[2]:
            tokens.append(palabrasReservadas[2])
            tokens.append(memoria[i+1])
            tokens.append(memoria[i+2])
            tokens.append(memoria[i+3])
            tokens.append(palabrasReservadas[2])
            tokens.append('(')
            tokens.append('"')
            tokens.append(memoria[i+4][16:-3])
            tokens.append('"')
            tokens.append(')')
        if palabra==palabrasReservadas[3]:
            tokens.append(palabrasReservadas[3])
    
            
        
        
        i+=1
        
    #for mem in memoria:
    #    print(mem)
    for token in tokens:
        print(token)   
        
#contenido=cargar_archivo_txt("entrada copy.txt") 
contenido=cargar_archivo_txt("entrada.txt")
analizador(contenido)