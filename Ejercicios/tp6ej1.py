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
    sin_espacios = cadena1.replace(" ", "")
    sin_espacios = sin_espacios.lower()
    lista1 = list(sin_espacios)
    sin_espacios = cadena2.replace(" ", "")
    sin_espacios = sin_espacios.lower()
    lista2 = list(sin_espacios)
    cantidad_de_coincidencias = 0
    cantidad_de_letras = 0
    errores = 0
    for letra_2 in lista2:
        cantidad_de_letras = cantidad_de_letras + 1
    for letra in lista1:
        try:       
            lista2.index(letra)
            lista2.remove(letra)
            cantidad_de_coincidencias = cantidad_de_coincidencias + 1
        except ValueError:
            errores = errores + 1
            print(f"--> Cantidad de errores: {errores}")
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