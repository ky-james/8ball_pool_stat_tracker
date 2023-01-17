from PyQt5.QtWidgets import *


class GameRecapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window
        self.setStyleSheet("background-color: rgb(0, 76, 153);")
        self.setWindowTitle("Pool Stat Tracker - Game Recap")
        self.setGeometry(100, 0, 1200, 800)

        # title background
        self.titleBackgroundLabel = QLabel("", self)
        self.titleBackgroundLabel.resize(1200, 200)
        self.titleBackgroundLabel.setStyleSheet("background-color: white;"
                                                "font-size: 80px;")
        self.titleBackgroundLabel.move(0, 0)

        # winner and loser titles
        self.winnerTitleLabel = QLabel("Winner", self)
        self.winnerTitleLabel.resize(300, 100)
        self.winnerTitleLabel.setStyleSheet("color: rgb(0, 225, 0);"
                                            "background-color: transparent;"
                                            "font-size: 75px;")
        self.winnerTitleLabel.move(200, 0)

        self.loserTitleLabel = QLabel("Loser", self)
        self.loserTitleLabel.resize(300, 100)
        self.loserTitleLabel.setStyleSheet("color: rgb(255, 0, 0);"
                                            "background-color: transparent;"
                                            "font-size: 75px;")
        self.loserTitleLabel.move(800, 0)

        # winner and loser names
        self.winnerNameLabel = QLabel("??", self)
        self.winnerNameLabel.resize(200, 100)
        self.winnerNameLabel.setStyleSheet("color: rgb(0, 76, 153);"
                                           "background-color: transparent;"
                                           "font-size: 40px;")
        self.winnerNameLabel.move(285, 75)

        self.loserNameLabel = QLabel("??", self)
        self.loserNameLabel.resize(200, 100)
        self.loserNameLabel.setStyleSheet("color: rgb(0, 76, 153);"
                                           "background-color: transparent;"
                                           "font-size: 40px;")
        self.loserNameLabel.move(885, 75)

        # key stats labels
        # balls sunk
        self.ballsSunkKeyStatsLabel = QLabel("Balls Sunk", self)
        self.ballsSunkKeyStatsLabel.resize(200, 100)
        self.ballsSunkKeyStatsLabel.setStyleSheet("color:white;"
                                                  "background-color: transparent;"
                                                  "font-size: 30px;")
        self.ballsSunkKeyStatsLabel.move(550, 200)

        # shooting percentage
        self.shootingPercentageKeyStatsLabel = QLabel("Shooting Percentage", self)
        self.shootingPercentageKeyStatsLabel.resize(350, 100)
        self.shootingPercentageKeyStatsLabel.setStyleSheet("color:white;"
                                                           "background-color: transparent;"
                                                           "font-size: 30px;")
        self.shootingPercentageKeyStatsLabel.move(490, 265)

        # 8-ball shooting percentage
        self.eightBallShootingPercentageKeyStatsLabel = QLabel("8-Ball Shooting Percentage", self)
        self.eightBallShootingPercentageKeyStatsLabel.resize(360, 100)
        self.eightBallShootingPercentageKeyStatsLabel.setStyleSheet("color:white;"
                                                                    "background-color: transparent;"
                                                                    "font-size: 30px;")
        self.eightBallShootingPercentageKeyStatsLabel.move(450, 330)

        # balls in hand
        self.ballsInHandKeyStatsLabel = QLabel("Balls in Hand", self)
        self.ballsInHandKeyStatsLabel.resize(250, 100)
        self.ballsInHandKeyStatsLabel.setStyleSheet("color:white;"
                                                    "background-color: transparent;"
                                                    "font-size: 30px;")
        self.ballsInHandKeyStatsLabel.move(535, 395)

        # scratches
        self.scratchesKeyStatsLabel = QLabel("Scratches", self)
        self.scratchesKeyStatsLabel.resize(200, 100)
        self.scratchesKeyStatsLabel.setStyleSheet("color:white;"
                                                  "background-color: transparent;"
                                                  "font-size: 30px;")
        self.scratchesKeyStatsLabel.move(550, 450)

        # winner key stats
        self.winnerBallsSunkLabel = QLabel("??", self)
        self.winnerBallsSunkLabel.resize(75, 75)
        self.winnerBallsSunkLabel.setStyleSheet("color: white;"
                                                "background-color: transparent;"
                                                "font-size: 40px;")
        self.winnerBallsSunkLabel.move(200, 210)

        self.winnerShootingPercentageLabel = QLabel("??", self)
        self.winnerShootingPercentageLabel.resize(100, 75)
        self.winnerShootingPercentageLabel.setStyleSheet("color: white;"
                                                         "background-color: transparent;"
                                                         "font-size: 40px;")
        self.winnerShootingPercentageLabel.move(200, 275)

        self.winnerEightBallShootingPercentageLabel = QLabel("??", self)
        self.winnerEightBallShootingPercentageLabel.resize(100, 75)
        self.winnerEightBallShootingPercentageLabel.setStyleSheet("color: white;"
                                                                  "background-color: transparent;"
                                                                  "font-size: 40px;")
        self.winnerEightBallShootingPercentageLabel.move(200, 340)

        self.winnerBallsInHandLabel = QLabel("??", self)
        self.winnerBallsInHandLabel.resize(75, 75)
        self.winnerBallsInHandLabel.setStyleSheet("color: white;"
                                                  "background-color: transparent;"
                                                  "font-size: 40px;")
        self.winnerBallsInHandLabel.move(200, 405)

        self.winnerScratchesLabel = QLabel("??", self)
        self.winnerScratchesLabel.resize(75, 75)
        self.winnerScratchesLabel.setStyleSheet("color: white;"
                                                "background-color: transparent;"
                                                "font-size: 40px;")
        self.winnerScratchesLabel.move(200, 470)

        # loser key stats
        self.loserBallsSunkLabel = QLabel("??", self)
        self.loserBallsSunkLabel.resize(75, 75)
        self.loserBallsSunkLabel.setStyleSheet("color: white;"
                                                "background-color: transparent;"
                                                "font-size: 40px;")
        self.loserBallsSunkLabel.move(975, 210)

        self.loserShootingPercentageLabel = QLabel("??", self)
        self.loserShootingPercentageLabel.resize(100, 75)
        self.loserShootingPercentageLabel.setStyleSheet("color: white;"
                                                         "background-color: transparent;"
                                                         "font-size: 40px;")
        self.loserShootingPercentageLabel.move(975, 275)

        self.loserEightBallShootingPercentageLabel = QLabel("??", self)
        self.loserEightBallShootingPercentageLabel.resize(100, 75)
        self.loserEightBallShootingPercentageLabel.setStyleSheet("color: white;"
                                                                  "background-color: transparent;"
                                                                  "font-size: 40px;")
        self.loserEightBallShootingPercentageLabel.move(975, 340)

        self.loserBallsInHandLabel = QLabel("??", self)
        self.loserBallsInHandLabel.resize(75, 75)
        self.loserBallsInHandLabel.setStyleSheet("color: white;"
                                                  "background-color: transparent;"
                                                  "font-size: 40px;")
        self.loserBallsInHandLabel.move(975, 405)

        self.loserScratchesLabel = QLabel("??", self)
        self.loserScratchesLabel.resize(75, 75)
        self.loserScratchesLabel.setStyleSheet("color: white;"
                                                "background-color: transparent;"
                                                "font-size: 40px;")
        self.loserScratchesLabel.move(975, 470)

        # return to menu button
        self.returnToMenuButton = QPushButton("Return to Menu", self)
        self.returnToMenuButton.resize(400, 100)
        self.returnToMenuButton.setStyleSheet("QPushButton{"
                                              "color: white; border-style: outset; border-width: 4px;"
                                              "background-color: rgb(0, 40, 80);"
                                              "font-size: 40px;"
                                              "border-radius: 50px;"
                                              "}"
                                              "QPushButton:hover{"
                                              "background-color: rgb(0, 76, 153);"
                                              "}"
                                              )
        self.returnToMenuButton.move(410, 650)
