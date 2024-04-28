# Manual de Tecnico de la proyecto 1

## Introducción
El proyecto consiste en la elaboración de una herramienta que permita el diseño y 
creación de sentencias de bases de datos no relacionales de una forma sencilla.  La 
aplicación tendrá un área de edición de código y un área de visualización de la 
sentencia final generada.      
Cuando  ya  se  cuente  con  las  sentencias  creadas  inicialmente,  se  procederá  a 
realizar la compilación respectiva lo que generar las sentencias de MongoDB que 
serán mostradas en el espacio de resultados que posteriormente se podrán aplicar 
a un entorno adecuado a MongoDb.

## Requisitos del Sistema
- Visual code
- Sistema Operativo: Compatible con Pytho
- Python 3.12.2  o superior
- Graphviz
- Navegador Web: Google Chrome, Mozilla Firefox, Safari

## Clase principal
Esta clase actúa como punto de entrada del programa. Se encarga de iniciar la aplicación y dirigir el flujo de ejecución hacia las otras clases y componentes del sistema. En el diagrama mostrado se resalta que esta clase es la principal y que no cuenta con un constructor explícito, lo que indica que su inicialización y ejecución se realizan directamente al iniciar el programa.
![alt text](imagenes\1.png)

## AnalizadorLexico
Esta clase se encarga de realizar el análisis léxico del código fuente proporcionado por el usuario. Utiliza un diccionario de palabras reservadas para identificar y clasificar tokens específicos en el código. La función analizador recorre línea por línea del archivo, buscando coincidencias con las palabras reservadas definidas en el diccionario. Cuando encuentra una coincidencia, registra la fila y la columna correspondientes en las que se encontró la palabra clave.
![alt text](imagenes\2.png)

## interfaz
La clase interfaz en reporte.py se encarga de crear la interfaz gráfica del programa utilizando la biblioteca Tkinter de Python. La interfaz gráfica proporciona una manera fácil e intuitiva para que los usuarios interactúen con el sistema y visualicen los resultados del análisis léxico.

Componentes de la interfaz
Botón "Cargar Archivo": Permite al usuario seleccionar y cargar un archivo de código fuente para su análisis.
Área de texto "Editor": Muestra el contenido del archivo cargado y permite al usuario realizar modificaciones si es necesario.
Botón "Analizar": Inicia el proceso de análisis léxico del código fuente cargado.
Área de texto "Resultados": Muestra los resultados del análisis léxico, como los tokens identificados y sus ubicaciones en el código fuente.
Botón "generar las sentencias": Genera un archivo HTML que muestra los resultados del análisis léxico en forma de una tabla estructurada.
Botón "Limpiar": Borra el contenido de las áreas de texto "Editor" y "Resultados", permitiendo al usuario cargar y analizar un nuevo archivo si lo desea.
Botón "Salir": Cierra la aplicación.
![alt text](imagenes\3.png)

## erroresSintacticos
Esta clase genera una lista de los errores encontrados en el archivo de entrada. Es invocada desde la interfaz para mostrar los errores al usuario
![alt text](imagenes\4.png)

## generarSentencias
La clase generarSentencias se encarga de leer y construir las sentencias para MongoDB a partir del código fuente analizado.
![alt text](imagenes\5.png)

## tablaErrores
Esta función genera una tabla HTML para mostrar los errores encontrados durante el análisis léxico.
![alt text](imagenes\6.png)

## tablatokes
Esta función genera una tabla HTML para mostrar los tokens identificados durante el análisis léxico.

Cada componente desempeña un papel crucial en el funcionamiento global de la herramienta, facilitando la creación y análisis de sentencias de bases de datos no relacionales.
![alt text](imagenes\7.png)
