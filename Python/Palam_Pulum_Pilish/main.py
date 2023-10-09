
import sys
from PySide6.QtWidgets import QApplication , QMainWindow
from ui_gameboard import Ui_MainWindow

class Mainwindow ( QMainWindow ):

    def __init__ ( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)

app = QApplication ( sys.argv )
window = Mainwindow ()
window.show ()
app.exec ()