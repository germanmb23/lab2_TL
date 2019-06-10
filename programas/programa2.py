# -*- coding: utf-8 -*-

import sys
import io
import nltk


def tokenize(text):
    return list(text)


def parse(s):
    grammar = """
    S -> '(' S ')' | S '+' S | S '*' S | N 

    N -> N '0' | N '1' | N '2' | N '3' | N '4' | N '5' | N '6' | N '7' | N '8' | N '9' | '1' | '3' | '2' | '4' | '5' | '6' | '7' | '8' | '9'

    """
    grammar = nltk.CFG.fromstring(grammar)
    s_tok = tokenize(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = [t for t in parser.parse(s_tok)][:1]
    return tree


if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()  
    f.close()
    
    #s = '(12*(9+(115*12)))+(10+5)'
    # ejemplos
    # entrada7 = '7*(45+16)' -> (16+45)*7
    # entrada8 = '7+(45*)' -> NO PERTENECE
    # entrada9 = '(12*(9+(115*12)))+(10+5)' -> (5+10)+(((12*115)+9)*12)
      
  
    try:
      tree = parse(s)
      if tree:
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    #print(salida)
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()


