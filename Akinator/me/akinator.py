import asyncio
import requests
from PyQt5 import QtWidgets, uic, QtGui, QtCore

from akinator import (
    CantGoBackAnyFurther,
    InvalidAnswer,
    AsyncAkinator,
    Answer,
    Theme,
)


class AkinatorWorker(QtCore.QThread):
    update_question_signal = QtCore.pyqtSignal(str)
    show_finish_screen_signal = QtCore.pyqtSignal(str, str, bytes)

    def __init__(self):
        super().__init__()
        self.aki = None
        self.loop = None
        self.answer = None
        self.back_button_pressed = False

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.run_akinator())

    async def run_akinator(self):
        self.aki = AsyncAkinator(
            child_mode=True,
            theme=Theme.from_str('characters'),
        )

        first_question = await self.aki.start_game()
        self.update_question_signal.emit(first_question)

        while self.aki.progression <= 80:
            if self.back_button_pressed:
                self.back_button_pressed = False
                try:
                    await self.aki.back()
                    print('went back 1 question')
                except CantGoBackAnyFurther:
                    print('cannot go back any further!')
            else:
                if self.answer is not None:
                    try:
                        answer = Answer.from_str(self.answer)
                    except InvalidAnswer:
                        print('Invalid answer')
                    else:
                        await self.aki.answer(answer)
                    self.answer = None

            next_question = self.aki.question
            self.update_question_signal.emit(next_question)

        first_guess = await self.aki.win()
        if first_guess:
            self.show_finish_screen_signal.emit(first_guess.name, first_guess.description, self.download_image(first_guess.absolute_picture_path))

    def set_answer(self, answer):
        self.answer = answer

    def set_back_button_pressed(self):
        self.back_button_pressed = True

    def download_image(self, url):
        response = requests.get(url)
        image_data = response.content
        return image_data


class AkinatorGUI:
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("./telas/Start.ui")
        self.tela_principal = uic.loadUi("./telas/Main.ui")
        self.tela_finish = uic.loadUi("./telas/Finish.ui")
        self.tela_inicial.show()

        self.tela_inicial.btnPlay.clicked.connect(self.play_game)

        self.tela_principal.btnYes.clicked.connect(self.handle_yes)
        self.tela_principal.btnNo.clicked.connect(self.handle_no)
        self.tela_principal.btnIdk.clicked.connect(self.handle_idk)
        self.tela_principal.btnPs.clicked.connect(self.handle_ps)
        self.tela_principal.btnPn.clicked.connect(self.handle_pn)
        self.tela_principal.btnBack.clicked.connect(self.handle_bk)

        self.worker = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.process_events)
        app.exec()

    def play_game(self):
        self.tela_inicial.hide()
        self.tela_principal.show()

        self.worker = AkinatorWorker()
        self.worker.update_question_signal.connect(self.update_question)
        self.worker.show_finish_screen_signal.connect(self.show_finish_screen)
        self.worker.finished.connect(self.worker_finished)
        self.worker.start()

        self.timer.start(0)

    def handle_yes(self):
        self.worker.set_answer('yes')

    def handle_no(self):
        self.worker.set_answer('no')

    def handle_idk(self):
        self.worker.set_answer('idk')

    def handle_ps(self):
        self.worker.set_answer('probably')

    def handle_pn(self):
        self.worker.set_answer('probably_not')

    def handle_bk(self):
        self.worker.set_back_button_pressed()

    def update_question(self, question):
        self.tela_principal.lbQuestion.setText(question)

    def show_finish_screen(self, name, description, image_data):
        self.tela_principal.hide()
        self.tela_finish.lbName.setText(name)
        self.tela_finish.lbSubName.setText(description)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image_data)
        self.tela_finish.lbImg.setPixmap(pixmap)
        self.tela_finish.show()

    def worker_finished(self):
        self.worker = None

    def process_events(self):
        QtCore.QCoreApplication.processEvents()


if __name__ == '__main__':
    gui = AkinatorGUI()
