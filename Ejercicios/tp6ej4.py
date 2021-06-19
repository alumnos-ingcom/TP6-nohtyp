################
# Nohtyp
# Mauricio Boyé - @MauriBoye
# Facundo Bistevins - @FacuBiste
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°4
"""
import tp6ej1

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para archivos inexistentes"""
    pass 

def codificador(texto_base, rotado):
    """
    Esta funcion devuelve un archivo nuevo con el texto cifrado
    de otro archivo.
    """
    texto = texto_base + ".txt"
    try:
        with open(texto, "r", 1, "utf-8") as cifrado:
            nombre_final = texto_base + ".cesar.txt"
            with open(nombre_final, "x", 1, "utf-8") as final:
                for texto in cifrado.readlines():
                    texto_cifrado = []
                    texto_cifrado_caracteres = ""
                    i = 0
                    while i < (len(texto)-1):
                        if (ord(texto[i])+int(rotado)) <= ord("z"):
                            texto_cifrado.append(ord(texto[i])+int(rotado))
                            texto_cifrado_caracteres = texto_cifrado_caracteres + (chr(texto_cifrado[i]))
                        if (ord(texto[i])+int(rotado)) > ord("z"):
                            texto_cifrado.append(ord(texto[i])+int(rotado)-(ord("z")-ord("@")))
                            texto_cifrado_caracteres = texto_cifrado_caracteres + (chr(texto_cifrado[i]))
                        i = i + 1
                    final.write(str(texto_cifrado_caracteres))
                    final.write("\n")
    except FileNotFoundError as err:
        raise IngresoIncorrecto(f"'{texto}' no existe") from err
        
def principal():
    tp6ej1.marco("codificador()")
    texto_base = input("Ingrese el nombre del archivo de entrada: ")
    rotado = input("Ingrese la cantidad de caracteres rotados: ")
    codificador(texto_base, rotado)

if __name__ == "__main__":
    principal()