
################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def anagrama(cadena1, cadena2):
    
    sin_espacios = cadena1.replace(" ", "")
    
    sin_espacios = sin_espacios.lower()
    
    lista1 = list(sin_espacios)
    
    sin_espacios = cadena2.replace(" ", "")
    
    sin_espacios = sin_espacios.lower()
    
    lista2 = list(sin_espacios)
    
    cantidad_de_coincidencias = 0
    
    cantidad_de_letras = 0 
    
    for letra_2 in lista2:
        
        cantidad_de_letras += 1
    
    for letra in lista1:
        
        try:       
            
            lista2.index(letra)
            lista2.remove(letra)


            cantidad_de_coincidencias += 1
            
        except ValueError:
            
            pass
            
    if cantidad_de_coincidencias == cantidad_de_letras:
        
        return True
    
    else:
        
        return False
                           

def principal():
    
    palabra1 = input("ingrese 1 palabra \n")
    
    palabra2 = input("ingrese una segunda palabra \n")
    
    son_anagrama = anagrama(palabra1, palabra2)
    
    if son_anagrama:
        
        print(f"'{palabra1}' y '{palabra2}' son anagramas")
        
    else:
        
        print(f"'{palabra1}' y '{palabra2}' NO son anagramas")
        

if __name__ == "__main__":
    principal()
