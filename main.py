import toml
from lexer import analisadorLexico
def main():
    lexer = analisadorLexico()
    f = open('dataset.txt')
    data = f.readlines()
    lexer.analiselexica(str(data))

if __name__ == "__main__":
    main()