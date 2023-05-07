import toml
from conversorTOMLtoJSON import Conversor
def main():
    i = 1
    while i:#True:
        #nomeFicheiro = input('Insira o path do ficheiro que quer converter : ')
        conv = Conversor()
        f = open("dataset3.txt")#open(nomeFicheiro)
        data = f.read()
        data = conv.splitData(data)
        conv.conversor(data)
        i=0
if __name__ == "__main__":
    main()