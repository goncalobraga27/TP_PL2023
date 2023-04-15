import toml
from conversorTOMLtoJSON import Conversor
def main():
    conv = Conversor()
    f = open('dataset.txt')
    data = f.read()
    conv.conversor(str(data))

if __name__ == "__main__":
    main()