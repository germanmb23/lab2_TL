# -*- coding: utf-8 -*-

import sys
import io
import nltk
import re

def tokenize(text):
    return list(text)


def parse(s):
    grammar = """

 	S -> '{' A '}'

    A -> '"' P '"' ':' S | '"' P '"' ':' S ',' A | '"' P '"' ':' '"' P '"' ',' A | '"' P '"' ':' N  ',' A | '"' P '"' ':' '"' P '"' | '"' P '"' ':' N 

	P -> P 'a' | P 's' | P 'd' | 'a' | 's' | 'd'

    N -> N '0' | N '1' | N '2' | N '3' | N '4' | N '5' | N '6' | N '7' | N '8' | N '9' | '0' |'1' | '3' | '2' | '4' | '5' | '6' | '7' | '8' | '9'

    """
    grammar = nltk.CFG.fromstring(grammar)
    s_tok = tokenize(s.strip())
	#BottomUpLeftCornerChartParser
    parser = nltk.LeftCornerChartParser(grammar)
    # parser = nltk.LeftCornerChartParser(grammar)
    tree = [t for t in parser.parse(s_tok)][:1]
    return tree


if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()  
    f.close()
    
    
    # ejemplos
    #entrada7 = '{"s":"s","as":255,"as":0,"as":0}' #-> PERTENECE
    #entrada8 = '{"sd":{"as":{"as":255,"s":0,"s":0},"as":{"s":0,"as":0,"s":255}}}' #-> PERTENECE
    #entrada9 = '{"asd":"asd","a:255}' #-> NO PERTENECE
    #s = entrada8  
  
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


