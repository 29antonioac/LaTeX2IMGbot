#!/usr/bin/env python3

# LaTeX2IMG transforma usando un editor web una expresión LaTeX a una imagen.

import sys
import os
from PIL import Image, ImageOps
from urllib.parse import quote
from urllib.request import urlopen

def img2webp(rutaImagen):
    file, ext = os.path.splitext(rutaImagen)
    im = Image.open(rutaImagen).convert("RGBA")
    im = ImageOps.expand(im,75)
    im.save(file + ".webp", "WEBP")
    os.remove(rutaImagen)

def main(argumentos):
    webp = False

    if len(argumentos) < 4:
        expresion = input("Introduce expresión LaTeX: ")
        nombre_archivo = input("Introduce nombre del archivo resultante: ")
        extension = input("Introduce la extensión deseada (gif,png,pdf,swf,emf,svg,webp): ")
    else:
        expresion = argumentos[1]
        nombre_archivo = argumentos[2]
        extension = argumentos[3]

    if extension not in ("gif","png","pdf","swf","emf","svg","webp"):
        print("La extensión no está entre las soportadas, saliendo...")
        sys.exit(-1)

    if extension == "webp":
        webp = True
        extension = "png"

    # Preparamos las cadenas de texto
    servidor = "http://latex.codecogs.com/" + extension + ".download?"
    nombre_archivo_completo = nombre_archivo + "." + extension
    tamanio = "%5Cdpi%7B300%7D%20"

    # Transformamos la expresión para quitar caracteres extraños en la URL
    expresion = quote(expresion)
    url = servidor + tamanio + expresion
    # print("Descargando desde",url)

    # Descarga el fichero desde url y lo guarda como nombre_archivo:
    with urlopen(url) as respuesta, open(nombre_archivo_completo, 'wb') as fichero_salida:
        datos = respuesta.read()        # Un objeto "bytes"
        fichero_salida.write(datos)     # Se escribe en disco

    if webp:
        img2webp(nombre_archivo_completo)
        extension = "webp"

    # Si llamo a LaTeX2IMG como módulo, no imprimir nada
    if __name__ == "__main__":
        print("Descargado como",nombre_archivo + "." + extension)

if __name__ == "__main__":
    main(sys.argv)
