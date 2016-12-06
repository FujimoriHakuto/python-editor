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
    self.setWindowTitle("Qt Text Text Sample")