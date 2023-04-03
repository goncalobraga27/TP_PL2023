from ply.lex import lex
from ply.yacc import yacc


class analisadorLexico:
    def analiselexica(self, data):

        states = (('NEWDICTIONARY', 'inclusive'),
                  ('NEWSUBDICTIONARY', 'inclusive'),
                  )
        
        tokens = (
            "COMMENTARY",
            "WORD", 
            "NUMBER", 
            "CONTENT")

        literals = (r'\.',r'\:',r'\-',r'\'',r'\}',r'\{', r'\]',r'\[',r'\,', r'\"',r'\=')


        def t_COMMENTARY(t):
            r"#.*\n" # r'#.*'
            pass

        t_WORD = r'\w+'
        t_NUMBER = r'\d+'

        t_CONTENT = r'(\w|\"|\-|\:|\.)+'
        
        t_ANY_ignore = ' \t\n'

        def t_NEWLINE(t):
            r"""\n+"""
            t.lexer.lineno += t.value.count('\n')
            return t

        def t_NEWDICTIONARY(t):
            r'\w+\]'
            print("Entrei no estado NEWDICTIONARY")
            t.lexer.begin('NEWDICTIONARY')
            return t

        def t_NEWSUBDICTIONARY(t):
            r'(\w+\.\w+\])|((\w+\.)+\w+\])'
            print("Entrei no estado NEWSUBDICTIONARY")
            t.lexer.begin('NEWSUBDICTIONARY')
            return t

        def t_NEWCOMENTARY(t):
            r'\#'
            print("Entrei no estado NEWCOMENTARY")
            t.lexer.begin('NEWCOMENTARY')
            return t

        def t_NEWCOMMENTARY_CONTENT(t):
            r""".*\n"""
            pass

        def t_NEWDICTIONARY_NEWSUBDICTIONARY_END(t):
            r'\n\['
            print('Sai do meu estado atual, e vou voltar ao meu estado inicial')
            t.lexer.begin('INITIAL')
            return t

        def t_NEWCOMENTARY_END(t):
            r'\n'
            print('Sai do meu estado atual, e vou voltar ao meu estado inicial')
            t.lexer.begin('INITIAL')
            return t

        def t_ANY_error(t):
            print('Lexical error: "' + str(t.value[0]) + '" in line ' + str(t.lineno))
            t.lexer.skip(1)

        lexer = lex()

        lexer.input(data)
        for tok in lexer:
            if not tok:
                break
            print(tok)

        def p_expression(p):
            """
            expression : key IGUAL content
            """
            # p is a sequence that represents rule contents.
            #
            # expression : key IGUAL content
            #   p[0]     : p[1] p[2] p[3]
            #
            p[0] = ('atribuição', p[2], p[1], p[3])

        def p_key_word(p):
            """
            key: WORD
            """
            p[0] = ('chave', p[1])

        def p_content(p):
            """
            content : CONTENT
                    | lista
            """
            p[0] = ('content', p[1])

        def p_lista(p):
            """
            lista : APR elementos FPR
                  | APR FPR
            """
            p[0] = ('lista', p[1], p[2], p[3])
