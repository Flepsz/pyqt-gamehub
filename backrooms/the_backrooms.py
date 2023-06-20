from PyQt5 import QtWidgets, uic, QtMultimedia, QtCore
from PyQt5.QtCore import QUrl


def changetl(tohide, toshow):
    tohide.hide()
    toshow.show()


class Backrooms:
    def __init__(self):
        app = QtWidgets.QApplication([])

        self.scream_sound = None
        self.correct_sound = None
        self.error_sound = None
        self.die_sound = None
        self.paper_sound = None
        self.parabens37_sound = None
        self.parabens_sound = None
        self.key_sound = None

        self.jumpscares = 0
        self.loop_times = 1
        self.times_locker = 0
        self.times_key = 0
        self.has_key = False
        self.times_door = 0

        # Carregar a música de fundo
        self.player = QtMultimedia.QMediaPlayer()
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/ambient.wav")))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.player.setPlaylist(self.playlist)
        self.player.play()

        # Telas Level0

        # Menu
        self.tl_menu = uic.loadUi("./telas/Menu.ui")
        self.tl_menu.startBtn.clicked.connect(lambda: changetl(self.tl_menu, self.tl_home))
        self.tl_menu.quitBtn.clicked.connect(app.quit)
        # self.tl_menu.show()

        # Home
        self.tl_home = uic.loadUi("./telas/Home.ui")
        self.tl_home.loopBtn.clicked.connect(lambda: self.loop_chk(self.tl_home))
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
        self.tl_home2.loopBtn.clicked.connect(lambda: self.loop_chk(self.tl_home2))
        self.tl_home2.escapeBtn.clicked.connect(lambda: changetl(self.tl_home2, self.tl_arrows))
        self.tl_home2.scareBtn.clicked.connect(self.show_jumpscare1)
        self.tl_home2.hintBtn.clicked.connect(self.paper_puzz_enter)

        # Puzzle
        self.tl_puzz = uic.loadUi("./telas/Puzz1.ui")
        self.tl_puzz.exitBtn.clicked.connect(self.paper_puzz_exit)

        # Arrows
        self.tl_arrows = uic.loadUi("./telas/Arrows.ui")
        self.tl_arrows.backBtn.clicked.connect(lambda: changetl(self.tl_arrows, self.tl_home2))
        self.tl_arrows.escapeBtn.clicked.connect(lambda: changetl(self.tl_arrows, self.tl_toDoor))
        self.tl_arrows.dieBtn.clicked.connect(lambda: self.dietl(self.tl_arrows))

        # Die
        self.tl_die = uic.loadUi("./telas/Died.ui")
        self.tl_die.playagnBtn.clicked.connect(self.plyagn)

        # to Door
        self.tl_toDoor = uic.loadUi("./telas/toDoor.ui")
        self.tl_toDoor.backBtn.clicked.connect(lambda: changetl(self.tl_toDoor, self.tl_arrows))
        self.tl_toDoor.todoorBtn.clicked.connect(lambda: changetl(self.tl_toDoor, self.tl_door))
        self.tl_toDoor.tohomeBtn.clicked.connect(lambda: changetl(self.tl_toDoor, self.tl_home))

        # Door
        self.tl_door = uic.loadUi("./telas/Door.ui")
        self.tl_door.topasswordBtn.clicked.connect(lambda: changetl(self.tl_door, self.tl_locker))
        self.tl_door.backBtn.clicked.connect(lambda: changetl(self.tl_door, self.tl_toDoor))

        # Locker
        self.tl_locker = uic.loadUi("./telas/Locker.ui")
        self.tl_locker.presssenhaBtn.clicked.connect(self.test_password)
        self.tl_locker.backBtn.clicked.connect(lambda: changetl(self.tl_locker, self.tl_door))

        # Locker Wrong
        self.tl_lockerwrng = uic.loadUi("./telas/Lockerwrng.ui")
        self.tl_lockerwrng.okBtn.clicked.connect(lambda: changetl(self.tl_lockerwrng, self.tl_locker))

        # Door Accepted
        self.tl_dooracpt = uic.loadUi("./telas/Dooraccepted.ui")
        self.tl_dooracpt.openBtn.clicked.connect(lambda: changetl(self.tl_dooracpt, self.tl_abandoned))

        # Abandoned
        self.tl_abandoned = uic.loadUi("./telas/Abandoned.ui")
        self.tl_abandoned.loopBtn.clicked.connect(lambda: self.loop_chk(self.tl_abandoned))
        self.tl_abandoned.exitBtn.clicked.connect(lambda: changetl(self.tl_abandoned, self.tl_exit))

        # Exit lvl 0
        self.tl_exit = uic.loadUi("./telas/Exit.ui")
        self.tl_exit.exitBtn.clicked.connect(self.exit)

        # Telas Level37

        # Home37
        self.tl_home37 = uic.loadUi("./telas/Home37.ui")
        self.tl_home37.totunnelBtn.clicked.connect(lambda: changetl(self.tl_home37, self.tl_tunnel37))

        # Tunnel37
        self.tl_tunnel37 = uic.loadUi("./telas/Tunnel37.ui")
        self.tl_tunnel37.nextBtn.clicked.connect(lambda: changetl(self.tl_tunnel37, self.tl_bi37))
        self.tl_tunnel37.backBtn.clicked.connect(lambda: changetl(self.tl_tunnel37, self.tl_home37))

        # Biela37
        self.tl_bi37 = uic.loadUi("./telas/Bi37.ui")
        self.tl_bi37.tokeyBtn.clicked.connect(self.chk_key)
        self.tl_bi37.toexitBtn.clicked.connect(lambda: changetl(self.tl_bi37, self.tl_door37))
        self.tl_bi37.backBtn.clicked.connect(lambda: changetl(self.tl_bi37, self.tl_tunnel37))
        self.tl_bi37.show()

        # Key37
        self.tl_key37 = uic.loadUi("./telas/Key37.ui")
        self.tl_key37.keyBtn.clicked.connect(self.add_key)
        self.tl_key37.backBtn.clicked.connect(lambda: changetl(self.tl_key37, self.tl_bi37))

        # without Key37
        self.tl_wtkey37 = uic.loadUi("./telas/wtKey37.ui")
        self.tl_wtkey37.backBtn.clicked.connect(lambda: changetl(self.tl_wtkey37, self.tl_bi37))

        # Door exit37
        self.tl_door37 = uic.loadUi("./telas/Door37.ui")
        self.tl_door37.escapeBtn.clicked.connect(self.chk_key_door)
        self.tl_door37.backBtn.clicked.connect(lambda: changetl(self.tl_door37, self.tl_bi37))

        # wrong alert Door 37
        self.tl_door37wrng = uic.loadUi("./telas/Door37wng.ui")
        self.tl_door37wrng.okBtn.clicked.connect(lambda: changetl(self.tl_door37wrng, self.tl_door37))

        # Cangrats Window
        self.tl_congrats = uic.loadUi("./telas/Congrats.ui")
        self.tl_congrats.exitBtn.clicked.connect(app.quit)

        app.exec()
        
    def sounds(self):
        # Scream
        self.scream_sound = QtMultimedia.QMediaPlayer()
        self.scream_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/scream.wav")))

        # Correct
        self.correct_sound = QtMultimedia.QMediaPlayer()
        self.correct_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/correct.wav")))

        # Error
        self.error_sound = QtMultimedia.QMediaPlayer()
        self.error_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/error.wav")))

        # Die
        self.die_sound = QtMultimedia.QMediaPlayer()
        self.die_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/die.wav")))

        # Paper
        self.paper_sound = QtMultimedia.QMediaPlayer()
        self.paper_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/paper.wav")))

        # Parabens cororico
        self.parabens_sound = QtMultimedia.QMediaPlayer()
        self.parabens_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/parabens.wav")))

        # Key pickup sound
        self.key_sound = QtMultimedia.QMediaPlayer()
        self.key_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/key_pickup.wav")))

        # Parabeinsz
        self.parabens37_sound = QtMultimedia.QMediaPlayer()
        self.parabens37_sound.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/parabens37.wav")))

    def show_jumpscare(self):
        self.jumpscares += 1
        self.sounds()
        self.scream_sound.play()
        if self.jumpscares == 3:
            self.dietl(self.tl_home)
        else:
            self.tl_home.close()
            self.tl_Scare.show()
            QtCore.QTimer.singleShot(1000, self.close_jumscare)

    def close_jumscare(self):
        self.tl_Scare.close()
        self.tl_home.show()

    def show_jumpscare1(self):
        self.jumpscares += 1
        self.sounds()
        self.scream_sound.play()
        if self.jumpscares == 3:
            self.dietl(self.tl_home)
        else:
            self.tl_home2.close()
            self.tl_Scare1.show()
            QtCore.QTimer.singleShot(1000, self.close_jumscare1)

    def close_jumscare1(self):
        self.tl_Scare1.close()
        self.tl_home2.show()

    def dietl(self, window):
        window.close()
        self.sounds()
        self.die_sound.play()
        self.tl_die.show()

    def plyagn(self):
        self.jumpscares = 0
        self.loop_times = 1
        self.times_locker = 0
        self.times_key = 0
        self.has_key = False
        self.times_door = 0
        changetl(self.tl_die, self.tl_menu)

    def loop_chk(self, window):
        if self.loop_times == 2:
            self.sounds()
            self.scream_sound.play()
            window.close()
            self.tl_loop.show()
            self.loop_times += 1
        elif self.loop_times < 3:
            window.close()
            self.tl_loop.show()
            self.loop_times += 1
        else:
            self.dietl(window)

    def paper_puzz_enter(self):
        self.sounds()
        self.paper_sound.play()
        self.tl_home2.close()
        self.tl_puzz.show()

    def paper_puzz_exit(self):
        self.sounds()
        self.paper_sound.play()
        self.tl_puzz.close()
        self.tl_home2.show()

    def test_password(self):
        senha = self.tl_locker.senhaLe.text()
        if senha == "555":
            self.sounds()
            self.correct_sound.play()
            changetl(self.tl_locker, self.tl_dooracpt)
        else:
            self.times_locker += 1
            if self.times_locker == 3:
                self.sounds()
                self.scream_sound.play()
                self.dietl(self.tl_door)
            else:
                self.sounds()
                self.error_sound.play()
                changetl(self.tl_locker, self.tl_lockerwrng)

    def exit(self):
        self.sounds()
        self.parabens_sound.play()
        self.change_music()
        self.tl_exit.close()
        self.tl_home37.show()

    def add_key(self):
        self.has_key = True
        self.sounds()
        self.key_sound.play()
        self.tl_key37.close()
        self.tl_wtkey37.show()

    def chk_key(self):
        self.times_key += 1
        if self.times_key == 3:
            if self.has_key:
                self.tl_bi37.close()
                self.tl_wtkey37.show()
            else:
                self.tl_bi37.close()
                self.tl_key37.show()
        else:
            self.dietl(self.tl_bi37)

    def chk_key_door(self):
        if self.has_key:
            self.tl_door37.close()
            self.tl_congrats.show()
            self.sounds()
            self.parabens37_sound.play()
        else:
            self.times_door += 1
            if self.times_door == 3:
                self.dietl(self.tl_door37)
            else:
                self.tl_door37.close()
                self.tl_door37wrng.show()

    def change_music(self):
        # Parar a música atual
        self.player.stop()

        # Carregar e reproduzir uma nova música de fundo
        self.playlist.clear()
        self.playlist.addMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile("./img/fx/ambient37.wav")))
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.player.play()


if __name__ == '__main__':
    game = Backrooms()
