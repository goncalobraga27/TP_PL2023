from ply.lex import lex
from ply.yacc import yacc
import json


class Conversor:
    def __init__(self):
        self.fileStates = []
        self.documentTitle = ""
        self.documentData = dict()
        self.keyEmpty = 0
        self.auxListas = []

    def splitData(self, data):
        resultado = []
        resultadoInt = data.split('\n')
        lista = ""
        stringJunta = ""
        inLista = 0
        inString = 0
        inLiteral = 0
        for it in resultadoInt:
            if len(it) >= 1:
                if it[-1] != '[' and inLista == 0 and it[-1] != '"' and it[-1] != '\\' and it[
                    -1] != '\'' and inString == 0 and inLiteral == 0:
                    resultado.append(it)
                elif it[-1] == '[':
                    inLista = 1
                    lista += it
                elif inLista == 1 and it[-1] != ']':
                    lista += it
                elif inLista == 1 and it[-1] == ']':
                    lista += it
                    resultado.append(lista)
                    lista = ""
                    inLista = 0
                elif it[-1] == "\"" and it[-2] == "\"" and it[-3] == "\"" and inString == 0:
                    stringJunta += it
                    inString = 1
                elif it[-1] != "\"" and it[-2] != "\"" and it[-3] != "\"" and it[-1] != '\\' and it[
                    -1] != '\'' and inString == 1:
                    stringJunta += it + "\n"
                elif it[-1] == "\"" and it[-2] == "\"" and it[-3] == "\"" and inString == 1:
                    stringJunta += it
                    inString = 0
                    resultado.append(stringJunta)
                    stringJunta = ""
                elif it[-1] == "\\" and inString == 0:
                    stringJunta += it[:-1]
                    inString = 1
                elif it[-1] == "\\" and inString == 1:
                    stringJunta += it[:-1] + " "
                elif it[-1] == "\"" and it[-2] == "\"" and it[-3] == "\"" and inString == 1:
                    stringJunta += it
                    inString = 0
                    resultado.append(stringJunta)
                    stringJunta = ""
                elif it[-1] == "\'" and it[-2] == "\'" and it[-3] == "\'" and inLiteral == 0:
                    stringJunta += it
                    inLiteral = 1
                elif it[-1] != "\'" and it[-2] != "\'" and it[-3] != "\'" and inLiteral == 1:
                    stringJunta += it + " "
                elif it[-1] == "\'" and it[-2] == "\'" and it[-3] == "\'" and inLiteral == 1:
                    stringJunta += it
                    inLiteral = 0
                    resultado.append(stringJunta)
                    stringJunta = ""
                else:
                    resultado.append(it)

        return resultado

    def levelsData(self, data):
        resultado = []
        level = ""
        inComa = 0
        for it in data:
            if it == '\"':
                inComa = 1
            elif it != '.' and inComa == 0:
                level += it
            elif it != '.' and inComa == 1:
                level += it
            elif it == '.' and inComa == 0:
                resultado.append(level)
                level = ""
            elif it == '.' and inComa == 1:
                level += it
        resultado.append(level)
        return resultado

    def countPoints(self, data):
        resultado = 0
        for it in data:
            if it == '.':
                resultado += 1
        return resultado

    def conversor(self, data):

        states = (('NEWDICTIONARY', 'inclusive'),
                  ('NEWSUBDICTIONARY', 'inclusive'),
                  )
        tokens = (
            "WORD", "INT", "FLOAT", "PLICA", "FPR", "APR",
            "VIRG", "ASPA", "IGUAL", "HASHTAG", "CONTENT", "DATE", "TIME", "NEWDICTIONARY", "NEWSUBDICTIONARY",
            "SIGNAL", "INTWITHUNDERSCORE", "HEXADECIMAL", "OCTAL", "BINARIO"

        )

        literals = (':', '-')

        t_WORD = r'[a-zA-Z_\-\.\"]+'
        t_FLOAT = r'\d+\.\d+'
        t_INT = r'\d+'
        t_PLICA = r'\''
        t_FPR = r'\]'
        t_APR = r'\['
        t_VIRG = r'\,'
        t_ASPA = r'"'
        t_IGUAL = r'\='
        t_HASHTAG = r'\#'
        t_CONTENT = r'("|\').[^=]*("|\')'
        t_DATE = r'\d+\-\d+\-\d+'
        t_TIME = r'\d+\:\d+:\d+'
        t_SIGNAL = r'(\+|-){1}'
        t_INTWITHUNDERSCORE = r'\d+(?=\_)|\_|(?<=\_)\d+'
        t_HEXADECIMAL = r'0[xX][0-9a-fA-F\_]+'
        t_OCTAL = r'0[oO][0-7]+'
        t_BINARIO = r'0[bB][0-1]+'
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

        for it in data:
            lexer.input(it)
            for tok in lexer:
                if not tok:
                    break
                print(tok)

        def p_Dados(p):
            """
            Dados : WORD IGUAL Content
                  | HASHTAG Frase
                  | ASPA ASPA IGUAL Content
                  | PLICA PLICA IGUAL Content
                  | INT IGUAL Content
                  | CONTENT IGUAL Content

            """
            if str(p[1]) == "title":
                self.documentTitle = p[3][1:][:-1]
            elif str(p[1]) == '\"\"':
                dic = self.documentData[self.fileStates[0]]
                if len(self.fileStates) != 1:
                    for i in range(1, len(self.fileStates)):
                        dic = dic[self.fileStates[i]]
                    if str(p[3])[0] == '"':
                        dic['discouraged' + str(self.keyEmpty)] = p[3][1:][:-1]
                        self.keyEmpty += 1
                    else:
                        dic['discouraged' + str(self.keyEmpty)] = p[3]
                        self.keyEmpty += 1
                else:
                    if str(p[3])[0] == '"':
                        dic['discouraged' + str(self.keyEmpty)] = p[3][1:][:-1]
                        self.keyEmpty += 1
                    else:
                        dic['discouraged' + str(self.keyEmpty)] = p[3]
                        self.keyEmpty += 1
            elif str(p[1]) == '\'' and str(p[2]) == '\'':
                dic = self.documentData[self.fileStates[0]]
                if len(self.fileStates) != 1:
                    for i in range(1, len(self.fileStates)):
                        dic = dic[self.fileStates[i]]
                    if str(p[4])[0] == '"':
                        dic['discouraged' + str(self.keyEmpty)] = p[4][1:][:-1]
                        self.keyEmpty += 1
                    else:
                        dic['discouraged' + str(self.keyEmpty)] = p[4]
                        self.keyEmpty += 1
                else:
                    if str(p[4])[0] == '"':
                        dic['discouraged' + str(self.keyEmpty)] = p[4][1:][:-1]
                        self.keyEmpty += 1
                    else:
                        dic['discouraged' + str(self.keyEmpty)] = p[3]
                        self.keyEmpty += 1
            elif str(p[2]) == "=" and self.countPoints(str(p[1])) == 0:
                dic = self.documentData[self.fileStates[0]]
                if len(self.fileStates) != 1:
                    for i in range(1, len(self.fileStates)):
                        dic = dic[self.fileStates[i]]
                    if str(p[3])[0] == '"':
                        dic[str(p[1])] = p[3][1:][:-1]
                    else:
                        dic[str(p[1])] = p[3]
                else:
                    if str(p[3])[0] == '"':
                        if str(p[1])[0] == '"' or str(p[1])[0] == '\'':
                            dic[str(p[1])[1:][:-1]] = p[3][1:][:-1]
                        else:
                            dic[str(p[1])] = p[3][1:][:-1]
                    else:
                        if str(p[1])[0] == '"' or str(p[1])[0] == '\'':
                            dic[str(p[1])[1:][:-1]] = p[3]
                        else:
                            dic[str(p[1])] = p[3]
            elif str(p[2]) == "=" and self.countPoints(str(p[1])) == 1:
                fileStatesTemp = self.levelsData(str(p[1]))
                if len(fileStatesTemp) == 1:
                    self.documentData[fileStatesTemp[0]] = dict()
                else:
                    if fileStatesTemp[0] not in self.documentData:
                        self.documentData[fileStatesTemp[0]] = dict()
                    dic = self.documentData[fileStatesTemp[0]]
                    for i in range(1, len(fileStatesTemp) - 1):
                        if fileStatesTemp[i] not in dic:
                            dic[fileStatesTemp[i]] = dict()
                            dic = dic[fileStatesTemp[i]]
                        else:
                            dic = dic[fileStatesTemp[i]]
                    if type(dic) != str:
                        if str(p[3])[0] == '"':
                            dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[3][1:][:-1]
                        else:
                            dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[3]
            elif str(p[2]) == "=" and self.countPoints(str(p[1])) > 1:
                fileStatesTemp = self.levelsData(str(p[1]))
                if fileStatesTemp[0] not in self.documentData:
                    self.documentData[fileStatesTemp[0]] = dict()
                dic = self.documentData[fileStatesTemp[0]]
                for i in range(1, len(fileStatesTemp) - 1):
                    if fileStatesTemp[i] not in dic:
                        dic[fileStatesTemp[i]] = dict()
                        dic = dic[fileStatesTemp[i]]
                    else:
                        dic = dic[fileStatesTemp[i]]
                if type(dic) != str:
                    if str(p[3])[0] == '"':
                        dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[3][1:][:-1]
                    else:
                        dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[3]

        def p_Dados_NewDict_NewSubDict(p):
            """
            Dados : APR NEWDICTIONARY
                  | APR NEWSUBDICTIONARY
            """
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

        def p_Dados_WithOneEspace(p):
            """
            Dados : WORD WORD IGUAL Content
            """
            key = str(p[1]) + str(p[2])
            fileStatesTemp = self.levelsData(key)
            if len(fileStatesTemp) == 1:
                self.documentData[fileStatesTemp[0]] = dict()
            else:
                if fileStatesTemp[0] not in self.documentData:
                    self.documentData[fileStatesTemp[0]] = dict()
                dic = self.documentData[fileStatesTemp[0]]
                for i in range(1, len(fileStatesTemp)):
                    if fileStatesTemp[i] not in dic:
                        dic[fileStatesTemp[i]] = dict()
                if str(p[4])[0] == '"':
                    dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[4][1:][:-1]
                else:
                    dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[4]

        def p_Dados_WithTwoEspaces(p):
            """
            Dados : WORD WORD WORD IGUAL Content
            """
            key = str(p[1]) + str(p[2]) + str(p[3])
            fileStatesTemp = self.levelsData(key)
            if len(fileStatesTemp) == 1:
                self.documentData[fileStatesTemp[0]] = dict()
            else:
                if fileStatesTemp[0] not in self.documentData:
                    self.documentData[fileStatesTemp[0]] = dict()
                dic = self.documentData[fileStatesTemp[0]]
                for i in range(1, len(fileStatesTemp)):
                    if fileStatesTemp[i] not in dic:
                        dic[fileStatesTemp[i]] = dict()
                if str(p[5])[0] == '"':
                    dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[5][1:][:-1]
                else:
                    dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[5]

        def p_Dados_IntwithPoints(p):
            """
            Dados : INT WORD INT IGUAL Content
            """
            key = str(p[1]) + str(p[2]) + str(p[3])
            fileStatesTemp = self.levelsData(key)
            if len(fileStatesTemp) == 1:
                self.documentData[fileStatesTemp[0]] = dict()
            else:
                if fileStatesTemp[0] not in self.documentData:
                    self.documentData[fileStatesTemp[0]] = dict()
                dic = self.documentData[fileStatesTemp[0]]
                for i in range(1, len(fileStatesTemp)):
                    if fileStatesTemp[i] not in dic:
                        dic[fileStatesTemp[i]] = dict()
                if str(p[5])[0] == '"':
                    dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[5][1:][:-1]
                else:
                    dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[5]

        def p_Dados_IntwithPoints_Float(p):
            """
            Dados : FLOAT IGUAL Content
            """
            key = str(p[1])
            fileStatesTemp = self.levelsData(key)
            if len(fileStatesTemp) == 1:
                self.documentData[fileStatesTemp[0]] = dict()
            else:
                if fileStatesTemp[0] not in self.documentData:
                    self.documentData[fileStatesTemp[0]] = dict()
                dic = self.documentData[fileStatesTemp[0]]
                for i in range(1, len(fileStatesTemp)):
                    if fileStatesTemp[i] not in dic:
                        dic[fileStatesTemp[i]] = dict()
                if str(p[3])[0] == '"':
                    dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[3][1:][:-1]
                else:
                    dic[fileStatesTemp[len(fileStatesTemp) - 1]] = p[3]

        def p_Frase(p):
            """
            Frase : WORD
                  | Seqword
            """

        def p_SeqWord(p):
            """
            Seqword : WORD  Seqword
                    |
            """

        def p_Content(p):
            """
            Content : WORD
                    | CONTENT
                    | DATE
                    | TIME
                    | Lista
                    | Palavras
                    | LittleEndian
                    | HEXADECIMAL
                    | OCTAL
                    | BINARIO
            """
            if p[1] == 'True' or p[1] == 'true' or p[1] == 'Verdadeiro' or p[1] == 'verdadeiro':
                p[0] = bool(p[1])
            elif p[1] == 'False' or p[1] == 'false' or p[1] == 'Falso' or p[1] == 'falso':
                p[0] = bool(None)
            else:
                p[0] = p[1]
            print("O conteúdo da atribuição é isto:" + str(p[0]))

        def p_Content_LittleEndian(p):
            """
            LittleEndian : INTWITHUNDERSCORE OtherEndians
            """
            p[0] = str(p[1]) + str(p[2])

        def p_OtherEndians(p):
            """
            OtherEndians : INTWITHUNDERSCORE OtherEndians
            """
            p[0] = str(p[1]) + str(p[2])

        def p_OtherEndians_Vazio(p):
            """
            OtherEndians :
            """
            p[0] = ""

        def p_Content_inteiros(p):
            """
            Content : INT
            """
            p[0] = int(p[1])
            print("O conteúdo da atribuição é isto:" + str(p[0]))

        def p_Content_floats(p):
            """
            Content : FLOAT
            """
            p[0] = float(p[1])
            print("O conteúdo da atribuição é isto:" + str(p[0]))

        def p_Signal_Numbers_INT(p):
            """
            Content : SIGNAL INT
            """
            if p[1] == '-':
                p[0] = 0 - int(p[2])
            else:
                p[0] = 0 + int(p[2])
            print("O conteúdo da atribuição é isto:" + str(p[0]))

        def p_Signal_Numbers_FLOAT(p):
            """
            Content : SIGNAL FLOAT
                    | WORD FLOAT
            """
            if p[1] == '-':
                p[0] = 0 - float(p[2])
            else:
                p[0] = 0 + float(p[2])
            print("O conteúdo da atribuição é isto:" + str(p[0]))
        def p_Lista(p):
            """
            Lista : APR Elementos FPR
            """
            p[0] = self.auxListas
            self.auxListas = []

        def p_Lista_Vazia(p):
            """
            Lista : APR FPR
            """
            p[0] = []

        def p_Elementos(p):
            """
            Elementos : Elementos VIRG Elemento
            """
            p[0] = p[1]
            self.auxListas.append(p[3])

        def p_Elementos_Elemento(p):
            """
            Elementos : Elemento
            """
            if ',' not in str(p[1]):
                p[0] = p[1]
                self.auxListas.append(p[1])
            else:
                palavras = p[1].split(',')
                for item in palavras:
                    self.auxListas.append(item[1:][:-1])

        def p_Elemento(p):
            """
            Elemento : WORD
            """
            if p[1][0] == '"':
                p[0] = '"' + p[1][1:][:-1] + '"'

            else:
                p[0] = p[1]

        def p_Elemento_Content(p):
            """
            Elemento : CONTENT
            """
            p[0] = p[1]

        def p_Elemento_inteiros(p):
            """
            Elemento : INT
            """
            p[0] = int(p[1])

        def p_Palavras(p):
            """
            Palavras : WORD Palavras
            """
            p[0] = str(p[1]) + " " + str(p[2])

        def p_Palavras_Unica(p):
            """
            Palavras : WORD
            """
            p[0] = str(p[1])

        def p_Palavras_Vazia(p):
            """
            Palavras :
            """
            p[0] = ""

        def p_error(p):
            # print("O p é isto:" + str(p))
            print("Erro sintático no input!")
            parser.success = False

        parser = yacc()
        for it in data:
            parser.parse(it)
        print(self.documentData)
        with open(self.documentTitle + ".json", "w") as write_file:
            json.dump(self.documentData, write_file, indent=4)
