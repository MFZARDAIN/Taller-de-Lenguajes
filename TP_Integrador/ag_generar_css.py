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
                Si es un color adaptalo a HEX.
                Genera la propiedad {propiedad} y adapta el valor: {valor} al formato del lenguaje CSS.
                Coloca ';' al final.
                '''
            }
        ]
    )

    return respuesta['message']['content']