import ply.lex as lex
import re
from ply.lex import TOKEN

fuente = open("shadow", "r")
salida = open("salida.txt", "w")

data = fuente.read()
fechas = set(data.split('\n'))

# lista de tokens
tokens = (
    'SIGNO_PESO',#signo de $
    'NUM',#digito
    'HASH',#hash completo
    'EXTRA'#es lo que hay despues del $, alfanumerico
)

# Regular expression rules for simple tokens
t_SIGNO_PESO = r'\$'
NUM = r'\d+'
EXTRA=r'[A-Z,a-z,0-9,/,.,:]*' #se uso cerradura de Kleene

HASH = t_SIGNO_PESO+NUM+t_SIGNO_PESO+EXTRA+t_SIGNO_PESO+EXTRA #combinacion $numero$caracteres alfanumericos

#Definimos hash como token
@TOKEN(HASH)
def t_HASH(t):
    t.value = str(t.value)
    return t

# Ignorar el salto de linea
t_ignore = ' \n'


#QUE HACE EN CASO DE ERROR, EN ESTE CASO SE SALTA 1 CARACTER
def t_error(t):
    t.lexer.skip(1)

# Creamos el lexer
lexer = lex.lex()

# Entrada: datos del archivo
lexer.input(data)

 # Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      #CUANDO NO HAY MAS CARACTERES
    salida.write(str(tok.value)+'\n') #escribimos en el archivo de salida
