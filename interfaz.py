import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from analizadorLexico import analizador,cargar_archivo_txt,numeroDeTokens,listaTokens,numeroDeErrores,listaErrores
from tablaTokens import reporte
from tablaErrores import tablaErrores
from generarSentencias import sentencias

ruta=""

def interfaz():
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Proyecto 2 LFP")
    ventana.geometry("850x720")
    
    # Limpiar el contenido actual
    def borrarPantalla():
        textboxPantalla.delete(1.0, tk.END)  
    
    # Función para abrir el explorador de archivos y obtener la ruta del archivo seleccionado
    def abrir_explorador():
        global ruta
        ruta = filedialog.askopenfilename()
        if ruta:
            # Leer el contenido del archivo
            with open(ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            # Insertar el contenido en el cuadro de texto
            borrarPantalla()
            textboxPantalla.insert(tk.END, contenido)
        messagebox.showinfo("Mensaje", "Se desplegado el archivo")
        
    def guardarArchivo():
        global ruta
        contenido = textboxPantalla.get("1.0", tk.END)  # Obtener todo el contenido del cuadro de texto
        # Guardar el contenido en el archivo
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
        messagebox.showinfo("Mensaje", "El archivo se ha guardado correctamente")
        
    def cerrarVentana(ventana):
        ventana.destroy()
    
    # Crear de arriba
    frameArriba = tk.Frame(ventana, width=840, height=50, background="grey", relief=tk.SUNKEN)
    frameArriba.grid(column=0, columnspan=3, row=0, pady=5, padx=5)
    
    # Crear una etiqueta para indicar el propósito del Combobox
    etiqueta = tk.Label(frameArriba, text="Archivo:")
    etiqueta.grid(column=0, row=0, padx=5, pady=5)
    
    # Crear un Combobox
    opcionesArchivo = ["Nuevo", "Abrir", "Guardar", "Salir"]
    comboboxArchivo = ttk.Combobox(frameArriba,values=opcionesArchivo)
    comboboxArchivo.grid(column=1, row=0, pady=5, padx=5)
    
    # Función para manejar la selección del combobox
    def seleccionar_opcion(event):
        seleccion = comboboxArchivo.get()
        if seleccion == "Abrir":
            abrir_explorador()
        if seleccion == "Nuevo":
            borrarPantalla()
            messagebox.showinfo("Mensaje", "Se Borro El area de Trabajo")
        if seleccion=="Guardar":
            guardarArchivo()
            messagebox.showinfo("Mensaje", "Se Ha Guardado El Archivo")
        if seleccion=="Salir":
            cerrarVentana(ventana)
    
    # Asignar una función para manejar la selección de opciones
    comboboxArchivo.bind("<<ComboboxSelected>>", seleccionar_opcion)
    
    # Crear una etiqueta para indicar el propósito del Combobox
    etiqueta = tk.Label(frameArriba, text="Analisis:")
    etiqueta.grid(column=2, row=0, padx=5, pady=5)
    
    # Crear un Combobox
    opcionesAnalisis = ["Generar Sentencias"]
    comboboxAnalisis = ttk.Combobox(frameArriba,values=opcionesAnalisis)
    comboboxAnalisis.grid(column=3, row=0, pady=5, padx=5)
    
    # Función para manejar la selección del combobox
    def seleccionar_opcion(event):
        seleccion = comboboxAnalisis.get()
        if seleccion == "Generar Sentencias":
            borrarPantalla()
            contenido="Sentencias MD"
            contenido+=sentencias()
            textboxPantalla.insert(tk.END, contenido)
            contenido=cargar_archivo_txt(ruta)
            analizador(contenido)
        
    
    # Asignar una función para manejar la selección de opciones
    comboboxAnalisis.bind("<<ComboboxSelected>>", seleccionar_opcion)
    
    # Crear una etiqueta para indicar el propósito del Combobox
    etiqueta = tk.Label(frameArriba, text="Tokens:")
    etiqueta.grid(column=4, row=0, padx=5, pady=5)
    
    # Crear un Combobox
    opcionesTokens = ["Nuevo Correlativo", "Token","Tabla"]
    comboboxTokens = ttk.Combobox(frameArriba,values=opcionesTokens)
    comboboxTokens.grid(column=5, row=0, pady=5, padx=5)
    
    # Función para manejar la selección del combobox
    def seleccionar_opcion(event):
        seleccion = comboboxTokens.get()
        
        if seleccion == "Nuevo Correlativo":
            contenido="Numero de tokens\n"
            contenido+=str(numeroDeTokens())
            borrarPantalla()
            textboxPantalla.insert(tk.END, contenido)
        if seleccion == "Token":
            contenido="Tabla de tokens\n"
            contenido+=listaTokens()
            borrarPantalla()
            textboxPantalla.insert(tk.END, contenido)     
        if seleccion == "Tabla":
            reporte()
        
    
    # Asignar una función para manejar la selección de opciones
    comboboxTokens.bind("<<ComboboxSelected>>", seleccionar_opcion)
    
    # Crear una etiqueta para indicar el propósito del Combobox
    etiqueta = tk.Label(frameArriba, text="Errores:")
    etiqueta.grid(column=6, row=0, padx=5, pady=5)
    
    # Crear un Combobox
    opcionesErrores = ["Nuevo Correlativo", "Token","Tabla"]
    comboboxErrores = ttk.Combobox(frameArriba,values=opcionesErrores)
    comboboxErrores.grid(column=7, row=0, pady=5, padx=5)
    
    # Función para manejar la selección del combobox
    def seleccionar_opcion(event):
        seleccion = comboboxErrores.get()
        if seleccion == "Nuevo Correlativo":
            contenido="Numero de errores\n"
            contenido+=str(numeroDeErrores())
            borrarPantalla()
            textboxPantalla.insert(tk.END, contenido)
        if seleccion == "Token":
            contenido="Tabla de tokens\n"
            contenido+=listaErrores()
            borrarPantalla()
            textboxPantalla.insert(tk.END, contenido)     
        if seleccion == "Tabla":
            tablaErrores()
        
    
    # Asignar una función para manejar la selección de opciones
    comboboxErrores.bind("<<ComboboxSelected>>", seleccionar_opcion)
    
    # Crear de abajo
    frameAbajo = tk.Frame(ventana, width=840, height=670, background="lightgrey", relief=tk.SUNKEN)
    frameAbajo.grid(column=0, columnspan=3, row=1, rowspan=5, pady=5, padx=5)
    
    # Crear el cuadro de texto
    textboxPantalla = tk.Text(frameAbajo, height=40, width=100)
    textboxPantalla.pack(padx=10, pady=10)
    
    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()
    
    
