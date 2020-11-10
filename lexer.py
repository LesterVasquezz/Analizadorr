import ply.lex as lex
import re
from ply.lex import TOKEN

fuente = open("shadow", "r")
salida = open("salida.txt", "w")

data = fuente.read()

# lista de tokens
tokens = (
    'SALT',
    'HASH',#hash completo
    'EXTRA'#es lo que hay despues del $, alfanumerico
)

# Regular expression rules for simple tokens
EXTRA=r'[A-Z,a-z,0-9,/,.]*' #se uso cerradura de Kleene

SALT=r'\$'+r'\d+'+r'\$'+EXTRA
HASH=r'\$'+EXTRA


#Definimos hash como token
@TOKEN(SALT)
def t_SALT(t):
    t.value = str(t.value)
    return t
@TOKEN(HASH)
def t_HASH(t):
    t.value = str(t.value[1:])
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
