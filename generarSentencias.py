from analizadorLexico import tokens

listSentencias=[]

def sentencias():
    i=0 
    for i in range(len(tokens)):
        if tokens[i] =="CrearBD" and tokens[i+3]=="nueva":
            nombre=tokens[i+1]
            listSentencias.append("use('" + nombre + "');")  
        if tokens[i] =="EliminarBD" and tokens[i+3]=="nueva":
            nombre=tokens[i+3]
            listSentencias.append("db.dropDatabase();")                                       
        if tokens[i] =="CrearColeccion" and tokens[i+3]=="nueva":
            nombre=tokens[i+1]
            listSentencias.append("db.createCollection('"+tokens[i+1]+"');")
        if tokens[i] =="EliminarColeccion" and tokens[i+3]=="nueva":
            nombre=tokens[i+1]
            listSentencias.append("db."+nombre+".drop();")
        if tokens[i] =="EliminarColeccion" and tokens[i+3]!="nueva":
            nombre=tokens[i+3]
            listSentencias.append("db."+nombre+".drop();")
        if tokens[i] =="InsertarUnico" and tokens[i+3]=="nueva":
            nombre=tokens[i+7]
            listSentencias.append("db."+nombre+".insertOne(ARCHIVOJSON);")
        if tokens[i] =="ActualizarUnico" and tokens[i+3]=="nueva":
            nombre=tokens[i+7]
            listSentencias.append("db."+nombre+".updateOne(ARCHIVOJSON);")
        if tokens[i] =="EliminarUnico" and tokens[i+3]=="nueva":
            nombre=tokens[i+7]
            listSentencias.append("db."+nombre+".deleteOne(ARCHIVOJSON);")
        if tokens[i] =="BuscarTodo" and tokens[i+3]=="nueva":
            nombre=tokens[i+7]
            listSentencias.append("db."+nombre+".find();")
        if tokens[i] =="BuscarUnico" and tokens[i+3]=="nueva":
            nombre=tokens[i+7]
            listSentencias.append("db."+nombre+".findOne();")
            
    cadena=""
    for sen in listSentencias:
        cadena+=sen+"\n"
    
    return cadena





#contenido=cargar_archivo_txt("entrada.txt")
#analizador(contenido)
#sentencias()
