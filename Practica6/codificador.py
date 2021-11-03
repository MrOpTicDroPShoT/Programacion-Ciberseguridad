import base64 as b64
import sys
def codificador(ubicacion):
    with open(ubicacion,"r") as f:
        archivo_resultado = open ("texto codificado","w")
        texto_sin_codificar = f.read()

        texto_codificado=b64.b64encode(bytes(texto_sin_codificar, "UTF-8"))
        print("El texto codificado es:", (texto_codificado))

        texto_decodificado=b64.b64decode(texto_codificado)
        print("El texto decodificado es:",(texto_decodificado))

        archivo_resultado.write(str(texto_codificado) + "\n")
        archivo_resultado.write(str(texto_decodificado) + "\n")
        archivo_resultado.close()
        f.close()

ubicacion = sys.argv[1]
codificador(ubicacion)
