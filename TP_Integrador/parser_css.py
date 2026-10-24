import ply.yacc as yacc
from lexer_css import tokens
from ag_generar_css import generar_css

css = []

def p_lista_sentencias(t):
    '''
    sentencias  :   sentencias sentencia
                |   sentencia
    '''
    if len(t) == 3:
        t[0] = t[1] + '\n' + t[2]
    else:
        t[0] = t[1]
    css.clear()
    css.append(t[0])

def p_sentencia(t):
    '''
    sentencia   :   elemento
                |   CLASS elemento
                |   ID elemento
    '''
    if t[1] == 'clase' :
        t[0] = "." + t[2]
    elif t[1] == 'id' :
        t[0] = "#" + t[2]
    else:
        t[0] = t[1]
    pass

def p_elemento_selector(t):
    '''
    elemento    :   BODY START propiedades END
                |   HEADER START propiedades END
                |   NAV START propiedades END
                |   SECTION START propiedades END
                |   ARTICLE START propiedades END
                |   ASIDE START propiedades END
                |   FOOTER START propiedades END
                |   DIV START propiedades END
    '''
    selectores = {
        'BD': 'body', 'HD': 'header', 'NV': 'nav', 'ST': 'section',
        'AR': 'article', 'AS': 'aside', 'FT': 'footer', 'DV': 'div'
    }
    
    selector_real = selectores.get(t[1], t[1].lower())
    t[0] = f"{selector_real}{{\n{t[3]}\n}}"

def p_elemento_texto(t):
    'elemento   :   TEXT START propiedades END'
    t[0] = f"{t[1]}{{\n{t[3]}\n}}"


def p_propiedades(t):
    '''
    propiedades :   propiedad AND propiedades
                |   propiedad
    '''
    if len(t) == 4:
        t[0] = t[1] + '\n' + t[3]
    else:
        t[0] = t[1]
    pass

def p_propiedad_color(t):
    '''
    propiedad   :   COLOR EQUALS RED
                |   COLOR EQUALS BLUE
                |   COLOR EQUALS GREEN
                |   COLOR EQUALS YELLOW
                |   COLOR EQUALS WHITE
                |   COLOR EQUALS BLACK
    '''
    cod = generar_css('color', t[3])
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_fondo(t):
    '''
    propiedad   :   BACKGROUND_COLOR EQUALS RED
                |   BACKGROUND_COLOR EQUALS BLUE
                |   BACKGROUND_COLOR EQUALS GREEN
                |   BACKGROUND_COLOR EQUALS YELLOW
                |   BACKGROUND_COLOR EQUALS WHITE
                |   BACKGROUND_COLOR EQUALS BLACK
    '''
    cod = generar_css('background-color', t[3])
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_alineacion(t):
    '''
    propiedad   :   TEXT_ALIGNMENT EQUALS LEFT
                |   TEXT_ALIGNMENT EQUALS CENTER
                |   TEXT_ALIGNMENT EQUALS RIGHT
                |   TEXT_ALIGNMENT EQUALS JUSTIFY
    '''
    cod = generar_css('text-alignment', t[3])
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_padding(t):
    'propiedad  :   PADDING EQUALS VALUE'
    cod = generar_css('padding', t[3])
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_margin(t):
    'propiedad  :   MARGIN EQUALS VALUE'
    cod = generar_css('margin', t[3])
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_tamaño_texto(t):
    'propiedad  :   FONT_SIZE EQUALS VALUE'
    cod = generar_css('font-size', t[3])
    t[0] = f"\t{cod.strip()}"
    pass

def p_error(t):
    css.append('Error Sintáctico')

parser = yacc.yacc(debug=1)