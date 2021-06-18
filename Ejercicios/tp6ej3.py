################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°3
"""
import tp6ej1

def copiadora(texto_1, texto_2):
    """
    Esta función copia el contenido de un archivo de entrada en otro
    archivo de salida
    """
    with open(texto_1, "r", 1, "utf-8") as entrada:
        with open(texto_2, "w", 1, "utf-8") as salida:
            copia = entrada.read()
            salida.write(copia)

def principal():
    tp6ej1.marco("copiadora()")
    texto_1 = input("Ingrese el nombre del archivo de entrada: ")
    texto_2 = input("Ingrese el nombre del archivo de salida: ")
    copiadora(texto_1, texto_2)

if __name__ == "__main__":
    principal()