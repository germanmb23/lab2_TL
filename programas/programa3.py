# -*- coding: utf-8 -*-
import string
import sys
import io
import nltk
import re
from nltk.tree import Tree

def tokenize(text):
	return list(text)


def parse(s):
	grammar = """

	S -> '{' A '}'

	A -> '"' P '"' ':' S | '"' P '"' ':' S ',' A | '"' P '"' ':' '"' P '"' ',' A | '"' P '"' ':' N  ',' A | '"' P '"' ':' '"' P '"' | '"' P '"' ':' N 

	N -> N '0' | N '1' | N '2' | N '3' | N '4' | N '5' | N '6' | N '7' | N '8' | N '9' | '0' |'1' | '3' | '2' | '4' | '5' | '6' | '7' | '8' | '9'

	"""

	#Agrego los caracteres
	grammar += "P ->" 

	for char in string.ascii_lowercase:
		grammar += " P '" + char + "'|"
		grammar +=  " '" + char + "' |"

	for char in string.ascii_uppercase:
		grammar += " P '" + char + "' |"
		grammar +=  " '" + char + "' |"
	

	grammar += " P '_' | '_'"

	grammar = nltk.CFG.fromstring(grammar)
	s_tok = tokenize(s.strip())
	parser = nltk.LeftCornerChartParser(grammar)
	tree = [t for t in parser.parse(s_tok)][:1]
	return tree
	
def espacio(y):
	espacio = ''
	for i in range(0,y):
		espacio += '    '
	return espacio

def jsontoyaml(tree, n):
	resultado=""
	for subtree in tree:
		if type(subtree) == Tree:
			if(subtree.label()=="S"):
				resultado=resultado+jsontoyaml(subtree, n+1)
			else:
				resultado=resultado+jsontoyaml(subtree, n)
                
		else:
			if(subtree=='{' or subtree==','):
				ident = espacio(n)
				if n != 0:
					resultado += '\n' + ident
				else:
					if subtree != '{':
						resultado += '\n'
			else:
				if(subtree!='}' and subtree!='"'):
					resultado=resultado+subtree
				if(subtree==":"):
					resultado += ' '
	return resultado
	
	
if __name__ == '__main__':
	archivo_entrada = sys.argv[1]
	archivo_salida = sys.argv[2]
	f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
	s = f.read()  
	f.close() 
  
	try:
	  tree = parse(s)
	  if tree:
		  salida = jsontoyaml(tree, -1)
	  else:
		  salida = "NO PERTENECE"
	except ValueError:
	  salida = "NO CUBRE"
	
	#print(salida)
	
	f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
	f.write(salida)
	f.close()


