import toml
from conversorTOMLtoJSON import Conversor
def main():
    conv = Conversor()
    f = open('dataset.txt')
    data = f.read()
    data = conv.splitData(data)
    conv.conversor(data)
if __name__ == "__main__":
    main()