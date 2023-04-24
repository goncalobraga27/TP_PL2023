# Passa um dictionario (dic) para o formato YAML, escrevendo este num ficheiro YAML (f). Numero de espacos para a identacao deve comecar por 0, sendo recursivamente manipulado.
def dictToYAML(dic,espacos,f):
    for e in dic:
        if type(dic[e]) == dict:
            f.write((espacos * "  " ) + e + ":\n")
            #res += dictToYAML(dic[e],espacos+1,res)         
            dictToYAML(dic[e],espacos+1,f)
        elif type(dic[e]) == list:
            f.write((espacos * "  " ) + e + ":\n")
            for l in dic[e]:
                f.write(((espacos+1) * "  " ) + "- " + str(l) + "\n")
        else:
            f.write((espacos * "  " ) + e + ": " + str(dic[e]) + "\n")

# ! DEBUG !
# Passa um dictionario (dic) para o formato YAML, escrevendo este no terminal. Numero de espacos para a identacao deve comecar por 0, sendo recursivamente manipulado.
def dictToYAML_P(dic,espacos):
    for e in dic:
        if type(dic[e]) == dict:
            print((espacos * "  " ) + e + ":\n", end =" ")
            #res += dictToYAML(dic[e],espacos+1,res)         
            dictToYAML_P(dic[e],espacos+1)
        elif type(dic[e]) == list:
            print((espacos * "  " ) + e + ":\n", end =" ")
            for l in dic[e]:
                print(((espacos+1) * "  " ) + "- " + str(l) + "\n", end =" ")
        else:
            print((espacos * "  " ) + e + ": " + str(dic[e]) + "\n", end =" ")

# ! DEBUG !
"""
teste = {'employee': {'name': 'John Doe', 'age': 35, 'job': {'title': 'Software Engineer', 'department': 'IT', 'years_of_experience': 10}, 'address': {'street': '123 Main St.', 'city': 'San Francisco', 'state': 'CA', 'zip': 94102}, 'past_jobs' : ['sega','Nintendo','EA']}}

#print(dictToYAML(teste,0,""))
dictToYAML_P(teste,0)

f = open("teste.yaml", "a")
dictToYAML(teste,0,f)
"""