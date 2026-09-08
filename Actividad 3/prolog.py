import janus_swi as janus

#Los comentarios empiezan con el símbolo %
#Las constantes y predicados empiezan con minúsculas
#Los hechos acaban en punto
#Las variables inician con mayúsculas

janus.consult('lógica proposicional', '''
    conexion(or).
    conexion(and).
    conexion(then).
    const(f).
    const(v).
    vari(p).
    vari(q).
    vari(r).
    vari(s).
    expresion(X) :- const(X).
    expresion(X) :- vari(X).
    expresion([neg, Y]) :- expresion(Y).
    expresion([A, C, B]) :- expresion(A), conexion(C), expresion(B).
''')

# p & (q -> ¬r)
list(janus.query('expresion( [p, and, [q, then, [neg, r]]]).'))