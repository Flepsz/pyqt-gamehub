from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton

class telas():
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("telas/inicial.ui")
        self.tela_texto = uic.loadUi("telas/texto.ui")
        self.tela_inicial.show()
        
        self.tela_inicial.mudar.clicked.connect(self.mudarTela)

        self.tela_inicial.siar.clicked.connect(self.sairPrograma)

        self.tela_texto.voltar.clicked.connect(self.voltarInicio)

        self.tela_texto.okB.clicked.connect(self.mudarTexto)

        app.exec()


    def mudarTela(self):
        self.tela_inicial.close()
        self.tela_texto.show()

    def sairPrograma(self):
        self.tela_inicial.close()

    def voltarInicio(self):
        self.tela_texto.close()
        self.tela_inicial.show()

    def mudarTexto(self):
        textoBacana = self.tela_texto.inputT.text()
        self.tela_texto.sim.setText(textoBacana)
        self.tela_texto.inputT.setText("")

    
if __name__ == '__main__':
    c = telas()