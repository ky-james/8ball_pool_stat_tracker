from PyQt5.QtWidgets import *


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window
        self.setStyleSheet("background-color: rgb(0, 76, 153);")
        self.setWindowTitle("Pool Stat Tracker - Home Screen")
        self.setGeometry(100, 0, 1200, 800)

        # title background
        self.titleBackgroundLabel = QLabel("", self)
        self.titleBackgroundLabel.resize(1200, 200)
        self.titleBackgroundLabel.setStyleSheet("background-color: white;"
                                                "font-size: 80px;")
        self.titleBackgroundLabel.move(0, 0)

        # title label
        self.titleLabel = QLabel("Pool Stat Tracker", self)
        self.titleLabel.resize(1200, 200)
        self.titleLabel.setStyleSheet("color: rgb(0, 76, 153);"
                                      "background-color: transparent;"
                                      "font-size: 100px;")
        self.titleLabel.move(240, -25)

        # subheading
        self.subheadingLabel = QLabel("Track Your Stats As You Play!", self)
        self.subheadingLabel.resize(500, 100)
        self.subheadingLabel.setStyleSheet("color: rgb(0, 76, 153);"
                                           "background-color: transparent;"
                                           "font-size: 30px;")
        self.subheadingLabel.move(415, 130)

        # new game pushbutton
        self.newGameButton = QPushButton("Start a New Game", self)
        self.newGameButton.resize(400, 100)
        self.newGameButton.setStyleSheet("QPushButton{"
                                         "color: white; border-style: outset; border-width: 4px;"
                                         "background-color: rgb(0, 40, 80);"
                                         "font-size: 40px;"
                                         "border-radius: 50px;"
                                         "}"
                                         "QPushButton:hover{"
                                         "background-color: rgb(0, 76, 153);"
                                         "}"
                                         )
        self.newGameButton.move(400, 325)

        # pool statistics button
        self.poolStatsButton = QPushButton("Pool Statistics", self)
        self.poolStatsButton.resize(400, 100)
        self.poolStatsButton.setStyleSheet("QPushButton{"
                                           "color: white; border-style: outset; border-width: 4px;"
                                           "background-color: rgb(0, 40, 80);"
                                           "font-size: 40px;"
                                           "border-radius: 50px;"
                                           "}"
                                           "QPushButton:hover{"
                                           "background-color: rgb(0, 76, 153);"
                                           "}"
                                           )
        self.poolStatsButton.move(400, 550)

        # show all the widgets
        self.show()
