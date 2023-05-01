import ply.yacc as yacc
import ply.lex as lex
#from json_lex import tokens

import toml

tokens = (
    'STRING',
    'NUM',
    'LPR',
    'RPR',
    'LCHAVETA',
    'RCHAVETA',
    'VIRG',
    'DOISPONTOS',
    'BOOL',
    'NULL'
)

# regex para cada token

t_STRING = r'"(?:\\.|[^"])*"'  # Matches double-quoted strings with escape sequences
t_NUM = r'-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?'  # Da match com qualquer numero, inclusive decimais # (\+|-)?
t_LPR = r'\['  # Abrir parentese reto
t_RPR = r'\]'  # Fechar parentese reto
t_LCHAVETA = r'\{'  # Abrir chaveta
t_RCHAVETA = r'\}'  # Abrir chaveta
t_VIRG = r','  
t_DOISPONTOS = r':' 
t_BOOL = r'true|false'
t_NULL = r'null' 

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()


# Gramatica JSON


def p_object(p):
    '''
    object : LCHAVETA members RCHAVETA
    '''
    p[0] = dict(p[2])

def p_members(p):
    '''
    members : par
            | par VIRG members
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_par(p):
    '''
    par : STRING DOISPONTOS value
    '''
    p[0] = (p[1][1:-1], p[3])

def p_array(p):
    '''
    array : LPR elementos RPR
    '''
    p[0] = p[2]
    #print(p[0])

def p_elementos(p):
    '''
    elementos : value
             | value VIRG elementos
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_value_outros(p):
    '''
    value : object
          | NULL
          | array
    '''
    p[0] = p[1]
    


def p_value_Bool(p):
    '''
    value : BOOL
    '''
    p[0] = bool(p[1])

def p_value_NUM(p):
    '''
    value : NUM
    '''
    # mudar aqui, nao aceita so ints (TAMBEM TEM DE ACEITAR NOTACAO CIENTIFICA)
    try :
        p[0] = int(p[1])
    except:
        p[0] = float(p[1])
    


def p_value_String(p):
    '''
    value : STRING
    '''
    p[0] = p[1][1:-1]


# Define error handling
def p_error(p):
    if p:
        print("Erro sintÃ¡tico! :  '%s'" % p.value)
    else:
        print("EOF")


parser = yacc.yacc()

exemplo= '''
{
  "name" : [
  "string": "Hello, world!",
  "number": 12345,
  "boolean": true,
  "null": null,
  "array": ["apple", "banana", "cherry"],
  "object": {
    "key1": "value1",
    "key2": "value2",
    "servers":{
        "alpha": {
            "beta":1
            }
        }
    }
  ]
}
'''
exemplo2 = '''
{
  "firstName": "John",
  "lastName": "Doe",
  "age": 35,
  "age1": 35e10,
  "age1": 35e-1,
  "age2": -35,
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "555-555-1234"
    },
    {
      "type": "work",
      "number": "555-555-5678"
    }
  ],
  "email": "johndoe@example.com",
  "isMarried": true,
  "spouse": null,
  "children": [
    {
      "name": "Jane",
      "age": 10
    },
    {
      "name": "Joe",
      "age": 8
    }
  ],
  "hobbies": [
    "reading",
    "hiking",
    "cooking"
  ],
  "favoriteColors": {
    "primary": "blue",
    "secondary": "green"
  },
  "date": "2023-04-25T12:00:00.000Z"
}

'''
print(parser.parse(exemplo2))
print("-<><><><><><><><><><><><")
print(toml.dumps(parser.parse(exemplo2))) # esta correto (ERRO NO ARRAY)


print('''\n\n------------------------\n
      Problemas : \n
      -Tratar da notacao cientifica\n
      -Ver se as datas fazem parte\n
      - Problema virgula array -> supostamente funciona em python
      - testar com mais exemplos
      - date type error
--------------------------\n''')