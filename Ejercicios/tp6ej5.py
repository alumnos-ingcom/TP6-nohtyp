################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp6ej1, tp6ej4

def descodificador(texto_base, rotado):
    """
    Esta funcion devuelve un archivo nuevo con el texto descifrado
    de otro archivo.
    """
    if ".cesar" in texto_base: 
        texto = texto_base + ".txt"
        try:
            with open(texto, "r", 1, "utf-8") as cifrado:
                nombre_final = texto_base + ".decode.txt"
                with open(nombre_final, "x", 1, "utf-8") as final:
                    for texto in cifrado.readlines():
                        texto_descifrado = ""
                        texto_descifrado_unicode = []                    
                        i = 0
                        while i < (len(texto)-1):
                            if (ord(texto[i])-int(rotado)) == ord(" "):
                                texto_descifrado = texto_descifrado + " "
                            elif (ord(texto[i])-int(rotado)) < int(ord("A")):
                                texto_descifrado = texto_descifrado + chr((ord(texto[i])-int(rotado)+(ord("z")-ord("@"))))
                                texto_descifrado_unicode.append(ord(texto_descifrado[i]))
                            elif (ord(texto[i])-int(rotado)) >= int(ord("A")):
                                texto_descifrado = texto_descifrado + chr((ord(texto[i])-int(rotado)))
                                texto_descifrado_unicode.append(ord(texto_descifrado[i]))
                            i = i + 1
                        final.write(str(texto_descifrado))
                        final.write("\n")
        except FileNotFoundError as err:
            raise tp6ej4.IngresoIncorrecto(f"'{texto}' no existe") from err
    else:
        raise tp6ej4.IngresoIncorrecto(f"'{texto_base}' debe ser un archivo codificado '.cesar'")

def principal():
    tp6ej1.marco("descodificador()")
    texto_base = input("Ingrese el nombre del archivo de entrada: ")
    rotado = input("Ingrese la cantidad de caracteres desrotados: ")
    descodificador(texto_base, rotado)
    print(f"\nEl nombre del nuevo archivo descodificado es: '{texto_base}.decode.txt'")

if __name__ == "__main__":
    principal()