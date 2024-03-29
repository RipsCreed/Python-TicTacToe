from PyQt5 import QtCore, QtGui, QtWidgets
from new_window import Ui_SecondWindow

class Ui_tictactoe(object):
    def openWindow(self, message):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow(message)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, tictactoe):
        self.symbol = "X"
        tictactoe.setObjectName("tictactoe")
        tictactoe.resize(319, 329)
        tictactoe.setStyleSheet("background-color: cyan;")
        self.centralwidget = QtWidgets.QWidget(tictactoe)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 20, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 20, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 120, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 120, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 120, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 220, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 220, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 220, 75, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: white; border: 1px solid;")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        tictactoe.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tictactoe)
        self.statusbar.setObjectName("statusbar")
        tictactoe.setStatusBar(self.statusbar)

        self.locations = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.location = {
            "A1": self.pushButton,
            "A2": self.pushButton_4,
            "A3": self.pushButton_7,

            "B1": self.pushButton_2,
            "B2": self.pushButton_5,
            "B3": self.pushButton_8,

            "C1": self.pushButton_3,
            "C2": self.pushButton_6,
            "C3": self.pushButton_9
        }

        self.pushButton.clicked.connect(self.Bir)
        self.pushButton_2.clicked.connect(self.Iki)
        self.pushButton_3.clicked.connect(self.Uc)    
        self.pushButton_4.clicked.connect(self.Dort)
        self.pushButton_5.clicked.connect(self.Bes)
        self.pushButton_6.clicked.connect(self.Alti)
        self.pushButton_7.clicked.connect(self.Yedi)
        self.pushButton_8.clicked.connect(self.Sekiz)
        self.pushButton_9.clicked.connect(self.Dokuz)

        self.retranslateUi(tictactoe)
        QtCore.QMetaObject.connectSlotsByName(tictactoe)

    def Bir(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("A1", "X") != False:
                    self.Put_Symbol("A1", "X")
                    self.symbol = "O"
                    self.Control()
        

            elif self.symbol == "O":
                if self.Put_Symbol("A1", "O") != False:
                    self.Put_Symbol("A1", "O")
                    self.symbol = "X"
                    self.Control()

    def Iki(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("B1", "X") != False:        
                    self.Put_Symbol("B1", "X")
                    self.symbol = "O"
                    self.Control()

            elif self.symbol == "O":
                if self.Put_Symbol("B1", "O") != False:
                    self.Put_Symbol("B1", "O")
                    self.symbol = "X"
                    self.Control()

    def Uc(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("C1", "X") != False:
                    self.Put_Symbol("C1", "X")
                    self.symbol = "O"
                    self.Control()

            elif self.symbol == "O":
                if self.Put_Symbol("C1", "O") != False:
                    self.Put_Symbol("C1", "O")
                    self.symbol = "X"
                    self.Control()

    def Dort(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("A2", "X") != False:
                    self.Put_Symbol("A2", "X")
                    self.symbol = "O"
                    self.Control()

            elif self.symbol == "O":
                if self.Put_Symbol("A2", "O") != False:
                    self.Put_Symbol("A2", "O")
                    self.symbol = "X"
                    self.Control()

    def Bes(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("B2", "X") != False:

                    self.Put_Symbol("B2", "X")
                    self.symbol = "O"
                    self.Control()

            elif self.symbol == "O":
                if self.Put_Symbol("B2", "O") != False:
                    self.Put_Symbol("B2", "O")
                    self.symbol = "X"
                    self.Control()

    def Alti(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("C2", "X") != False:
                    self.Put_Symbol("C2", "X")
                    self.symbol = "O"
                    self.Control()

            elif self.symbol == "O":
                if self.Put_Symbol("C2", "O") != False:
                    self.Put_Symbol("C2", "O")
                    self.symbol = "X"
                    self.Control()

    def Yedi(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("A3", "X") != False:
                    self.Put_Symbol("A3", "X")
                    self.symbol = "O"
                    self.Control()

            elif self.symbol == "O":
                if self.Put_Symbol("A3", "O") != False:
                    self.Put_Symbol("A3", "O")
                    self.symbol = "X"
                    self.Control()

    def Sekiz(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("B3", "X") != False:
                    self.Put_Symbol("B3", "X")
                    self.symbol = "O"
                    self.Control()

            elif self.symbol == "O":
                if self.Put_Symbol("B3", "O") != False:
                    self.Put_Symbol("B3", "O")
                    self.symbol = "X"
                    self.Control()

    def Dokuz(self):
        if self.Control() == False:
            if self.symbol == "X":
                if self.Put_Symbol("C3", "X") != False:
                    self.Put_Symbol("C3", "X")
                    self.symbol = "O"
                    self.Control()

            elif self.symbol == "O":
                if self.Put_Symbol("C3", "O") != False:
                    self.Put_Symbol("C3", "O")
                    self.symbol = "X"
                    self.Control()

    def Put_Symbol(self, location, symbol):

        if self.location[location].text() == "":
            self.location[location].setText(symbol)

        elif self.location[location].text() != "":
            return False

    def Control(self):
        #* A1 B1 C1 --- A2 B2 C2 --- A3 B3 C3 --- A1 A2 A3 --- B1 B2 B3 --- C1 C2 C3 --- A1 B2 C3 --- A3 B2 C1

        if self.pushButton.text() == self.pushButton_2.text() == self.pushButton_3.text() != "": # A1 B1 C1
            if self.pushButton.text() == self.pushButton_2.text() == self.pushButton_3.text() == "X":
                self.openWindow("X Kazandı 🎉")
                return True
            
            elif self.pushButton.text() == self.pushButton_2.text() == self.pushButton_3.text() == "O":
                self.openWindow("O Kazandı 🎉")
                return True      

        elif self.pushButton_4.text() == self.pushButton_5.text() == self.pushButton_6.text() != "": # A2 B2 C2
            if self.pushButton_4.text() == self.pushButton_5.text() == self.pushButton_6.text() == "X":
                self.openWindow("X Kazandı 🎉")
                return True
            
            elif self.pushButton_4.text() == self.pushButton_5.text() == self.pushButton_6.text() == "O":
               self.openWindow("O Kazandı 🎉")
               return True

        elif self.pushButton_7.text() == self.pushButton_8.text() == self.pushButton_9.text() != "": # A3 B3 C3
            if self.pushButton_7.text() == self.pushButton_8.text() == self.pushButton_9.text() == "X":
                self.openWindow("X Kazandı 🎉")
                return True

            elif self.pushButton_7.text() == self.pushButton_8.text() == self.pushButton_9.text() == "O":
               self.openWindow("O Kazandı 🎉")
               return True

        elif self.pushButton.text() == self.pushButton_4.text() == self.pushButton_7.text() != "": # A1 A2 A3
            if self.pushButton.text() == self.pushButton_4.text() == self.pushButton_7.text() == "X":
                self.openWindow("X Kazandı 🎉")
                return True

            elif self.pushButton.text() == self.pushButton_4.text() == self.pushButton_7.text() == "O":
                self.openWindow("O Kazandı 🎉")
                return True

        elif self.pushButton_2.text() == self.pushButton_5.text() == self.pushButton_8.text() != "":
            if self.pushButton_2.text() == self.pushButton_5.text() == self.pushButton_8.text() == "X":
                self.openWindow("X Kazandı 🎉")
                return True

            elif self.pushButton_2.text() == self.pushButton_5.text() == self.pushButton_8.text() == "O":
                self.openWindow("O Kazandı 🎉")
                return True

        elif self.pushButton_3.text() == self.pushButton_6.text() == self.pushButton_9.text() != "":
            if self.pushButton_3.text() == self.pushButton_6.text() == self.pushButton_9.text() == "X":
                self.openWindow("X Kazandı 🎉")
                return True
            
            elif self.pushButton_3.text() == self.pushButton_6.text() == self.pushButton_9.text() == "O":
                self.openWindow("O Kazandı 🎉")
                return True

        elif self.pushButton.text() == self.pushButton_5.text() == self.pushButton_9.text() != "":
            if self.pushButton.text() == self.pushButton_5.text() == self.pushButton_9.text() == "X":
                self.openWindow("X Kazandı 🎉")
                return True

            elif self.pushButton.text() == self.pushButton_5.text() == self.pushButton_9.text() == "O":
                self.openWindow("O Kazandı 🎉")
                return True

        elif self.pushButton_3.text() == self.pushButton_5.text() == self.pushButton_7.text() != "":
            if self.pushButton_3.text() == self.pushButton_5.text() == self.pushButton_7.text() == "X":
                self.openWindow("X Kazandı 🎉")
                return True

            elif self.pushButton_3.text() == self.pushButton_5.text() == self.pushButton_7.text() == "O":
                self.openWindow("O Kazandı 🎉")
                return True
            
        elif self.pushButton.text() != "" and self.pushButton_2.text() != "" and self.pushButton_3.text() != "" and self.pushButton_4.text() != "" and self.pushButton_5.text() != "" and self.pushButton_6.text() != "" and self.pushButton_7.text() != "" and self.pushButton_8.text() != "" and self.pushButton_9.text() != "":
            self.openWindow("Berabere")
            
        else:
            return False



    def retranslateUi(self, tictactoe):
        _translate = QtCore.QCoreApplication.translate
        tictactoe.setWindowTitle(_translate("tictactoe", "TicTacToe"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tictactoe()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())