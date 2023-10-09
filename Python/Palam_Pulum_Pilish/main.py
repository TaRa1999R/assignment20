
import sys
from PySide6.QtWidgets import QApplication , QMainWindow
from ui_Palam_Pulum_Plish import Ui_MainWindow

class Mainwindow ( QMainWindow ):

    def __init__ ( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)
        self.ui.back1.setText ("🤚🏻")
        self.ui.back2.setText ("🤚🏻")
        self.ui.front1.setText ("✋🏻")
        self.ui.front2.setText ("✋🏻")
        self.ui.player.setChecked (True)

app = QApplication ( sys.argv )
window = Mainwindow ()
window.show ()
app.exec ()