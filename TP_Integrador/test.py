import subprocess
from pathlib import Path

def test_caso1():
    md_file = Path("test/caso1.md")
    
    resultado = subprocess.run(
        ['python', 'TP_Integrador/main.py', str(md_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    css_generado = Path("test/caso1.md.html")

    assert css_generado.exists()

    actual = css_generado.read_text(encoding="utf-8")
    esperado = '''
                .div{
                    color: red;
                    background-color: black;
                }
                '''
    
    assert actual.replace('\n', '').replace(' ', '') == esperado.replace('\n', '').replace(' ', '')