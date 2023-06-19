from PyQt5 import QtWidgets, uic, QtGui, QtMultimedia, QtCore
from PyQt5.QtCore import QUrl, Qt


def changetl(tohide, toshow):
    tohide.hide()
    toshow.show()


class Backrooms:
    def __init__(self):
        app = QtWidgets.QApplication([])


        # Carregar a música de fundo
        self.player = QtMultimedia.QMediaPlayer()
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/ambient.mp3")))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.player.setPlaylist(self.playlist)
        self.player.play()

        # Telas Level0

        # Menu
        self.tl_menu = uic.loadUi("./telas/Menu.ui")
        self.tl_menu.startBtn.clicked.connect(lambda: changetl(self.tl_menu, self.tl_home))
        self.tl_menu.quitBtn.clicked.connect(app.quit)
        self.tl_menu.show()

        # Home
        self.tl_home = uic.loadUi("./telas/Home.ui")
        self.tl_home.loopBtn.clicked.connect(lambda: changetl(self.tl_home, self.tl_loop))
        self.tl_home.escapeBtn.clicked.connect(lambda: changetl(self.tl_home, self.tl_home2))
        self.tl_home.scareBtn.clicked.connect(self.show_jumpscare)

        # Loop
        self.tl_loop = uic.loadUi("./telas/Loop.ui")
        self.tl_loop.homeBtn.clicked.connect(lambda: changetl(self.tl_loop, self.tl_home))

        # Jump Scares
        self.tl_Scare = uic.loadUi("./telas/Scare.ui")
        self.tl_Scare1 = uic.loadUi("./telas/Scare1.ui")

        # Home 2
        self.tl_home2 = uic.loadUi("./telas/Home2.ui")
        self.tl_home2.loopBtn.clicked.connect(lambda: changetl(self.tl_home2, self.tl_loop))
        self.tl_home2.escapeBtn.clicked.connect(lambda: changetl(self.tl_home2, self.tl_arrows))
        self.tl_home2.scareBtn.clicked.connect(self.show_jumpscare1)
        self.tl_home2.hintBtn.clicked.connect(lambda: changetl(self.tl_home2, self.tl_puzz))

        # Puzzle
        self.tl_puzz = uic.loadUi("./telas/Puzz1.ui")
        self.tl_puzz.exitBtn.clicked.connect(lambda: changetl(self.tl_puzz, self.tl_home2))

        # Arrows
        self.tl_arrows = uic.loadUi("./telas/Arrows.ui")
        self.tl_arrows.backBtn.clicked.connect(lambda: changetl(self.tl_arrows, self.tl_home2))
        self.tl_arrows.escapeBtn.clicked.connect(lambda: changetl(self.tl_arrows, self.tl_toDoor))
        self.tl_arrows.dieBtn.clicked.connect(lambda: self.dietl(self.tl_arrows))

        # Die
        self.tl_die = uic.loadUi("./telas/Died.ui")
        self.tl_die.playagnBtn.clicked.connect(lambda: changetl(self.tl_die, self.tl_menu))

        # to Door
        self.tl_toDoor = uic.loadUi("./telas/toDoor.ui")
        self.tl_toDoor.backBtn.clicked.connect(lambda: changetl(self.tl_toDoor, self.tl_arrows))
        self.tl_toDoor.todoorBtn.clicked.connect(lambda: changetl(self.tl_toDoor, self.tl_door))
        self.tl_toDoor.tohomeBtn.clicked.connect(lambda: changetl(self.tl_toDoor, self.tl_home))

        # Door
        self.tl_door = uic.loadUi("./telas/Door.ui")
        self.tl_door.topasswordBtn.clicked.connect(lambda: changetl(self.tl_door, self.tl_locker))

        # Locker
        self.tl_locker = uic.loadUi("./telas/Locker.ui")
        self.tl_locker.presssenhaBtn.clicked.connect(self.test_password)

        # Locker Wrong
        self.tl_lockerwrng = uic.loadUi("./telas/Lockerwrng.ui")
        self.tl_lockerwrng.okBtn.clicked.connect(lambda: changetl(self.tl_lockerwrng, self.tl_locker))

        # Door Accepted
        self.tl_dooracpt = uic.loadUi("./telas/Dooraccepted.ui")
        self.tl_dooracpt.openBtn.clicked.connect(lambda: changetl(self.tl_dooracpt, self.tl_abandoned))

        # Abandoned
        self.tl_abandoned = uic.loadUi("./telas/Abandoned.ui")
        self.tl_abandoned.loopBtn.clicked.connect(lambda: changetl(self.tl_abandoned, self.tl_loop))
        self.tl_abandoned.exitBtn.clicked.connect(lambda: changetl(self.tl_abandoned, self.tl_exit))

        # Exit lvl 0
        self.tl_exit = uic.loadUi("./telas/Exit.ui")
        # self.tl_exit.exitBtn.clicked.connect()




        app.exec()
        
    def sounds(self):
        # Scream
        self.scream_sound = QtMultimedia.QMediaPlayer()
        self.scream_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/scream.mp3")))
        
        # Correct
        self.correct_sound = QtMultimedia.QMediaPlayer()
        self.correct_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/correct.mp3")))
        
        # Error
        self.error_sound = QtMultimedia.QMediaPlayer()
        self.error_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/error.mp3")))

        # Die
        # Error
        self.die_sound = QtMultimedia.QMediaPlayer()
        self.die_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/die.mp3")))

    def show_jumpscare(self):
        self.tl_home.close()
        self.tl_Scare.show()
        self.sounds()
        self.scream_sound.play()
        QtCore.QTimer.singleShot(1000, self.close_jumscare)

    def close_jumscare(self):
        self.tl_Scare.close()
        self.tl_home.show()

    def show_jumpscare1(self):
        self.tl_home2.close()
        self.tl_Scare1.show()
        self.sounds()
        self.scream_sound.play()
        QtCore.QTimer.singleShot(1000, self.close_jumscare1)

    def close_jumscare1(self):
        self.tl_Scare1.close()
        self.tl_home2.show()

    def dietl(self, window):
        window.close()
        self.sounds()
        self.die_sound.play()
        self.tl_die.show()

    def test_password(self):
        self.sounds()
        senha = self.tl_locker.senhaLe.text()
        if senha == "555":
            self.correct_sound.play()
            changetl(self.tl_locker, self.tl_dooracpt)
        else:
            self.error_sound.play()
            changetl(self.tl_locker, self.tl_lockerwrng)

    def change_music(self):
        # Parar a música atual
        self.player.stop()

        # Carregar e reproduzir uma nova música de fundo
        self.playlist.clear()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/ambient37.mp3")))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.player.play()


if __name__ == '__main__':
    game = Backrooms()
