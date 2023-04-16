from ply.lex import lex
from ply.yacc import yacc
import json


class Conversor:
    def __init__(self):
        self.fileStates = []
        self.documentTitle = ""
        self.documentData = dict()

    def levelsData(self, data):
        nLevel = 0
        resultado = []
        level = ""
        for it in data:
            if it == '.':
                resultado.append(level)
                nLevel += 1
                level += it
            else:
                level += it
        resultado.append(data)
        return resultado

    def conversor(self, data):

        states = (('NEWDICTIONARY', 'inclusive'),
                  ('NEWSUBDICTIONARY', 'inclusive'),
                  )
        tokens = (
            "COMMENTARY", "WORD", "INT", "FLOAT", "POINT", "HIFEN", "PLICA", "FC", "AC", "FPR", "APR", "NEWLINE", "END",
            "VIRG", "ASPA", "IGUAL", "HASHTAG", "CONTENT", "DATE", "TIME", "BOOL", "NEWDICTIONARY", "NEWSUBDICTIONARY")

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

        def p_Dados(p):
            """
            Dados : WORD IGUAL Content
                  | APR NEWDICTIONARY
                  | APR NEWSUBDICTIONARY
            """
            if str(p[1]) == "title":
                self.documentTitle = str(p[3])[1:][:-1]
            elif str(p[1]) == "[":
                self.fileStates = self.levelsData(str(p[2])[:-1])
                if len(self.fileStates) == 1:
                    self.documentData[self.fileStates[0]] = dict()
                else:
                    if self.fileStates[0] not in self.documentData:
                        self.documentData[self.fileStates[0]] = dict()
                    dic = self.documentData[self.fileStates[0]]
                    for i in range(1, len(self.fileStates)):
                        if self.fileStates[i] not in dic:
                            dic[self.fileStates[i]] = dict()
                        dic = dic[self.fileStates[i]]

            else:
                dic = self.documentData[self.fileStates[0]]
                if len(self.fileStates) != 1:
                    for i in range(1, len(self.fileStates)):
                        dic = dic[self.fileStates[i]]
                    dic[str(p[1])] = str(p[3])
                else:
                    dic[str(p[1])] = str(p[3])

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
            print("O conteúdo da atribuição é isto:" + p[0])

        def p_Lista(p):
            """
            Lista : APR Elementos FPR
            """
            p[0] = "[" + str(p[2]) + "]"

        def p_Lista_Vazia(p):
            """
            Lista : APR FPR
            """
            p[0] = "[]"

        def p_Elementos(p):
            """
            Elementos : Elementos VIRG Elemento
            """
            p[0] = str(p[1]) + "," + str(p[3])

        def p_Elementos_Elemento(p):
            """
            Elementos : Elemento
            """
            p[0] = str(p[1])

        def p_Elemento(p):
            """
            Elemento : INT
                    | WORD
                    | CONTENT
            """
            p[0] = str(p[1])

        def p_error(p):
            print("O p é isto:" + str(p))
            print("Erro sintático no input!")
            parser.success = False

        parser = yacc()
        data = data.split('\n')
        for it in data:
            parser.parse(it)
        print(self.documentData)
        with open(self.documentTitle, "w") as write_file:
            json.dump(self.documentData, write_file, indent=4)
