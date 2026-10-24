import subprocess
from pathlib import Path

'Se eliminan Tabulaciones, Saltos de Linea y Espacios en cada Test'

def test_caso1():
    'Prueba de Formato HEX en colorest'
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
                .div{
                    color: #FF0000;
                    background-color: #000000;
                }
                '''
    
    assert actual.replace('\n', '').replace(' ', '').replace('\t', '') == esperado.replace('\n', '').replace(' ', '').replace('\t', '')