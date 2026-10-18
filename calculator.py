import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QGridLayout,QPushButton, QLabel
from PySide6.QtGui import QPalette, QColor
from layout_colorwidget import Color




    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.equation = []
        
        self.current_text = ""
        self.setWindowTitle("calc")

        layout1 = QVBoxLayout()


        self.textbox = QLabel(self.current_text)
        layout1.addWidget(self.textbox)
        self.textbox.setStyleSheet("""
            QLabel {
                border: 2px solid #FFEE8C;
                padding: 20px;
                background-color:
            }
        """)

        layout1.setSpacing(1)
        layout2 = QGridLayout()

      
        acbutton = QPushButton("AC")
        acbutton.clicked.connect(self.AC)
        layout2.addWidget(acbutton)

        sevenbutton = QPushButton("7")
        sevenbutton.clicked.connect(self.seven)
        layout2.addWidget(sevenbutton)

        fourbutton = QPushButton("4")
        fourbutton.clicked.connect(self.four)
        layout2.addWidget(fourbutton)

        onebutton = QPushButton("1")
        onebutton.clicked.connect(self.one)
        layout2.addWidget(onebutton)

        zerobutton = QPushButton("0")
        zerobutton.clicked.connect(self.zero)
        layout2.addWidget(zerobutton)

        bracketbutton = QPushButton("()")
        bracketbutton.clicked.connect(self.bracket)
        layout2.addWidget((bracketbutton),0,1)

        eightbutton = QPushButton("8")
        eightbutton.clicked.connect(self.eight)
        layout2.addWidget((eightbutton),1,1)

        fivebutton = QPushButton("5")
        fivebutton.clicked.connect(self.five)
        layout2.addWidget((fivebutton),2,1)

        twobutton = QPushButton("2")
        twobutton.clicked.connect(self.two)
        layout2.addWidget((twobutton),3,1)

        decimalbutton = QPushButton(".")
        decimalbutton.clicked.connect(self.decimal)
        layout2.addWidget((decimalbutton),4,1)

        modbutton = QPushButton("%")
        modbutton.clicked.connect(self.mod)
        layout2.addWidget((modbutton),0,2)

        ninebutton = QPushButton("9")
        ninebutton.clicked.connect(self.nine)
        layout2.addWidget((ninebutton),1,2)

        sixbutton = QPushButton("6")
        sixbutton.clicked.connect(self.six)
        layout2.addWidget((sixbutton),2,2)

        threebutton = QPushButton("3")
        threebutton.clicked.connect(self.three)
        layout2.addWidget((threebutton),3,2)

        delbutton = QPushButton("del")
        delbutton.clicked.connect(self.delete)
        layout2.addWidget((delbutton),4,2)

        dividebutton = QPushButton("/")
        dividebutton.clicked.connect(self.divide)
        layout2.addWidget((dividebutton),0,3)

        multiplybutton = QPushButton("X")
        multiplybutton.clicked.connect(self.multiply)
        layout2.addWidget((multiplybutton),1,3)

        subtractbutton = QPushButton("-")
        subtractbutton.clicked.connect(self.subtract)
        layout2.addWidget((subtractbutton),2,3)

        addbutton = QPushButton("+")
        addbutton.clicked.connect(self.add)
        layout2.addWidget((addbutton),3,3)

        execbutton = QPushButton("=")
        execbutton.clicked.connect(self.exec_equation)
        layout2.addWidget((execbutton),4,3)

        layout1.addLayout(layout2)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def decimal(self):
        self.current_text += "."
        self.textbox.setText(self.current_text)
        self.equation.append(".")

    def mod(self):
        self.current_text += "%"
        self.textbox.setText(self.current_text)
        self.equation.append("%")

    def nine(self):
        self.current_text += "9"
        self.textbox.setText(self.current_text)
        self.equation.append(9)

    def six(self):
        self.current_text += "6"
        self.textbox.setText(self.current_text)
        self.equation.append(6)

    def three(self):
        self.current_text += "3"
        self.textbox.setText(self.current_text)
        self.equation.append(3)

    def delete(self):
        self.current_text = self.current_text[:-1]
        self.textbox.setText(self.current_text)
        stringconvert = str(self.equation[-1])
        self.equation[-1] = stringconvert[:-1]

    def divide(self):
        self.current_text += "/"
        self.textbox.setText(self.current_text)
        self.equation.append("/")

    def subtract(self):
        self.current_text += "-"
        self.textbox.setText(self.current_text)
        self.equation.append("-")

    def add(self):
        self.current_text += "+"
        self.textbox.setText(self.current_text)
        self.equation.append("+")
        
    def AC(self):
        self.current_text = ""
        self.textbox.setText(self.current_text)
        self.equation.clear()
        return self.equation

    def seven(self): 
        self.current_text += "7"
        self.textbox.setText(self.current_text)
        self.equation.append(7)
        return self.equation

    def four(self):
        self.current_text += "4"
        self.textbox.setText(self.current_text)
        self.equation.append(4)
        return self.equation

    def one(self):
        self.current_text += "1"
        self.textbox.setText(self.current_text)
        self.equation.append(1)
        return self.equation

    def zero(self):
        self.current_text += "0"
        self.textbox.setText(self.current_text)
        self.equation.append(0)
        return self.equation

    def multiply(self):
        self.current_text += "x"
        self.textbox.setText(self.current_text)
        self.equation.append("*")

    def eight(self):
        self.current_text += "8"
        self.textbox.setText(self.current_text)
        self.equation.append(8)

    def five(self):
        self.current_text += "5"
        self.textbox.setText(self.current_text)
        self.equation.append(5)

    def two(self):
        self.current_text += "2"
        self.textbox.setText(self.current_text)
        self.equation.append(2)

    def bracket(self):
    
        open_count = self.equation.count("(")
        close_count = self.equation.count(")")

        if open_count > close_count:
            self.current_text += ")"
            self.equation.append(")")
        else:
            self.current_text += "("
            self.equation.append("(")

        self.textbox.setText(self.current_text)
        return self.equation
    

    def exec_equation(self):
        try:
            res = ""

            for i in range(len(self.equation)):
                res += str(self.equation[i])

            res = eval(res)
            self.current_text = str(res)
            self.textbox.setText(str(res))
            self.equation.clear()
            self.equation.append(res)
        except Exception:
            self.textbox.setText("error")
            self.current_text = "" 
            self.equation.clear()
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()