import sys
from PyQt5 import QtWidgets, uic
from akinator import CantGoBackAnyFurther, InvalidAnswer, Akinator, Answer, Theme


class Janela:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("Start.ui")
        self.tela_principal = uic.loadUi("Main.ui")
        self.tela_inicial.show()
        self.answer = ''

        self.akinator = Akinator(child_mode=True, theme=Theme.from_str('characters'))

        self.tela_inicial.btnPlay.clicked.connect(self.play_game)

        self.tela_principal.btnYes.clicked.connect()
        self.tela_principal.btnNo.clicked.connect()
        self.tela_principal.btnIdk.clicked.connect()
        self.tela_principal.btnPs.clicked.connect()
        self.tela_principal.btnPn.clicked.connect()
        app.exec()

    def handle_yes(self):
        try:
            self.akinator.answer(Answer.YES)
            self.ask_question()
        except CantGoBackAnyFurther:
            self.end_game()

    def handle_no(self):
        try:
            self.akinator.answer(Answer.NO)
            self.ask_question()
        except CantGoBackAnyFurther:
            self.end_game()

    def handle_idk(self):
        try:
            self.akinator.answer(Answer.DONT_KNOW)
            self.ask_question()
        except CantGoBackAnyFurther:
            self.end_game()

    def handle_ps(self):
        try:
            self.akinator.answer(Answer.PROBABLY)
            self.ask_question()
        except CantGoBackAnyFurther:
            self.end_game()

    def handle_pn(self):
        try:
            self.akinator.answer(Answer.PROBABLY_NOT)
            self.ask_question()
        except CantGoBackAnyFurther:
            self.end_game()


    def play_game(self):
        self.tela_inicial.close()
        self.tela_principal.show()
        asyncio.run(self.test())



    



if __name__ == '__main__':
    a = Janela()
    # asyncio.run(test())
