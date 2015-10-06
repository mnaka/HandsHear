# A Gui for Hands Hear

import sys
from PyQt4.QtGui import *
from MainWindow import Ui_MainWindow

class Editor(QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex =  Editor()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()


