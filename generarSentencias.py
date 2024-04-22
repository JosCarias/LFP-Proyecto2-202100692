from analizadorLexico import tokens,cargar_archivo_txt,analizador

listSentencias=[]
errores=[]
def sentencias():
    global sentencias
    i=0 
    for i in range(len(tokens)):
        if tokens[i] =="CrearBD" and tokens[i+3]=="nueva":
            nombre=tokens[i+1]
            listSentencias.append("use('"+nombre+"');")
        if tokens[i] =="EliminarBD" and tokens[i+3]=="nueva":
            nombre=tokens[i+1]
            listSentencias.append("db.dropDatabase();")
        if tokens[i] =="CrearColeccion" and tokens[i+3]=="nueva":
            nombre=tokens[i+1]
            listSentencias.append("db.createCollection('"+tokens[i+1]+"');")

    for sen in listSentencias:
        print(sen)






contenido=cargar_archivo_txt("entrada.txt")
analizador(contenido)
sentencias()
