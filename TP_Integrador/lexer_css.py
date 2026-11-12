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
    'BS': 'BORDER_STYLE',
    'BC': 'BORDER_COLOR',
    'TA': 'TEXT_ALIGN',
    'TD': 'TEXT_DECORATION',
    'TDC': 'TEXT_DECORATION_COLOR',
    'TDS': 'TEXT_DECORATION_STYLE',
    'PD': 'PADDING',
    'MG': 'MARGIN',
    'FS': 'FONT_SIZE',
    'rojo': 'RED',
    'azul': 'BLUE',
    'amarillo': 'YELLOW',
    'verde': 'GREEN',
    'carmesi': 'CRIMSON',
    'naranja': 'ORANGE',
    'violeta': 'VIOLET',
    'indigo': 'INDIGO',
    'celeste': 'SKYBLUE',
    'blanco': 'WHITE',
    'negro': 'BLACK',
    'gris': 'GREY',
    'izquierda': 'LEFT',
    'centrado': 'CENTER',
    'derecha': 'RIGHT',
    'justificado': 'JUSTIFY',
    'arriba': 'OVERLINE',
    'abajo': 'UNDERLINE',
    'tachado': 'LINE_THROUGH',
    'solido': 'SOLID',
    'doble': 'DOUBLE',
    'punteado': 'DOTTED',
    'trazas': 'DASHED',
    'ondulado': 'WAVY'
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

t_EQUALS = r'\:'

t_AND = r'\,'

t_START = r'\('

t_END = r'\)'

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
