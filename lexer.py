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
        """
        lexer.input(data)
        for tok in lexer:
            if not tok:
                break
            print(tok)
        """

        def p_Atribuicao(p):
            """
            Atribuicao : Key IGUAL Content
            """

        def p_Key(p):
            """
             Key : WORD
            """
            p[0] = p[1]

        def p_Content(p):
            """
            Content : WORD
                    | FLOAT
                    | INT
                    | CONTENT
                    | DATE
                    | TIME
                    | BOOL
                    | Lista
            """
            p[0] = p[1]
            print("Estou a printar isto:" + p[0])

        def p_Lista(p):
            """
            Lista : APR Elementos FPR
            """
            p[0] = p[1]

        def p_Lista_Vazia(p):
            """
            Lista : APR FPR
            """

        def p_Elementos(p):
            """
            Elementos : Elementos VIRG Elemento
            """

        def p_Elementos_Elemento(p):
            """
            Elementos : Elemento
            """

        def p_Elemento(p):
            """
            Elemento : INT
                    | WORD
                    | CONTENT
            """
            p[0] = p[1]

        def p_Seccao(p):
            """
            Seccao : APR Content FPR Conteudo
            """
            p[0] = p[4]

        def p_Seccao_Conteudo(p):
            """
            Conteudo : Atribuicao OutrasAtribuicoes
                     | Seccao
            """
            p[0] = p[1]

        def p_Seccao_Conteudo_Vazia(p):
            """
           Conteudo :
            """
        def p_OutrasAtribuicoes(p):
            """
            OutrasAtribuicoes : OutrasAtribuicoes Atribuicao
            """
            p[0] = p[2]

        def p_OutrasAtribuicoes_Vazia(p):
            """
            OutrasAtribuicoes :
            """

        def p_error(p):
            print("O p é isto:" + str(p))
            print("Erro sintático no input!")
            parser.success = False

        parser = yacc()

        parserResult = parser.parse(data)
        print(parserResult)
