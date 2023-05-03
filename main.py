import toml
from conversorTOMLtoJSON import Conversor
def main():
    while True:
        nomeFicheiro = input('Insira o path do ficheiro que quer converter : ')
        conv = Conversor()
        f = open(nomeFicheiro)
        data = f.read()
        data = conv.splitData(data)
        #conv.conversor(data)
if __name__ == "__main__":
    main()