################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# funcion de cesar y generador de archivo de texto aleatorio

import random

def texto_generator(cantidad_de_palabras):
    """
    esta funcion genera un archivo con texto aleatorio en base a las palabras
    y conectores que tiene, si le quieren agregar cualquier cosa ahi dice como
    """
    texto = [] 
    
    palabras = ["casa", "lugar", "verde", "rojo", "caminando", "explorar", "patio", "calle","sistema","auto",
                "color","azul","juguete","jamon","gato","queso","para","que","supuestamente", "nunca","sera","siempre"]
                # 1) las palabras o conectores se agregan a la lista, separado con comoma del resto y entre comillas
                # 2) el segundo paso es, mas abajo "busquen el siguiente comentario"
    conectores = ["de", "el", "la", "en", "por", "es", "sera", "sos", "la", "tu", "mi",
                   "del","que","nosotros","ellos","vos","para", "cuando","nunca"]
    
    cantidad_de_palabras -= 1
    
    palabras_del_texto = 0
    
    while cantidad_de_palabras > 0:
        
        palabras_del_texto += 1
        
        if palabras_del_texto > 10:
            
            texto.append("\n")
            
            palabras_del_texto = 0
            
        else:
            
            texto.append(palabras[random.randint(-22,21)]) # aca, en (-x,y) le suman a cada valor la -
                                                           # cantidad de palabras que agregaron
                                                           # EJ: agregaron 2 palabras, bueno. de (-23,22)
                                                           #  pasa a ser (-25,22)
        
            texto.append(conectores[random.randint(-19,18)]) # y aca lo mismo
        
            cantidad_de_palabras -= 1
        
    texto.append(palabras[random.randint(-11,10)])
    
    texto_final = " ".join(texto)
        
    return texto_final

def codificador(texto, cantidad):
    
    cantidad = abs(cantidad)
    
    texto_ingresado = list(texto)
    
    armando_texto = []
    
    
    
    if cantidad > 26:
        
        while cantidad > 26:
            cantidad -= 26
            
    minus = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    mayus = list("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    pocicion = 0
    
    pocicion_final = 0
    
    for letra in texto_ingresado:
        
        if letra.islower():
           
            pocicion = minus.index(letra)
            pocicion_final = pocicion + cantidad 
            armando_texto.append(minus[pocicion_final])
            
        elif letra.isupper():
            pocicion = mayus.index(letra)
            pocicion_final = pocicion + cantidad 
            armando_texto.append(mayus[pocicion_final])
            
        elif letra == " ":
            armando_texto.append(" ")
            
        elif letra.isdigit():
        
            letra = int(letra)
            letra = letra + cantidad
            
            while letra > 9:
                letra -= 10
            letra = str(letra)
            armando_texto.append(letra)
            
        else:
            armando_texto.append(letra)
            
    palabra_codificada = "".join(armando_texto)
    
    return palabra_codificada

def ingreso_entero(mensaje):
    validante = True
    print(mensaje)
    while validante:
        try:
            numero = int(input())
            validante = False
        except ValueError:
            print(f"error, por favor {mensaje}")
            
    return numero
