tokens=[]
columnas=[]
filas=[]
errores=[]
erColumnas=[]
erFilas=[]
palabrasReservadas=["CrearBD",
                    "=",
                    "nueva",
                    "(",
                    ")",
                    ";",
                    "EliminarBD"
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
        
    for palabra in memoria:
        if palabra[0:7]==palabrasReservadas[0]:
            tokens.append(palabrasReservadas[0])
        if palabra==palabrasReservadas[1]:
            tokens.append(palabrasReservadas[1])
        if palabra==palabrasReservadas[2]:
            tokens.append(palabrasReservadas[2])
        if len(palabra) >= 3 and palabra[-3] == palabrasReservadas[3]:
            tokens.append(palabrasReservadas[3])
        if len(palabra) >= 2 and palabra[-2] == palabrasReservadas[4]:
            tokens.append(palabrasReservadas[4])
        if len(palabra) >= 1 and palabra[-1] == palabrasReservadas[5]:
            tokens.append(palabrasReservadas[5])
        if palabra[0:10]==palabrasReservadas[6]:
            tokens.append(palabrasReservadas[6])
        
        

    for token in tokens:
        print(token)   
        
#contenido=cargar_archivo_txt("entrada copy.txt") 
contenido=cargar_archivo_txt("entrada.txt")
analizador(contenido)