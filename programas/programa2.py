# -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk.tree import Tree

def tokenize(text):
    return list(text)

def parse(s):
    grammar = """
    S ->'(' S ')' | S '*' S | S '+' S | NUM
    NUM -> '0' |'1' | '2' | '3' |'4' | '5' | '6' | '7' | '8' | '9' | '0' NUM | '1' NUM | '2' NUM | '3' NUM | '4' NUM | '5' NUM | '6' NUM | '7' NUM | '8' NUM | '9' NUM 
    """        
    grammar = nltk.CFG.fromstring(grammar)
    s_tok = tokenize(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree=[t for t in parser.parse(s_tok)][:1]
    return tree

def recorrer(tree):
    resultado=""
    for subtree in tree:
        if type(subtree) == Tree:
            if(subtree.label()=="S"):
                resultado=recorrer(subtree)+resultado
            else:
                resultado=resultado+recorrer(subtree)
                
        else:
            if(subtree=="("):
                subtree=")"
            else:
                if(subtree==")"):
                    subtree="("  
            resultado=subtree+resultado
    return resultado


if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s)
      resultado=recorrer(tree)
      if tree:
          salida = resultado
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()