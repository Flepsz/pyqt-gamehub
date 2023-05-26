from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QMainWindow, QDialog, QApplication
from inicial import Ui_Dialog
import sys

#class telas(QDialog, Ui_Dialog):
#    def __init__(self):
#        super().__init__()
#        super().setupUi(self)
        
#if __name__ == '__main__':
#    qtJanelas = QApplication(sys.argv)
#    qtJanelas.setStyle('Fusion')
#    telasLegal = telas()
#    
#    telasLegal.show()
#    sys.exit(qtJanelas.exec())


class telas(Ui_Dialog):
    def __init__(self, Dialog):
        super().__init__()
        #super().setupUi(Dialog)
        self.setupUi(Dialog)


if __name__ == '__main__':
    qtJanelas = QApplication(sys.argv)
    qtJanelas.setStyle('Fusion')

    Dialog = QtWidgets.QDialog()
    telasLegal = telas(Dialog)
    
    Dialog.show()
    sys.exit(qtJanelas.exec())