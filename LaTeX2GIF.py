#!/usr/bin/env python

# LaTeX2GIF transforma usando un editor web una expresión LaTeX a un archivo GIF.

import sys
from urllib.parse import quote
from urllib.request import urlopen

def main(argumentos):

    if len(argumentos) < 3:
        expresion = input("Introduce expresión LaTeX: ")
        nombre_archivo = input("Introduce nombre del archivo resultante: ")
    else:
        expresion = sys.argv[1]
        nombre_archivo = sys.argv[2]

    # Preparamos las cadenas de texto
    servidor = "http://latex.codecogs.com/gif.download?"
    nombre_archivo = nombre_archivo + ".gif"

    # Transformamos la expresión para quitar caracteres extraños en la URL
    expresion = quote(expresion)
    url = servidor + expresion
    # print("Descargando desde",url)

    # Descarga el fichero desde url y lo guarda como nombre_archivo:
    with urlopen(url) as respuesta, open(nombre_archivo, 'wb') as fichero_salida:
        datos = respuesta.read()        # Un objeto "bytes"
        fichero_salida.write(datos)     # Se escribe en disco

    print("Descargado como",nombre_archivo)

if __name__ == "__main__":
    main(sys.argv)
