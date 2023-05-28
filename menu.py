import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from conversorTOMLtoJSON import Conversor
import toYAML_XML as tYX
import json
import sys
import jsonToToml as jTT

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
        #self.setWindowTitle("Conversor JSON")
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
        self.o1Button.move(200, 245)
        self.o1Button.resize(250,150)
        self.o1Button.setToolTip('Converta algo no formato <b>TOML</b> para o formato <b>JSON</b>')
        self.o1Button.clicked.connect(lambda: self.press_Option(1))

        self.o3Button = qtw.QPushButton("Converter TOML\n para YAML", self)
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
        self.o3Button.move(550, 245)
        self.o3Button.resize(250,150)
        self.o3Button.setToolTip('Converta algo no formato <b>TOML</b> para o formato <b>YAML</b>')
        self.o3Button.clicked.connect(lambda: self.press_Option(3))

        self.o4Button = qtw.QPushButton("Converter TOML\n para XML", self)
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
        self.o4Button.move(200, 485)
        self.o4Button.resize(250,150)
        self.o4Button.setToolTip('Converta algo no formato <b>TOML</b> para o formato <b>XML</b>')
        self.o4Button.clicked.connect(lambda: self.press_Option(4))

        self.o6Button = qtw.QPushButton("Converter JSON\n para TOML", self)
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
        self.o6Button.move(550, 485)
        self.o6Button.resize(250,150)
        self.o6Button.setToolTip('Converta algo no formato <b>JSON</b> para o formato <b>TOML</b>')
        self.o6Button.clicked.connect(lambda: self.press_Option(6))

    def press_Option(self,option):
        match option:
            case 1:
                convertPage = ConvertMenu()
                convertPage.convertUI("TOML","JSON",1,True)
                widget.addWidget(convertPage)
                widget.setCurrentWidget(convertPage)
            case 3:
                convertPage = ConvertMenu()
                convertPage.convertUI("TOML","YAML",3,False)
                widget.addWidget(convertPage)
                widget.setCurrentWidget(convertPage)
            case 4:
                convertPage = ConvertMenu()
                convertPage.convertUI("TOML","XML",4,False)
                widget.addWidget(convertPage)
                widget.setCurrentWidget(convertPage)
            case 6:
                convertPage = ConvertMenu()
                convertPage.convertUI("JSON","TOML",6,False)
                widget.addWidget(convertPage)
                widget.setCurrentWidget(convertPage)
            case _:
                convertPage = ConvertMenu()
                convertPage.convertUI("X","Y",1,False)
                widget.addWidget(convertPage)
                widget.setCurrentWidget(convertPage)      

class ConvertMenu(qtw.QMainWindow):
    def __init__(self):
        super(ConvertMenu,self).__init__()
        self.setGeometry(500,100,1000,800)
        self.setFixedSize(1000,800)
        #self.setWindowTitle("Conversor JSON")
    
    # trocar pra menu de conversao
    def convertUI(self,input,output,option,file):
        widget.setWindowTitle("Conversor " + input + " para " + output)
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

        self.AFButton = qtw.QPushButton("Abrir Ficheiro", self)
        self.AFButton.setFont(qtg.QFont('Arial', 13,weight=qtg.QFont.Bold))
        self.AFButton.setStyleSheet("""
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
        self.AFButton.move(20, 730)
        self.AFButton.resize(140,60)
        self.AFButton.clicked.connect(lambda: self.openFile())

        if file:
            self.convertButton.move(675, 730)
            self.convertButton.resize(140,60)
            self.convertButton.clicked.connect(lambda: self.press_Converter(option))

            self.SVButton = qtw.QPushButton("Guardar em\n Ficheiro", self)
            self.SVButton.setFont(qtg.QFont('Arial', 13,weight=qtg.QFont.Bold))
            self.SVButton.setStyleSheet("""
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
            self.SVButton.move(840, 730)
            self.SVButton.resize(140,60)
            self.SVButton.clicked.connect(lambda: self.saveFile(option))
        
        self.BackButton = qtw.QPushButton("🡸", self)
        self.BackButton.setFont(qtg.QFont('Arial', 13,weight=qtg.QFont.Bold))
        self.BackButton.setStyleSheet("""
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
        self.BackButton.move(930, 7)
        self.BackButton.resize(50,50)
        self.BackButton.clicked.connect(lambda: self.returnMenu())
        self.BackButton.setToolTip('Voltar ao Início')
        
    
    def returnMenu(self):
        '''
        mainPage = MainMenu()
        mainPage.initUI()
        widget.addWidget(mainPage)
        widget.setCurrentWidget(mainPage)
        '''
        widget.setWindowTitle("Trabalho Prático")
        widget.removeWidget(widget.currentWidget())

    def press_Converter(self,option):
        match option:
            #usar funcao de conversao
            #pegar texto inserido : { self.textboxInput.toPlainText()}
            #apos conversao: self.textboxOutput.setPlainText(-texto convertido-)
            #self.textboxOutput.setPlainText("IHIHIHIHIHI")
            case 1:
                conv = Conversor()
                data = conv.splitData(self.textboxInput.toPlainText())
                #print(self.textboxInput.toPlainText())
                conv.conversor(data)   
                self.textboxOutput.setPlainText(str(json.dumps(conv.documentData, indent=4)))
            case 3:
                conv = Conversor()
                data = conv.splitData(self.textboxInput.toPlainText())
                #print(self.textboxInput.toPlainText())
                conv.conversor(data)   
                self.textboxOutput.setPlainText(str(tYX.dictToYAML(conv.documentData,0)))
            case 4:
                conv = Conversor()
                data = conv.splitData(self.textboxInput.toPlainText())
                #print(self.textboxInput.toPlainText())
                conv.conversor(data)   
                self.textboxOutput.setPlainText(str(tYX.dict2xml(conv.documentData,1)))
            case 6:
                inp = self.textboxInput.toPlainText()
                self.textboxOutput.setPlainText(str(jTT.toml.dumps(jTT.parser.parse(inp))))
            case _:
                self.textboxOutput.setPlainText(". . .")
    
    def openFile(self):
        fname = qtw.QFileDialog.getOpenFileName(self, 'Abrir Ficheiro', 'c:\\',"All Files (*)")
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        if fname[0]!= '':
            f = open(fname[0])
            data = f.read()
            self.textboxInput.setPlainText(data)
        else:
            pass

    def saveFile(self,option):
        fname = qtw.QFileDialog.getSaveFileName(self, 'Guardar Ficheiro', 'c:\\',"All Files (*)")
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        if fname[0]!= '':
            if option == 1:
                with open(fname[0], "w") as write_file:
                    conv = Conversor()
                    data = conv.splitData(self.textboxInput.toPlainText())
                    #print(self.textboxInput.toPlainText())
                    conv.conversor(data)
                    json.dump(conv.documentData, write_file, indent=4)
        else:
            pass



def start():
    app = qtw.QApplication(sys.argv)
    global widget 
    widget = qtw.QStackedWidget()
    widget.setGeometry(500,100,1000,800)
    widget.setFixedSize(1000,800)
    widget.setWindowTitle("Trabalho Prático")
    mainWin = MainMenu()
    widget.addWidget(mainWin)
    widget.setCurrentWidget(mainWin)   # setting the page that you want to load when application starts up. you can also use setCurrentIndex(int)
    widget.show()
    sys.exit(app.exec_())

start()