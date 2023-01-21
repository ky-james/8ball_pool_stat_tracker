from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class SelectPlayersWindow(QMainWindow):
    def __init__(self, playerList):
        super().__init__()

        # window
        self.setGeometry(100, 0, 1200, 800)
        self.setWindowTitle("Pool Stat Tracker - Select Players")
        self.setStyleSheet("background-color: rgb(0, 76, 153);")

        # title background
        self.titleBackgroundLabel = QLabel("", self)
        self.titleBackgroundLabel.resize(1200, 200)
        self.titleBackgroundLabel.setStyleSheet("background-color: white;"
                                                "font-size: 80px;")
        self.titleBackgroundLabel.move(0, 0)

        # title label
        self.titleLabel = QLabel("Select Players", self)
        self.titleLabel.resize(1200, 200)
        self.titleLabel.setStyleSheet("color: rgb(0, 76, 153);"
                                      "background-color: transparent;"
                                      "font-size: 100px;")
        self.titleLabel.move(300, -5)

        # breaking player label
        self.breakingPlayerLabel = QLabel("Breaking Player", self)
        self.breakingPlayerLabel.resize(500, 75)
        self.breakingPlayerLabel.setStyleSheet("color: white; font-size: 40px;")
        self.breakingPlayerLabel.move(127, 200)

        # incoming player label
        self.incomingPlayerLabel = QLabel("Incoming Player", self)
        self.incomingPlayerLabel.resize(500, 75)
        self.incomingPlayerLabel.setStyleSheet("color: white; font-size: 40px;")
        self.incomingPlayerLabel.move(805, 200)

        # breaking player combo box
        self.breakingPlayerComboBox = QComboBox(self)
        self.breakingPlayerComboBox.setGeometry(200, 150, 220, 75)
        self.breakingPlayerComboBox.setStyleSheet("QComboBox{"
                                        "color: white;"
                                        "background-color: rgb(0, 40, 80);"
                                        "font-size: 30px;"
                                        "border-style: outset;"
                                        "border-color: white;"
                                        "border-width: 3px;"
                                        "padding-left: 15px;"
                                        "}"
                                        "QComboBox::down-arrow{"
                                        "color: white;"
                                        "}"
                                        "QComboBox QListView{"
                                        "border: 2px solid white;"
                                        "}")
        self.breakingPlayerComboBox.move(150, 275)

        # incoming player combo box
        self.incomingPlayerComboBox = QComboBox(self)
        self.incomingPlayerComboBox.setGeometry(200, 150, 210, 75)
        self.incomingPlayerComboBox.setStyleSheet("QComboBox{"
                                        "color: white;"
                                        "background-color: rgb(0, 40, 80);"
                                        "font-size: 30px;"
                                        "border-style: outset;"
                                        "border-color: white;"
                                        "border-width: 3px;"
                                        "padding-left: 15px;"
                                        "}"
                                        "QComboBox::down-arrow{"
                                        "color: white;"
                                        "}"
                                        "QComboBox QListView{"
                                        "border: 2px solid white;"
                                        "}")
        self.incomingPlayerComboBox.move(840, 275)

        # filling combo boxes with player names
        for i in range(0, len(playerList)):
            self.breakingPlayerComboBox.addItem("     " + playerList[i].playerName)
            self.incomingPlayerComboBox.addItem("     " + playerList[i].playerName)

        # centring the text in the combo boxes


        # initializing incomingPlayerComboBox to be set at a different player than breakingPlayer's player
        self.incomingPlayerComboBox.setCurrentIndex(1)

        # start game pushbutton
        self.startGameButton = QPushButton("Start Game", self)
        self.startGameButton.resize(400, 100)
        self.startGameButton.setStyleSheet("QPushButton{"
                                           "color: green; border-style: outset; border-width: 4px;"
                                           "background-color: rgb(0, 40, 80);"
                                           "font-size: 40px;"
                                           "border-radius: 50px;"
                                           "}"
                                           "QPushButton:hover{"
                                           "background-color: rgb(0, 76, 153);"
                                           "}"
                                           )
        self.startGameButton.move(405, 380)

        # back pushbutton
        self.backButton = QPushButton("Back to Menu", self)
        self.backButton.resize(400, 100)
        self.backButton.setStyleSheet("QPushButton{"
                                      "color: red; "
                                      "border-style: outset; "
                                      "border-width: 4px;"
                                      "background-color: rgb(0, 40, 80);"
                                      "font-size: 40px;"
                                      "border-radius: 50px;"
                                      "}"
                                      "QPushButton:hover{"
                                      "background-color: rgb(0, 76, 153);"
                                      "}"
                                      )
        self.backButton.move(405, 575)

        self.show()
