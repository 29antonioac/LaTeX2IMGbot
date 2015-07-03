#!/usr/bin/env python

# LaTeX2GIF transforma usando un editor web una expresión LaTeX a un archivo GIF.

import sys
from urllib.parse import quote
from urllib.request import urlopen

def main(argumentos):

    if len(argumentos) < 4:
        expresion = input("Introduce expresión LaTeX: ")
        nombre_archivo = input("Introduce nombre del archivo resultante: ")
        extension = input("Introduce la extensión deseada (gif,png,pdf,swf,emf,svg): ")
    else:
        expresion = argumentos[1]
        nombre_archivo = argumentos[2]
        extension = argumentos[3]

    if extension not in ("gif","png","pdf","swf","emf","svg"):
        print("La extensión no está entre las soportadas, saliendo...")
        sys.exit(-1)

    # Preparamos las cadenas de texto
    servidor = "http://latex.codecogs.com/" + extension + ".download?"
    nombre_archivo = nombre_archivo + "." + extension
    tamanio = "%5Cdpi%7B300%7D%20"

    # Transformamos la expresión para quitar caracteres extraños en la URL
    expresion = quote(expresion)
    url = servidor + tamanio + expresion
    # print("Descargando desde",url)

    # Descarga el fichero desde url y lo guarda como nombre_archivo:
    with urlopen(url) as respuesta, open(nombre_archivo, 'wb') as fichero_salida:
        datos = respuesta.read()        # Un objeto "bytes"
        fichero_salida.write(datos)     # Se escribe en disco

    print("Descargado como",nombre_archivo)

if __name__ == "__main__":
    main(sys.argv)
