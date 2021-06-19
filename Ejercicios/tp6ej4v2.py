################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

import apoyo

"""
no se me ocurrio una funcion clara para este ejercicio, ya que senti que teniamos por separado cada funcion,
por eso todo directamente esta en principal. la unica funcion es un generador de archivos de texto aleatorio
que se encuentra en 'apoyo'.
"""
def genera_archivo(texto):
    
    """
    Esta funcion convierte un texto en archivo, se esta usando
    para hacer un texto aleatorio.
    """
    nombre = input("ingrese el nombre del archivo \n\n" )
    
    nombre = list(nombre)
    
    nombre.append(".txt")
    
    nombre = "".join(nombre)
    
    with open(nombre, "w", 1, "utf-8") as archivo:
        
        archivo.write(texto)
        
def principal():
    
    respuesta = input("desea generar un archivo?\n\n      Y - N\n\n")
    
    if respuesta == "y" or respuesta == "Y":
        
        cantidad= apoyo.ingreso_entero("cuandas palabras desea en su archivo?\n")
        
        genera_archivo(apoyo.texto_generator(cantidad))
    
    nombre = input("ingrese el nombre del archivo a codificar:\n")
    nombre = list(nombre)
    nombre.append(".txt")
    nombre = "".join(nombre)
    
    with open(nombre, "r", 1, "utf-8") as texto:
        
        texto_a_codificar = texto.read()
        
    cantidad_de_codificacion = apoyo.ingreso_entero("ingrese la cantidad de codificado")    
    
    texto_codificado = apoyo.codificador(texto_a_codificar, cantidad_de_codificacion)
    
    nombre = nombre.replace(".txt","")
    
    with open(f"{nombre}.cesar.txt", "w", 1, "utf-8") as codificado:
        
        codificado.write(texto_codificado)
        
if __name__ == "__main__":
    principal()

