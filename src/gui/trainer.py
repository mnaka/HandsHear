# This python file defines the user interface used to train
# databases and input commands

import sys
from PyQt4 import QtGui

class GUI(QtGui.QMainWindow):
    
    def __init__(self):
        super(GUI, self).__init__()
        
        self.initUI()

    def initUI(self):
       
        # Open database file
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open a learning database')
        openFile.triggered.connect(self.loadFile)
         
        # Exiting
        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        
        # Menubar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(exitAction)

        # Initial Shape of Window and Position
        self.resize(550, 350)
        self.center()
        
       
        self.setWindowTitle('Leap Commander')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def loadFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        f = open(fname, 'r')

def main():

    application = QtGui.QApplication(sys.argv)
    ex = GUI()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
