################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°6
"""
import random

import tp6ej1

def hace_etiqueta(contenido, etiqueta):
    '''
    Retorna el contenido envuelto en una etiqueta como está indicado en el segundo argumento.
    La funcion llamada con contenido="Hola" y etiqueta="h1" retornará
    <h1>Hola</h1>
    '''
    etiqueta = "<" + etiqueta + ">" + contenido + "</" + etiqueta + ">"
    return etiqueta
    
def hace_comenta(contenido):
    '''
    Retorna el contenido envuelto en las marcas de comentario HTML
    <!--  -->
    (separen las marcas del contenido con un espacio)
    '''
    comentario = "<!-- " + contenido + " -->"
    return comentario

def archivo_html(nombre):
    '''
    Crea un archivo html con un nombre ingresado por el usuario
    '''
    color_de_fondo = random.randint(-9999, 9999)
    
    nombre_final = nombre + ".html"
    encabezado1 = hace_etiqueta('Hola HTML', 'h1')
    encabezado2 = hace_etiqueta('Hola HTML', 'h2')
    encabezado3 = hace_etiqueta('Hola HTML', 'h3')
    encabezado4 = hace_etiqueta('Hola HTML', 'h4')
    encabezado5 = hace_etiqueta('Hola HTML', 'h5')
    parrafo = hace_etiqueta('Mama estoy en internet', 'p')
    with open(nombre_final, "x", 1, "utf-8") as archivo:
        archivo.write("<html>\n"
                     f"    <body bgcolor = #{color_de_fondo}>\n"
                     f"        {encabezado1}\n"
                     f"        {encabezado2}\n"
                     f"        {encabezado3}\n"
                     f"        {encabezado4}\n"
                     f"        {encabezado5}\n"
                     f"        {parrafo}\n"
                      "        <img src=https://i.pinimg.com/originals/c4/7d/88/c47d88963c6fd217884893c33bdc661d.gif alt=Mi imagen de prueba>\n"                      
                      "    </body>\n"
                      "    <footer>\n"
                      "        © Copyright 2021 INGCOM-UNRN/nohtyp\n"
                      "    </footer>\n"
                      "</html>")

def principal():
    tp6ej1.marco("archivo_html()")
    nombre = input("Ingrese el nombre del archivo html: ")
    archivo_html(nombre)
    print(f"El nombre del nuevo archivo es: '{nombre}.html'")
    
if __name__ == "__main__":
    principal()