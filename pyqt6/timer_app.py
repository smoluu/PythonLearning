from PyQt6.QtGui import QIcon
from PyQt6.QtCore  import QTimer, QTime
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QGridLayout
import sys
import os

class MyApp(QWidget):
    def  __init__(self):
        super().__init__()
        self.title = "Timer app"
        self.screenWidth = 500
        self.screenHeight = 300
        self.timer = QTimer()
        self.timer.timeout.connect(self.keepTime)
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.time = QTime(0,0,0)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Timer app")
        self.setWindowIcon(QIcon("icon.ico"))
        self.resize(self.screenWidth, self.screenHeight)
        layout = QGridLayout()
        self.setLayout(layout)

        # output box
        self.hBox = QTextEdit()
        self.mBox = QTextEdit()
        self.sBox = QTextEdit()
        self.hBox.setText("00")
        self.mBox.setText("00")
        self.sBox.setText("00")
        self.hBox.setStyleSheet("font-size: 120px")
        self.mBox.setStyleSheet("font-size: 120px")
        self.sBox.setStyleSheet("font-size: 120px")
        
        # buttons
        self.hUpBtn = QPushButton("▲")
        self.hDownBtn = QPushButton("▼")
        self.mUpBtn = QPushButton("▲")
        self.mDownBtn = QPushButton("▼")
        self.sUpBtn = QPushButton("▲")
        self.sDownBtn = QPushButton("▼")
        
        # Using lambda functions to connect the buttons
        self.hUpBtn.clicked.connect(lambda: self.time.addSecs(60*60))
        self.hDownBtn.clicked.connect(lambda: self.time.addSecs(-60*60))
        self.mUpBtn.clicked.connect(lambda: self.time.addSecs(60))
        self.mDownBtn.clicked.connect(lambda: self.time.addSecs(-60))
        self.sUpBtn.clicked.connect(lambda: self.time.addSecs(1))
        self.sDownBtn.clicked.connect(lambda: self.time.addSecs(-1))

        self.startBtn = QPushButton("Start")
        self.startBtn.clicked.connect(self.startTime)
        self.pauseBtn = QPushButton("Pause")
        self.pauseBtn.clicked.connect(self.pauseTime)


        layout.addWidget(self.hUpBtn,0,0,1,1) 
        layout.addWidget(self.mUpBtn,0,1,1,1)
        layout.addWidget(self.sUpBtn,0,2,1,1)

        layout.addWidget(self.hBox,1,0,1,1)
        layout.addWidget(self.mBox,1,1,1,1)
        layout.addWidget(self.sBox,1,2,1,1)
        
        layout.addWidget(self.hDownBtn,2,0,1,1) 
        layout.addWidget(self.mDownBtn,2,1,1,1) 
        layout.addWidget(self.sDownBtn,2,2,1,1)


        layout.addWidget(self.startBtn,3,0)
        layout.addWidget(self.pauseBtn,3,1)


    def startTime(self):
        h = int(self.hBox.toPlainText())
        m = int(self.mBox.toPlainText())
        s = int(self.sBox.toPlainText())

        if None not in (h,m,s):
            self.time = QTime(h,m,s)
             
        self.timer.start(1000)
        self.keepTime()

    def pauseTime(self):

        self.timer.stop()
        
    def keepTime(self):
        self.hBox.setText(self.time.toString("HH"))
        self.mBox.setText(self.time.toString("mm"))
        self.sBox.setText(self.time.toString("ss"))
        if self.timer.isActive():
            self.time = self.time.addSecs(-1)

    def endTime(self):
        pass

def main():
    app = QApplication(sys.argv)
    
    window = MyApp()
    window.show()

    app.exec()



if __name__ == "__main__":
    print(os.getcwd())
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
    
