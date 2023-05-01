import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw
from conversorTOMLtoJSON import Conversor
import sys

"""
#TODO:  - Menu principal (initUI)
        - Mexer em cores
        - Bloquear full screen
        - E o que a imaginação ditar... ඞඞඞඞ
"""

class Window(qtw.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(500,200,1000,800)
        self.setWindowTitle("Conversor TOML")
        #self.initUI()
        self.convertUI("JSON","TOML")

    # trocar pra menu de conversao
    def convertUI(self,input,output):
        self.inputType = qtw.QLabel(input,self)
        self.inputType.setFont(qtg.QFont('Arial', 30))
        self.inputType.move(20,0)
        self.inputType.resize(120,60)

        self.textboxInput = qtw.QTextEdit(self,
        acceptRichText= True,
        #lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
        #lineWrapColumnOrWidth=120,
        #placeholderText="Insira o conteúdo a converter..."
        )
        self.textboxInput.setFontPointSize(13)
        self.textboxInput.setPlaceholderText("Insira o conteúdo a converter...")
        self.textboxInput.move(20, 50)
        self.textboxInput.resize(450,660)

        self.outputType = qtw.QLabel(output,self)
        self.outputType.setFont(qtg.QFont('Arial', 30))
        self.outputType.move(530,0)
        self.outputType.resize(120,60)

        self.textboxOutput = qtw.QTextEdit(self,
        acceptRichText= True,
        readOnly = True,
        #lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
        #lineWrapColumnOrWidth=120,
        #plainText=". . ."
        )
        self.textboxOutput.setPlainText(". . .")
        self.textboxOutput.setFontPointSize(13)
        self.textboxOutput.move(530, 50)
        self.textboxOutput.resize(450,660)

        self.convertButton = qtw.QPushButton("Converter", self)
        self.convertButton.setFont(qtg.QFont('Arial', 13))
        self.convertButton.move(825, 730)
        self.convertButton.resize(140,60)
        self.convertButton.clicked.connect(self.press_Converter)

    def press_Converter(self):    
            #usar funcao de conversao
            #pegar texto inserido : { self.textboxInput.toPlainText()}
            #apos conversao: self.textboxOutput.setPlainText(-texto convertido-)
            self.textboxOutput.setPlainText("IHIHIHIHIHI")


def start():
    app = qtw.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

start()