import sys
from lexer_css import lexer
from parser_css import parser, css

archivo_ruta = sys.argv[1]
with open(archivo_ruta, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

parser.parse(contenido)

with open(f'{sys.argv[1]}.css', 'w', encoding='utf-8') as archivo_out:
    for linea in css:
        if 'Error Sintáctico' in css:
            archivo_out.write('/*Error Sintáctico*/')
            print('Error Sintáctico')
        else:
            print(linea)
            archivo_out.write(linea + '\n')      
    archivo_out.close()
