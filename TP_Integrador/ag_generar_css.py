import ollama

def generar_css(propiedad, valor):
    respuesta = ollama.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': f''' 
                Devuelve únicamente codigo en formato CSS. 
                Sin explicaciones. 
                Sin markdown. 
                Sin texto adicional. 
                Si es un valor númerico agregale la unidad de medida correspondiente a la propiedad.
                Si es un color adaptalo a HEX.
                Adapta al formato del lenguaje CSS la propiedad {propiedad} y el valor: {valor}.
                Coloca ';' al final.
                '''
            }
        ]
    )

    return respuesta['message']['content']