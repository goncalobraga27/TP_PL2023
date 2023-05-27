import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from conversorTOMLtoJSON import Conversor
import json
import sys

"""
#TODO:  - Mexer na cor da barra de descer
        - Mexer em cores
        - E o que a imaginação ditar... ඞඞඞඞ
        - Minor: tentar centar ao inicializar e mudar o nome da janela
"""

class MainMenu(qtw.QMainWindow):
    def __init__(self):
        super(MainMenu,self).__init__()
        self.setGeometry(500,100,1000,800)
        self.setFixedSize(1000,800)
        self.setWindowTitle("Conversor JSON")
        self.initUI()
        #self.convertUI("TOML","JSON",1)

    def initUI(self):
        self.setStyleSheet("background-color: rgb(154,192,205);")
        self.title = qtw.QLabel("Processamento de Linguagens",self)
        self.title.setFont(qtg.QFont('Arial', 30,weight=qtg.QFont.Bold))
        self.title.setStyleSheet("color: rgb(0,0,0);")
        self.title.move(230,10)
        self.title.resize(800,55)

        self.setStyleSheet("background-color: rgb(154,192,205);")
        self.title = qtw.QLabel("Trabalho Prático - Conversor de TOML",self)
        self.title.setFont(qtg.QFont('Arial', 20,weight=qtg.QFont.Bold))
        self.title.setStyleSheet("color: rgb(0,0,0);")
        self.title.move(300,70)
        self.title.resize(650,35)

        self.setStyleSheet("background-color: rgb(154,192,205);")
        self.title = qtw.QLabel("Ano Letivo 2022/2023 - Grupo 31",self)
        self.title.setFont(qtg.QFont('Arial', 17,weight=qtg.QFont.Bold))
        self.title.setStyleSheet("color: rgb(0,0,0);")
        self.title.move(370,110)
        self.title.resize(510,35)

        self.title = qtw.QLabel("Projeto concebido por Gonçalo Braga, João Loureiro e Simão Barroso",self)
        self.title.setFont(qtg.QFont('Arial', 13,weight=qtg.QFont.Bold))
        self.title.setStyleSheet("color: white;")
        self.title.move(275,750)
        self.title.resize(800,60)

        self.logo = qtw.QLabel(self)
        #pixmap = qtg.QPixmap('images/EEUMLOGO(1).png')
        self.logo.setPixmap(qtg.QPixmap('images/EEUMLOGO(1).png').scaled(150,136,qtc.Qt.IgnoreAspectRatio))
        self.logo.resize(150,136)
        self.logo.move(30,16)

        self.o1Button = qtw.QPushButton("Converter TOML\n para JSON", self)
        self.o1Button.setFont(qtg.QFont('Arial', 16,weight=qtg.QFont.Bold))
        self.o1Button.setStyleSheet("""
        QPushButton {
            background-color: rgb(238,64,0); 
            border: 2px solid rgb(0,0,0);
            border-radius: 11px;
            color: white;
        }
        QPushButton:hover {
            background-color: rgb(124,205,124);
            border: 2px solid rgb(0,0,0);
            color: white;
        }
        """)
        self.o1Button.move(70, 245)
        self.o1Button.resize(250,150)
        self.o1Button.setToolTip('Converta algo no formato <b>TOML</b> para o formato <b>JSON</b>')
        self.o1Button.clicked.connect(lambda: self.press_Option(1))

        self.o2Button = qtw.QPushButton("PLACEHOLDER 2", self)
        self.o2Button.setFont(qtg.QFont('Arial', 16,weight=qtg.QFont.Bold))
        self.o2Button.setStyleSheet("""
        QPushButton {
            background-color: rgb(238,64,0); 
            border: 2px solid rgb(0,0,0);
            border-radius: 11px;
            color: white;
        }
        QPushButton:hover {
            background-color: rgb(124,205,124);
            border: 2px solid rgb(0,0,0);
            color: white;
        }
        """)
        self.o2Button.move(370, 245)
        self.o2Button.resize(250,150)
        self.o2Button.setToolTip('Converta algo no formato <b>X</b> para o formato <b>Y</b>')
        #self.o2Button.clicked.connect(self.press_Option(2))

        self.o3Button = qtw.QPushButton("PLACEHOLDER 3", self)
        self.o3Button.setFont(qtg.QFont('Arial', 16,weight=qtg.QFont.Bold))
        self.o3Button.setStyleSheet("""
        QPushButton {
            background-color: rgb(238,64,0); 
            border: 2px solid rgb(0,0,0);
            border-radius: 11px;
            color: white;
        }
        QPushButton:hover {
            background-color: rgb(124,205,124);
            border: 2px solid rgb(0,0,0);
            color: white;
        }
        """)
        self.o3Button.move(670, 245)
        self.o3Button.resize(250,150)
        self.o3Button.setToolTip('Converta algo no formato <b>X</b> para o formato <b>Y</b>')
        #self.o3Button.clicked.connect(self.press_Option(3))

        self.o4Button = qtw.QPushButton("PLACEHOLDER 4", self)
        self.o4Button.setFont(qtg.QFont('Arial', 16,weight=qtg.QFont.Bold))
        self.o4Button.setStyleSheet("""
        QPushButton {
            background-color: rgb(238,64,0); 
            border: 2px solid rgb(0,0,0);
            border-radius: 11px;
            color: white;
        }
        QPushButton:hover {
            background-color: rgb(124,205,124);
            border: 2px solid rgb(0,0,0);
            color: white;
        }
        """)
        self.o4Button.move(70, 485)
        self.o4Button.resize(250,150)
        self.o4Button.setToolTip('Converta algo no formato <b>X</b> para o formato <b>Y</b>')
        #self.o4Button.clicked.connect(self.press_Option(4))

        self.o5Button = qtw.QPushButton("PLACEHOLDER 5", self)
        self.o5Button.setFont(qtg.QFont('Arial', 16,weight=qtg.QFont.Bold))
        self.o5Button.setStyleSheet("""
        QPushButton {
            background-color: rgb(238,64,0); 
            border: 2px solid rgb(0,0,0);
            border-radius: 11px;
            color: white;
        }
        QPushButton:hover {
            background-color: rgb(124,205,124);
            border: 2px solid rgb(0,0,0);
            color: white;
        }
        """)
        self.o5Button.move(370, 485)
        self.o5Button.resize(250,150)
        self.o5Button.setToolTip('Converta algo no formato <b>X</b> para o formato <b>Y</b>')
        #self.o5Button.clicked.connect(self.press_Option(5))

        self.o6Button = qtw.QPushButton("PLACEHOLDER 6", self)
        self.o6Button.setFont(qtg.QFont('Arial', 16,weight=qtg.QFont.Bold))
        self.o6Button.setStyleSheet("""
        QPushButton {
            background-color: rgb(238,64,0); 
            border: 2px solid rgb(0,0,0);
            border-radius: 11px;
            color: white;
        }
        QPushButton:hover {
            background-color: rgb(124,205,124);
            border: 2px solid rgb(0,0,0);
            color: white;
        }
        """)
        self.o6Button.move(670, 485)
        self.o6Button.resize(250,150)
        self.o6Button.setToolTip('Converta algo no formato <b>X</b> para o formato <b>Y</b>')
        #self.o6Button.clicked.connect(self.press_Option(6))

    def press_Option(self,option):
        match option:
            case 1:
                convertPage = ConvertMenu()
                convertPage.convertUI("TOML","JSON",1)
                widget.addWidget(convertPage)
                widget.setCurrentWidget(convertPage)
            case _:
                convertPage = ConvertMenu()
                convertPage.convertUI("X","Y",1)
                widget.addWidget(convertPage)
                widget.setCurrentWidget(convertPage)      

