import subprocess
from pathlib import Path

'Se eliminan Tabulaciones, Saltos de Linea y Espacios en cada Test'

def test_caso1():
    'Prueba 1: Formato HEX en colores'
    txt_file = Path("TP_Integrador/test/caso1.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso1.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                div{
                    color: #ff0000;
                    color: #0000ff;
                    color: #ffff00;
                    color: #ffffff;
                    color: #000000;
                    color: #808080;
                    color: #008000;
                    color: #4b0082;
                    color: #ee82ee;
                    color: #dc143c;
                    color: #ffa500;
                    color: #87ceeb;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso2():
    'Prueba 2: Alineación Texto'
    txt_file = Path("TP_Integrador/test/caso2.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso2.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                    div{
                        text-align: left;
                        text-align: center;
                        text-align: right;
                        text-align: justify;
                    }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso3():
    'Prueba 3'
    txt_file = Path("TP_Integrador/test/caso3.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso3.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                div{
                    text-decoration: underline;
                    text-decoration: overline;
                    text-decoration: line-through;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso4():
    'Prueba 4 - Estilos Bordes y Decoradores'
    txt_file = Path("TP_Integrador/test/caso4.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso4.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                div{
                    text-decoration-style: solid;
                    text-decoration-style: double;
                    text-decoration-style: dotted;
                    text-decoration-style: dashed;
                    text-decoration-style: wavy;
                }
                div{
                    border-style: solid;
                    border-style: double;
                    border-style: dotted;
                    border-style: dashed;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso5():
    'Prueba 5 - Clases e Ids'
    txt_file = Path("TP_Integrador/test/caso5.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso5.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                #Elemento1{
                    color: #0000ff;
                }
                .Elemento2{
                    color: #0000ff;
                }
                .Elemento3{
                    color: #0000ff;
                }
                #Elemento4{
                    color: #0000ff;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso6():
    'Prueba 6 - Elementos de HTML'
    txt_file = Path("TP_Integrador/test/caso6.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso6.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                body{
                    color: #808080;
                }
                header{
                    color: #808080;
                }
                nav{
                    color: #808080;
                }
                section{
                    color: #808080;
                }
                article{
                    color: #808080;
                }
                aside{
                    color: #808080;
                }
                footer{
                    color: #808080;
                }
                div{
                    color: #808080;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso7():
    'Prueba 7 - Propiedades'
    txt_file = Path("TP_Integrador/test/caso7.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso7.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                div{
                    color: #ff0000;
                    background-color: #ffffff;
                    border-color: #ff0000;
                    border-style: double;
                    text-align: justify;
                    text-decoration: underline;
                    text-decoration-color: #008000;
                    text-decoration-style: double;
                    padding: 15px;
                    margin: 15px;
                    font-size: 25px;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso8():
    'Prueba 8 - Caso de Uso 1'
    txt_file = Path("TP_Integrador/test/caso8.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso8.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                #Contenedor{
                    color: #ff0000;
                    background-color: #ffffff;
                    border-color: #ff0000;
                    border-style: double;
                    padding: 10px;
                    margin: 10px;
                }
                .Elemento{
                    text-align: justify;
                    text-decoration: underline;
                    text-decoration-color: #008000;
                    text-decoration-style: double;
                    font-size: 40px;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso9():
    'Prueba 9 - Caso de Uso 2'
    txt_file = Path("TP_Integrador/test/caso9.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso9.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                #Elemento3{
                        color: #000000;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')

def test_caso10():
    'Prueba 10 - Caso de Uso 3'
    txt_file = Path("TP_Integrador/test/caso10.txt")

    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(txt_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path('TP_Integrador/test/caso10.txt.css')

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                .contenedor{
                    color: #ff0000;
                    background-color: #000000;
                }
                nav{
                    text-align: center;
                    text-decoration: underline;
                }
                '''

    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')
