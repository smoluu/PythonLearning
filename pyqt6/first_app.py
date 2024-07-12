from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit,QVBoxLayout
import sys
import os

class MyApp(QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("Hello app")
        self.setWindowIcon(QIcon("icon.ico"))
        self.resize(500, 350) #width,height
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        #widgets
        self.inputfield = QLineEdit()
        # run sayHello when you press Enter in inputfield
        self.inputfield.returnPressed.connect(self.sayHello)
        
        button = QPushButton("&Say hello")
        button.clicked.connect(self.sayHello)
        
        # output box
        self.output = QTextEdit()

        layout.addWidget(self.inputfield)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        inputText = self.inputfield.text()
        self.output.setText("hello {0}".format(inputText))

def main():
    app = QApplication(sys.argv)
    
    window = MyApp()
    window.show()

    app.exec()



if __name__ == "__main__":
    print(os.getcwd())
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
    
