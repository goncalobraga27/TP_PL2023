# Passa um dictionario (dic) para o formato YAML, escrevendo este numa string (result). Numero de espacos para a identacao deve comecar por 0, sendo recursivamente manipulado.
def dictToYAML(dic, espacos):
    result = ""
    for e in dic:
        if type(dic[e]) == dict:
            result += (espacos * "  ") + e + ":\n"
            result += dictToYAML(dic[e], espacos + 1)
        elif type(dic[e]) == list:
            result += (espacos * "  ") + e + ":\n"
            for l in dic[e]:
                result += ((espacos + 1) * "  ") + "- " + str(l) + "\n"
        else:
            result += (espacos * "  ") + e + ": " + str(dic[e]) + "\n"
    return result

# Passa um dictionario (dic) para o formato XML, escrevendo este numa string (result). Numero de espacos para a identacao deve comecar por 0, sendo recursivamente manipulado.
def dict2xml(dic, n):
    result = ""
    for i in dic:
        result += 4 * (n - 1) * " " + "<" + i + ">\n"
        if type(dic[i]) == dict:
            result += dict2xml(dic[i], n + 1)
        else:
            result += 4 * n * " " + str(dic[i]) + "\n"
        result += 4 * (n - 1) * " " + "</" + i + ">\n"
    return result

#teste = {'employee': {'name': 'John Doe', 'age': 35, 'job': {'title': 'Software Engineer', 'department': 'IT', 'years_of_experience': 10}, 'address': {'street': '123 Main St.', 'city': 'San Francisco', 'state': 'CA', 'zip': 94102}, 'past_jobs' : ['sega','Nintendo','EA']}}
"""
#print(dictToYAML(teste,0,""))
dictToYAML_P(teste,0)

f = open("teste.yaml", "a")
dictToYAML(teste,0,f)
"""

#print(dictToYAML(teste,0))