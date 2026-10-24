import ply.lex as lex

keywords = {
    'id': 'ID',
    'clase': 'CLASS',
    'BD': 'BODY',
    'HD': 'HEADER',
    'NV': 'NAV',
    'ST': 'SECTION',
    'AR': 'ARTICLE',
    'AS': 'ASIDE',
    'FT': 'FOOTER',
    'DV': 'DIV',
    'CO': 'COLOR',
    'BK': 'BACKGROUND_COLOR',
    'TA': 'TEXT_ALIGNMENT',
    'PD': 'PADDING',
    'MG': 'MARGIN',
    'FS': 'FONT_SIZE',
    'rojo': 'RED',
    'azul': 'BLUE',
    'verde': 'GREEN',
    'amarillo': 'YELLOW',
    'blanco': 'WHITE',
    'negro': 'BLACK',
    'izquierda': 'LEFT',
    'centrado': 'CENTER',
    'derecha': 'RIGHT',
    'justificado': 'JUSTIFY'
}

tokens = (
    'TEXT',
    'EQUALS',
    'AND', 
    'START',
    'END',
    'VALUE'
) + tuple(keywords.values())

def t_TEXT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'TEXT') 
    t.value = t.value.strip()
    return t

def t_ID(t):
    r'id'
    return t

def t_CLASS(t):
    r'clase'
    return t

def t_BODY(t):
    r'BD'
    return t

def t_HEADER(t):
    r'HD'
    return t

def t_NAV(t):
    r'NV'
    return t

def t_SECTION(t):
    r'ST'
    return t

def t_ARTICLE(t):
    r'AR'
    return t

def t_ASIDE(t):
    r'AS'
    return t

def t_FOOTER(t):
    r'FT'
    return t

def t_DIV(t):
    r'DV'
    return t

def t_COLOR(t):
    r'CO'
    return t

def t_BACKGROUND_COLOR(t):
    r'BK'
    return t

def t_TEXT_ALIGNMENT(t):
    r'TA'
    return t

def t_PADDING(t):
    r'PD'
    return t

def t_MARGIN(t):
    r'MG'
    return t

def t_FONT_SIZE(t):
    r'FS'
    return t

t_EQUALS = r'\:'

t_AND = r'\,'

t_START = r'\('

t_END = r'\)'

def t_RED(t):
    r'rojo'
    return t

def t_BLUE(t):
    r'azul'
    return t

def t_GREEN(t):
    r'verde'
    return t

def t_YELLOW(t):
    r'amarillo'
    return t

def t_WHITE(t):
    r'blanco'
    return t
    
def t_BLACK(t):
    r'negro'
    return t
    
def t_LEFT(t):
    r'izq'
    return t
    
def t_CENTER(t):
    r'cen'
    return t

def t_RIGHT(t):
    r'der'
    return t

def t_JUSTIFY(t):
    r'jus'
    return t

def t_VALUE(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()