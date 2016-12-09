#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class UI(QMainWindow):
  def __init__(self):
    super(UI, self).__init__()
    self.initUI()
    
    
  def initUI(self):
    self.setGeometry(300,300,250,150)
    self.setWindowTitle("Qt Text Editor")
    
    self.w = QWidget()
    
    self.text = QTextEdit(self)
    hbox = QHBoxLayout()
    hbox.addWidget(self.text)
    
    self.w.setLayout(hbox)
    self.setCentralWidget(self.w)
    self.statusBar().showMessage("hello!")
    self.show()
        
    
def main():
  app = QApplication(sys.argv)
  ui = UI()
  sys.exit(app.exec_())
  
  
if __name__ == "__main__":
  main()