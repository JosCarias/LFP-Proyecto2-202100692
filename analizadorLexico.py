tokens=[]
columnas=[]
filas=[]
errores=[]
erColumnas=[]
erFilas=[]
palabrasReservadas=["CrearBD",
                    "EliminarBD",
                    "CrearColeccion",
                    "EliminarColeccion",
                    "InsertarUnico",
                    "ActualizarUnico",
                    "EliminarUnico",
                    "BuscarTodo",
                    "BuscarUnico"
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
            if memoria[i+1][-1]==";":
                tokens.append('(')
                tokens.append('"')
                tokens.append(memoria[i+1][2:-3])
                tokens.append('"')
                tokens.append(')')
                tokens.append(';')
            else:
                tokens.append(memoria[i+1])
                tokens.append(memoria[i+2])
                tokens.append(memoria[i+3])
        if palabra==palabrasReservadas[4]:
            tokens.append(palabrasReservadas[4])
            tokens.append(memoria[i+1])
            tokens.append(memoria[i+2])
            tokens.append(memoria[i+3])
            tokens.append(palabrasReservadas[4])
            tokens.append('(')
            tokens.append('"')
            tokens.append(memoria[i+4][15:-3])
            tokens.append('"')
            tokens.append(',')
            tokens.append('"')
            tokens.append(memoria[i+5])
            tokens.append('"')
            tokens.append(memoria[i+6][1:-2])
            tokens.append('"')
            tokens.append(':')
            tokens.append('"')
            tokens.append(memoria[i+7][1:-2])    
            tokens.append('"')
            tokens.append(',')
            tokens.append('"')
            tokens.append(memoria[i+8][1:-2])
            tokens.append('"')
            tokens.append(',')
            tokens.append('"')
            tokens.append(memoria[i+9][1:-2])
            tokens.append('"')
            tokens.append(memoria[i+10])
            tokens.append('"')
            tokens.append(')')
            tokens.append(';')
        if palabra==palabrasReservadas[5]:
            tokens.append(palabrasReservadas[5])
            tokens.append(memoria[i+1])
            tokens.append(memoria[i+2])
            tokens.append(memoria[i+3])
            tokens.append(palabrasReservadas[5])
            tokens.append('(')
            tokens.append('"')
            tokens.append(memoria[i+4][17:-2])
            tokens.append('"')
            tokens.append(',')
            tokens.append('"')
            tokens.append(memoria[i+6])
            tokens.append('"')
            tokens.append(memoria[i+7][1:-2])
            tokens.append(':')
            tokens.append('"')
            tokens.append(memoria[i+8][1:-1])
            tokens.append('"')
            tokens.append('}')
            tokens.append(',')
            tokens.append(memoria[i+10])
            tokens.append(memoria[i+11][:-1])
            tokens.append(':')
            tokens.append('{')
            tokens.append('"')
            tokens.append(memoria[i+12][2:-2])
            tokens.append('"')
            tokens.append(':')
            tokens.append('"')
            tokens.append(memoria[i+13][1:-2])
            tokens.append('"')
            tokens.append('}')
            tokens.append('"')
            tokens.append(')')
            tokens.append(';')
        if palabra==palabrasReservadas[6]:
            tokens.append(palabrasReservadas[6])
            tokens.append(memoria[i+1])
            tokens.append(memoria[i+2])
            tokens.append(memoria[i+3])
            tokens.append(palabrasReservadas[6])
            tokens.append("(")
            tokens.append('"')
            tokens.append(memoria[i+4][15:-2])
            tokens.append('"')
            tokens.append(',')
            tokens.append('"')
            tokens.append(memoria[i+6])
            tokens.append('"')
            tokens.append(memoria[i+7][1:-2])
            tokens.append('"')
            tokens.append(':')
            tokens.append('"')
            tokens.append(memoria[i+8][1:-1])
            tokens.append('"')
            tokens.append(memoria[i+9])
            tokens.append('"')
            tokens.append(')')
            tokens.append(';')
        if palabra==palabrasReservadas[7]:
            tokens.append(palabrasReservadas[7])
            tokens.append(memoria[i+1])
            tokens.append(memoria[i+2])
            tokens.append(memoria[i+3])
            tokens.append(palabrasReservadas[7])
            tokens.append("(")
            tokens.append('"')
            tokens.append(memoria[i+4][12:-3])
            tokens.append('"')
            tokens.append(')')
            tokens.append(';')
        if palabra==palabrasReservadas[8]:
            tokens.append(palabrasReservadas[8])
            tokens.append(memoria[i+1])
            tokens.append(memoria[i+2])
            tokens.append(memoria[i+3])
            tokens.append(palabrasReservadas[8])
            tokens.append("(")
            tokens.append('"')
            tokens.append(memoria[i+4][13:-3])
            tokens.append('"')
            tokens.append(')')
            tokens.append(';')
        i+=1
        
    for token in tokens:
        print(token)   
        
#contenido=cargar_archivo_txt("entrada copy.txt") 
contenido=cargar_archivo_txt("entrada.txt")
analizador(contenido)