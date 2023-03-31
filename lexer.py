from ply.lex import lex


class analisadorLexico:
    def analiselexica(self, data):
        states = (('NEWDICTIONARY', 'inclusive'),
                  ('NEWSUBDICTIONARY', 'inclusive')
                  )
        tokens = ("WORD", "NUMBER", "POINT", "TWOPOINTS", "HIFEN", "PLICA", "FC", "AC", "FPR", "APR", "NEWLINE", "END")

        t_WORD = r'\w+'
        t_NUMBER = r'\d+'
        t_POINT = r'\.'
        t_TWOPOINTS = r'\:'
        t_HIFEN = r'\-'
        t_PLICA = r'\''
        t_FC = r'\}'
        t_AC = r'\{'
        t_FPR = r'\]'
        t_APR = r'\['

        t_ignore = ' \t\n'

        def t_NEWLINE(t):
            r"""\\n+"""
            t.lexer.lineno += t.value.count('\n')
            return t

        def t_NEWDICTIONARY(t):
            r'\[\w+\]'
            print("Entrei no estado NEWDICTIONARY")
            t.lexer.begin('NEWDICTIONARY')
            return t

        def t_NEWSUBDICTIONARY(t):
            r'\[\w+\.\w+\]'
            print("Entrei no estado NEWSUBDICTIONARY")
            t.lexer.begin('NEWSUBDICTIONARY')
            return t

        def t_NEWDICTIONARY_NEWSUBDICTIONARY_END(t):
            r'\[\w+\] | \[\w+\.\w+\]'
            print('Sai do meu estado atual, e vou voltar ao meu estado inicial')
            t.lexer.begin('INITIAL')
            return t

        def t_error(t):
            print('Lexical error: "' + str(t.value[0]) + '" in line ' + str(t.lineno))
            t.lexer.skip(1)

        lexer = lex()

        lexer.input(data)
        for tok in lexer:
            if not tok:
                break
            print(tok)
