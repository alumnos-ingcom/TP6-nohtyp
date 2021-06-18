################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from tp6ej1 import anagrama

def palabras_de_anagrama(texto):
    
    dos_palabras = texto.readline()
    
    lista_de_palabras = dos_palabras.split() 
    
    palabra1 = []
    
    palabra2 = []
    
    que_palabra = True
    
    for palabra in lista_de_palabras:
        
        if que_palabra:
            
            if palabra == "–":
            
                que_palabra = False
            
            else:
                palabra1.append(palabra)
        else:
            palabra2.append(palabra)
            
    palabra1 = " ".join(palabra1)
    
    palabra2 = " ".join(palabra2)
    
    return palabra1, palabra2
    
def principal():
    
    texto = open("anagramas.txt", "r+", 1, "utf-8")
    
    while True:
        
        palabra1, palabra2 = palabras_de_anagrama(texto)
        
        if palabra1 == "":
            
            break
        
        else:
            
            son_anagrama = anagrama(palabra1, palabra2)
        
        if son_anagrama:
            
            print(f"'{palabra1}' y '{palabra2}' son anagrama \n\n")
            
        else:
            
            print(f"'{palabra1}' y '{palabra2}' NO son anagrama\n\n")
            

if __name__ == "__main__":
    principal()

