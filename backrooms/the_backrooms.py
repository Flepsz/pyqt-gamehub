from PyQt5 import QtWidgets, uic, QtGui, QtCore


class Backrooms:
    def __init__(self):
        app = QtWidgets.QApplication([])
        # Telas Level0

        # Menu
        self.tl_menu = uic.loadUi("./telas/Menu.ui")
        self.tl_menu.startBtn.clicked.connect()
        self.tl_menu.quitBtn.clicked.connect()

        # Home
        self.tl_home = uic.loadUi("./telas/Home.ui")
        self.tl_home.loopBtn.clicked.connect()
        self.tl_home.escapeBtn.clicked.connect()
        self.tl_home.scareBtn.clicked.connect()

        # Loop
        self.tl_loop = uic.loadUi("./telas/Loop.ui")
        self.tl_loop.HomeBtn.clicked.connect()

        # Jump Scares
        self.tl_Scare = uic.loadUi("./telas/Scare.ui")
        self.tl_Scare1 = uic.loadUi("./telas/Scare1.ui")

        # Home 2
        self.tl_home2 = uic.loadUi("./telas/Home2.ui")
        self.tl_home2.loopBtn.clicked.connect()
        self.tl_home2.escapeBtn.clicked.connect()
        self.tl_home2.scareBtn.clicked.connect()
        self.tl_home2.hintBtn.clicked.connect()

        # Puzzle
        self.tl_puzz = uic.loadUi("./telas/Puzz.ui")
        self.tl_puzz.exitBtn.clicked.connect()

        # Arrows
        self.tl_arrows = uic.loadUi("./telas/Arrows.ui")
        self.tl_arrows.backBtn.clicked.connect()
        self.tl_arrows.escapeBtn.clicked.connect()
        self.tl_arrows.dieBtn.clicked.connect()

        # Die
        self.tl_die = uic.loadUi("./telas/Died.ui")
        self.tl_die.plagnBtn.clicked.connect()

        # to Door
        self.tl_toDoor = uic.loadUi("./telas/toDoor.ui")
        self.tl_toDoor.backBtn.clicked.connect()
        self.tl_toDoor.todoorBtn.clicked.connect()
        self.tl_toDoor.tohomeBtn.clicked.connect()

        #

        app.exec()
