from PIL import ImageGrab
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QLabel, QLineEdit, QTextEdit, QGridLayout, qApp, QDialog, QFileDialog,\
    QMenuBar, QMenu, QMainWindow, QAction, QStatusBar, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import pygame
import time

f = open('data.txt','r')
st = f.readlines()
directory = st[3]
name = st[0][0:(len(st[0])-1)]
line = int(st[2][0:(len(st[2])-1)])
num = st[1][0:(len(st[1])-1)]
f.close()

def rewrite():
    global num
    global directory
    global line
    global name

    f = open('data.txt','w')
    f.writelines(name + '\n' + num + '\n' +str(line) + '\n'+ directory)
    f.close()

def ggrab():
    global line
    global directory
    global name
    global num
    bbox = (110, 52, 1390, 1005)
    line += 1
    rewrite()
    im = ImageGrab.grab(bbox)
    im.save(directory + '/' + name + num +str(line) + '.png')
    file = '8858.mp3'
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.music.stop()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.statusBar()

        btn = QPushButton('Capture!', self)
        btn.setToolTip('For online courses')
        btn.resize(120, 50)
        btn.move(90, 50)
        btn.clicked.connect(ggrab)

        btn2 = QPushButton('Quit', self)
        btn2.setToolTip('Click here to quit')
        btn2.resize(80,30)
        btn2.move(110, 110)
        btn2.clicked.connect(qApp.quit)

        self.le = QTextEdit(directory, self)
        self.le.move(10, 180)
        self.le.setFocusPolicy(Qt.NoFocus)
        self.le.setFont(QFont('', 15, QFont.Bold))
        self.le.resize(270, 100)

        seleAct = QAction('Select Path', self)
        seleAct.setShortcut('Ctrl+S')
        seleAct.setStatusTip('Select the Path for Saving')
        seleAct.triggered.connect(self.select)

        
        numAct = QAction('Course Number', self)
        numAct.triggered.connect(self.courNum)

        nameAct = QAction('Courses Name', self)
        nameAct.triggered.connect(self.courName)
        

        courMenu = QMenu('Setting', self)
        courMenu.addAction(nameAct)
        courMenu.addAction(numAct)

        menubar = self.menuBar()
        setmenu = menubar.addMenu('Option')
        setmenu.addAction(seleAct)
        setmenu.addMenu(courMenu)

        
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(305, 350)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('ScreenCapture')
        self.show()





    def select(self):

        global directory 
        directory = QFileDialog.getExistingDirectory(self, 'Select the Path', 'd:/')
        if directory:
            self.le.setText(str(directory))
            rewrite()
        else:
            QMessageBox.information(self, 'Alert', 'Select nothing')


    def courNum(self):
        global line
        global name
        global num
        text, ok = QInputDialog.getText(self, 'Course Number', 'Number:')

        if ok:
            line = 0
            num = text+'.'
            rewrite()


    def courName(self):
        global name
        text, ok = QInputDialog.getText(self, 'Course Name', 'Name:')

        if ok:
            line = 0
            name = text
            rewrite()
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


