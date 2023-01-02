from PyQt5.QtWidgets import *


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
        self.titleLabel.move(350, 0)

        # home label
        self.homeLabel = QLabel("Home Player", self)
        self.homeLabel.resize(500, 75)
        self.homeLabel.setStyleSheet("color: white; font-size: 40px;")
        self.homeLabel.move(150, 200)

        # away label
        self.awayLabel = QLabel("Away Player", self)
        self.awayLabel.resize(500, 75)
        self.awayLabel.setStyleSheet("color: white; font-size: 40px;")
        self.awayLabel.move(850, 200)

        # home combo box
        self.homeComboBox = QComboBox(self)
        self.homeComboBox.setGeometry(200, 150, 220, 75)
        self.homeComboBox.setStyleSheet("QComboBox{"
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
        self.homeComboBox.move(150, 275)

        # away combo box
        self.awayComboBox = QComboBox(self)
        self.awayComboBox.setGeometry(200, 150, 210, 75)
        self.awayComboBox.setStyleSheet("QComboBox{"
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
        self.awayComboBox.move(850, 275)

        # updating combo boxes
        for i in range(1, len(playerList)):
            self.homeComboBox.addItem(playerList[i].name)
            self.awayComboBox.addItem(playerList[i].name)

        # initializing awayComboBox to be set at a different player than homeComboBox's player
        self.awayComboBox.setCurrentIndex(1)

        # break check box
        self.breakCheckBox = QCheckBox(self)
        self.breakCheckBox.setText("Home Breaks")
        self.breakCheckBox.setGeometry(200, 150, 180, 60)
        self.breakCheckBox.setStyleSheet("QCheckBox{"
                                         "background-color: rgb(0, 40, 80); "
                                         "color: white;"
                                         "border-style: outset;"
                                         "border-width: 4px;"
                                         "border-color: white;"
                                         "border-radius: 50px;"
                                         "font-size: 23px;"
                                         "}"
                                         "QCheckBox:unchecked{"
                                         "color: red;"
                                         "}"
                                         "QCheckBox:checked{"
                                         "color: green;"
                                         "}"
                                         "QCheckBox:hover{"
                                         "background-color: rgb(0, 76, 153)"
                                         "}")
        self.breakCheckBox.move(510, 285)

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
        self.startGameButton.move(400, 400)

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
        self.backButton.move(400, 550)

        self.show()
