################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°1
"""

def anagrama(cadena1, cadena2):
    """
    Esta función indica si dos cadenas son anagramas
    """
    
    palabra1 = cadena1
    
    palabra2 = cadena2
    
    if not cadena1.isalpha():
        
        depuracion = list(cadena1)
        
        for caracter in depuracion:
            
            if not caracter.isalpha():
                
                palabra1 = palabra1.replace(caracter,"")
    
    if not cadena2.isalpha():
        
        depuracion = list(cadena2)
        
        for caracter in depuracion:
            
            if not caracter.isalpha():
                
                palabra2 = palabra2.replace(caracter,"")
    
    todo_minuscula1 = palabra1.lower()   
    
    todo_minuscula2 = palabra2.lower()    
    
    cadena_de_acentos =  "á é í ó ú"
       
    lista1 = list(todo_minuscula1)
    lista2 = list(todo_minuscula2)
    
    cantidad_de_coincidencias = 0
    cantidad_de_letras = 0
    
    
    for letra_2 in lista2:
        
        cantidad_de_letras = cantidad_de_letras + 1
        
        if cadena_de_acentos.find(letra_2) > -1:
        
            if letra_2 == "á":
                
                todo_minuscula2 = todo_minuscula2.replace(letra_2, "a")
                
            elif letra_2 == "é":
                
                todo_minuscula2 = todo_minuscula2.replace(letra_2, "e")
                
            elif letra_2 == "í":
                
                todo_minuscula2 = todo_minuscula2.replace(letra_2, "i")
                
            elif letra_2 == "ó":
                
                todo_minuscula2 = todo_minuscula2.replace(letra_2, "o")
                
            elif letra_2 == "ú":
                
                todo_minuscula2 = todo_minuscula2.replace(letra_2, "u")
                
    for letra_1 in lista1:
        
        if cadena_de_acentos.find(letra_1) > -1:
        
            if letra_1 == "á":
                
                todo_minuscula1 = todo_minuscula1.replace(letra_1, "a")
                
            elif letra_1 == "é":
                
                todo_minuscula1 = todo_minuscula1.replace(letra_1, "e")
                
            elif letra_1 == "í":
                
                todo_minuscula1 = todo_minuscula1.replace(letra_1, "i")
                
            elif letra_1 == "ó":
                
                todo_minuscula1 = todo_minuscula1.replace(letra_1, "o")
                
            elif letra_1 == "ú":
                
                todo_minuscula1 = todo_minuscula1.replace(letra_1, "u")
                
    lista1 = list(todo_minuscula1)
    lista2 = list(todo_minuscula2)
    
    for letra in lista1:
        
        try:
            
            lista2.index(letra)
            
            lista2.remove(letra)
            
            cantidad_de_coincidencias = cantidad_de_coincidencias + 1
            
        except ValueError: # este value error esta solo para atajar el error de "lista2.index" y seguir con el programa
                           # porque cuando una palabra no es anagrama con otra tiraria error, y eso no es error, es que no
                           # son anagrama
            pass
            
    return cantidad_de_coincidencias == cantidad_de_letras

def marco(texto):
    """
    Esta funcion crea un marco a un texto deseado
    """
    print("\n"+"╴"*80)
    print("╔"+"═"*len(texto)+"╗")
    print(f"║{texto}║")
    print("╚"+"═"*len(texto)+"╝")
    print("╴"*80)

def principal():
    
    marco("anagrama()")
    
    palabra1 = input("Ingrese una palabra: ")
    
    palabra2 = input("Ingrese otra palabra: ")
    
    son_anagrama = anagrama(palabra1, palabra2)
    
    if son_anagrama:
        
        print(f"\n'{palabra1}' y '{palabra2}' son anagramas")
    else:
        print(f"\n'{palabra1}' y '{palabra2}' NO son anagramas")

if __name__ == "__main__":
    principal()