class ConvertMenu(qtw.QMainWindow):
    def __init__(self):
        super(ConvertMenu,self).__init__()
        self.setGeometry(500,100,1000,800)
        self.setFixedSize(1000,800)
        self.setWindowTitle("Conversor JSON")
    
    # trocar pra menu de conversao
    def convertUI(self,input,output,option):
        self.setStyleSheet("background-color: rgb(154,192,205);")
        self.inputType = qtw.QLabel(input,self)
        self.inputType.setFont(qtg.QFont('Arial', 30))
        self.inputType.setStyleSheet("color: rgb(255,246,143);")
        self.inputType.move(20,0)
        self.inputType.resize(450,60)

        self.textboxInput = qtw.QTextEdit(self,
        acceptRichText= False,
        #lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
        #lineWrapColumnOrWidth=120,
        #placeholderText="Insira o conteúdo a converter..."
        )
        self.textboxInput.setFontPointSize(13)
        self.textboxInput.setStyleSheet("background-color: white;")
        self.textboxInput.setPlaceholderText("Insira o conteúdo a converter...")
        self.textboxInput.move(20, 60)
        self.textboxInput.resize(450,660)

        self.outputType = qtw.QLabel(output,self)
        self.outputType.setFont(qtg.QFont('Arial', 30))
        self.outputType.setStyleSheet("color: rgb(255,246,143);")
        self.outputType.move(530,0)
        self.outputType.resize(450,60)

        self.textboxOutput = qtw.QTextEdit(self,
        acceptRichText= False,
        readOnly = True,
        #lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
        #lineWrapColumnOrWidth=120,
        #plainText=". . ."
        )
        self.textboxOutput.setPlainText(". . .")
        self.textboxOutput.setFontPointSize(13)
        self.textboxOutput.setStyleSheet("background-color: white;")
        self.textboxOutput.move(530, 60)
        self.textboxOutput.resize(450,660)

        self.convertButton = qtw.QPushButton("Converter", self)
        self.convertButton.setFont(qtg.QFont('Arial', 13,weight=qtg.QFont.Bold))
        self.convertButton.setStyleSheet("""
        QPushButton {
            background-color: rgb(238,64,0); 
            border: 2px solid rgb(0,0,0);
            border-radius: 20px;
        }
        QPushButton:hover {
            background-color: rgb(124,205,124);
            border: 2px solid rgb(0,0,0);
        }
    """)
        self.convertButton.move(825, 730)
        self.convertButton.resize(140,60)
        self.convertButton.clicked.connect(lambda: self.press_Converter(option))

    def press_Converter(self,option):
        conv = Conversor()
        data = conv.splitData(self.textboxInput.toPlainText())
        print(self.textboxInput.toPlainText())
        conv.conversor(data)   
        self.textboxOutput.setPlainText(str(json.dumps(conv.documentData, indent=4))) 
        #usar funcao de conversao
        #pegar texto inserido : { self.textboxInput.toPlainText()}
        #apos conversao: self.textboxOutput.setPlainText(-texto convertido-)
        #self.textboxOutput.setPlainText("IHIHIHIHIHI")
                 


def start():
    app = qtw.QApplication(sys.argv)
    global widget 
    widget = qtw.QStackedWidget()
    widget.setGeometry(500,100,1000,800)
    widget.setFixedSize(1000,800)
    widget.setWindowTitle("Conversor JSON")
    mainWin = MainMenu()
    widget.addWidget(mainWin)
    widget.setCurrentWidget(mainWin)   # setting the page that you want to load when application starts up. you can also use setCurrentIndex(int)
    widget.show()
    sys.exit(app.exec_())

start()