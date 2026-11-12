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
    sentencia   :   selector
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
    selector    :   BODY START propiedades END
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

    cod = selectores.get(t[1], t[1].lower())
    t[0] = f"{cod}{{\n{t[3]}\n}}"

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

def p_propiedad_color_texto(t):
    '''
    propiedad   :   COLOR EQUALS RED
                |   COLOR EQUALS BLUE
                |   COLOR EQUALS YELLOW
                |   COLOR EQUALS GREEN
                |   COLOR EQUALS CRIMSON
                |   COLOR EQUALS ORANGE
                |   COLOR EQUALS SKYBLUE
                |   COLOR EQUALS INDIGO
                |   COLOR EQUALS VIOLET
                |   COLOR EQUALS WHITE
                |   COLOR EQUALS BLACK
                |   COLOR EQUALS GREY
    '''
    cod = generar_css('color', t[3]).lower()
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_fondo(t):
    '''
    propiedad   :   BACKGROUND_COLOR EQUALS RED
                |   BACKGROUND_COLOR EQUALS BLUE
                |   BACKGROUND_COLOR EQUALS YELLOW
                |   BACKGROUND_COLOR EQUALS GREEN
                |   BACKGROUND_COLOR EQUALS CRIMSON
                |   BACKGROUND_COLOR EQUALS ORANGE
                |   BACKGROUND_COLOR EQUALS INDIGO
                |   BACKGROUND_COLOR EQUALS VIOLET
                |   BACKGROUND_COLOR EQUALS SKYBLUE
                |   BACKGROUND_COLOR EQUALS WHITE
                |   BACKGROUND_COLOR EQUALS BLACK
                |   BACKGROUND_COLOR EQUALS GREY
    '''
    cod = generar_css('background-color', t[3]).lower()
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_estilo_borde(t):
    '''
    propiedad   :   BORDER_STYLE EQUALS SOLID
                |   BORDER_STYLE EQUALS DOUBLE
                |   BORDER_STYLE EQUALS DOTTED
                |   BORDER_STYLE EQUALS DASHED
    '''
    cod = generar_css('border-style', t[3]).lower()
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_color_borde(t):
    '''
    propiedad   :   BORDER_COLOR EQUALS RED
                |   BORDER_COLOR EQUALS BLUE
                |   BORDER_COLOR EQUALS YELLOW
                |   BORDER_COLOR EQUALS GREEN
                |   BORDER_COLOR EQUALS CRIMSON
                |   BORDER_COLOR EQUALS ORANGE
                |   BORDER_COLOR EQUALS SKYBLUE
                |   BORDER_COLOR EQUALS INDIGO
                |   BORDER_COLOR EQUALS VIOLET
                |   BORDER_COLOR EQUALS WHITE
                |   BORDER_COLOR EQUALS BLACK
                |   BORDER_COLOR EQUALS GREY
    '''
    cod = generar_css('border-color', t[3]).lower()
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_alineacion(t):
    '''
    propiedad   :   TEXT_ALIGN EQUALS LEFT
                |   TEXT_ALIGN EQUALS CENTER
                |   TEXT_ALIGN EQUALS RIGHT
                |   TEXT_ALIGN EQUALS JUSTIFY
    '''
    cod = generar_css('text-align', t[3])
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_decorador(t):
    '''
    propiedad   :   TEXT_DECORATION EQUALS OVERLINE
                |   TEXT_DECORATION EQUALS UNDERLINE
                |   TEXT_DECORATION EQUALS LINE_THROUGH
    '''
    cod = generar_css('text-decoration', t[3])
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_estilo_decorador(t):
    '''
    propiedad   :   TEXT_DECORATION_STYLE EQUALS SOLID
                |   TEXT_DECORATION_STYLE EQUALS DOUBLE
                |   TEXT_DECORATION_STYLE EQUALS DOTTED
                |   TEXT_DECORATION_STYLE EQUALS DASHED
                |   TEXT_DECORATION_STYLE EQUALS WAVY
    '''
    cod = generar_css('text-decoration-style', t[3]).lower()
    t[0] = f"\t{cod.strip()}"
    pass

def p_propiedad_color_decorador(t):
    '''
    propiedad   :   TEXT_DECORATION_COLOR EQUALS RED
                |   TEXT_DECORATION_COLOR EQUALS BLUE
                |   TEXT_DECORATION_COLOR EQUALS YELLOW
                |   TEXT_DECORATION_COLOR EQUALS GREEN
                |   TEXT_DECORATION_COLOR EQUALS CRIMSON
                |   TEXT_DECORATION_COLOR EQUALS ORANGE
                |   TEXT_DECORATION_COLOR EQUALS SKYBLUE
                |   TEXT_DECORATION_COLOR EQUALS INDIGO
                |   TEXT_DECORATION_COLOR EQUALS VIOLET
                |   TEXT_DECORATION_COLOR EQUALS WHITE
                |   TEXT_DECORATION_COLOR EQUALS BLACK
                |   TEXT_DECORATION_COLOR EQUALS GREY
    '''
    cod = generar_css('text-decoration-color', t[3]).lower()
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
    pass

parser = yacc.yacc()
