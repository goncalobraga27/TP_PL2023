from ply.lex import lex
from ply.yacc import yacc


class analisadorLexico:
    def analiselexica(self, data):

        states = (('NEWDICTIONARY', 'inclusive'),
                  ('NEWSUBDICTIONARY', 'inclusive'),
                  )
        tokens = (
            "COMMENTARY", "WORD", "INT", "FLOAT", "POINT", "HIFEN", "PLICA", "FC", "AC", "FPR", "APR", "NEWLINE", "END",
            "VIRG", "ASPA", "IGUAL", "HASHTAG", "CONTENT", "DATE", "TIME", "BOOL")

        literals = (':', '-')

        t_WORD = r'[a-zA-Z_]+'
        t_FLOAT = r'\d+\,\d+'
        t_INT = r'\d+'
        t_POINT = r'\.'
        t_HIFEN = r'\-'
        t_PLICA = r'\''
        t_FC = r'\}'
        t_AC = r'\{'
        t_FPR = r'\]'
        t_APR = r'\['
        t_VIRG = r'\,'
        t_ASPA = r'\"'
        t_IGUAL = r'\='
        t_HASHTAG = r'\#'
        t_CONTENT = r'\".*"'
        t_DATE = r'\d+\-\d+\-\d+'
        t_TIME = r'\d+\:\d+:\d+'
        t_BOOL = r'verdadeiro|falso'  # ou e` true or false?

        t_ANY_ignore = ' \t'

        def t_COMMENTARY(t):
            r"\#.*\n"
            pass

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

        def t_NEWDICTIONARY_NEWSUBDICTIONARY_END(t):
            r'\n\['
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

        def p_atribuicao(p):
            """
            atribuicao : key IGUAL content
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

        def p_lista_elementos(p):
            """
            elementos : INT
                      | ASPA WORD ASPA
                      | INT VIRG elementos
                      | ASPA WORD ASPA VIRG elementos
            """
            p[0] = ('elementos', p[1])

        def p_seccao(p):
            """
            seccao : APR content FPR conteudo
            """
            p[0] = ('seccao', p[2], p[4])

        def p_seccao_conteudo(p):
            """
            conteudo : atribuicao outrasAtribuicoes
                    | VAZIO
                    | seccao
            """
            p[0] = ('conteudo', p[2], p[4])

        def p_outrasAtribuicoes(p):
            """
            outrasAtribuicoes : Vazio
                              | atribuicao outrasAtribuicoes
            """
            p[0] = ('Outras Atribuicoes', p[1], p[2])

        # Build the parser
        #parser = yacc()

        # Parse a file
        #ast = parser.parse()
        #print(ast)