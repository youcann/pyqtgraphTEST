from PyQt4 import QtGui
import sys

import pyqtgraph

def mainWindow():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b=QtGui.QLabel(w)
    b.setText("TEST")
    w.setGeometry(100,100,200,50)
    b.move(50,20)
    w.setWindowTitle("RapidScanCANinterface Qt (v0.1)")
    w.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
   mainWindow()