from PyQt5 import QtWidgets, uic
from akinator import CantGoBackAnyFurther, InvalidAnswer, Akinator, Answer, Theme


class AkinatorGUI:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("Start.ui")
        self.tela_principal = uic.loadUi("Main.ui")
        self.tela_inicial.show()

        self.akinator = Akinator(child_mode=True, theme=Theme.from_str('characters'))

        self.tela_inicial.btnPlay.clicked.connect(self.play_game)

        self.tela_principal.btnYes.clicked.connect(self.handle_yes)
        self.tela_principal.btnNo.clicked.connect(self.handle_no)
        self.tela_principal.btnIdk.clicked.connect(self.handle_idk)
        self.tela_principal.btnPs.clicked.connect(self.handle_ps)
        self.tela_principal.btnPn.clicked.connect(self.handle_pn)

        app.exec()

    def play_game(self):
        self.tela_inicial.close()
        self.start_game()

    def start_game(self):
        self.tela_principal.show()
        first_question = self.akinator.start_game()
        self.tela_principal.lblQuestion.setText(first_question)
        self.tela_principal.show()

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

    def ask_question(self):
        self.tela_principal.lbQuestion.setText(self.akinator.question)

    def end_game(self):
        self.tela_principal.close()
        first_guess = self.akinator.win()

        if first_guess:
            print('Name:', first_guess.name)
            print('Description:', first_guess.description)
            print('Image:', first_guess.absolute_picture_path)


if __name__ == '__main__':
    akinator_gui = AkinatorGUI()
