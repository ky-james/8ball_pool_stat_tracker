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

        # winner and looser titles
        self.winnerTitleLabel = QLabel("Winner", self)
        self.winnerTitleLabel.resize(300, 100)
        self.winnerTitleLabel.setStyleSheet("color: rgb(0, 225, 0);"
                                            "background-color: transparent;"
                                            "font-size: 75px;")
        self.winnerTitleLabel.move(200, 0)

        self.looserTitleLabel = QLabel("Looser", self)
        self.looserTitleLabel.resize(300, 100)
        self.looserTitleLabel.setStyleSheet("color: rgb(255, 0, 0);"
                                            "background-color: transparent;"
                                            "font-size: 75px;")
        self.looserTitleLabel.move(800, 0)

        # winner and looser names
        self.winnerNameLabel = QLabel("Kyle", self)
        self.winnerNameLabel.resize(200, 100)
        self.winnerNameLabel.setStyleSheet("color: rgb(0, 76, 153);"
                                           "background-color: transparent;"
                                           "font-size: 40px;")
        self.winnerNameLabel.move(285, 75)

        self.looserNameLabel = QLabel("Brady", self)
        self.looserNameLabel.resize(200, 100)
        self.looserNameLabel.setStyleSheet("color: rgb(0, 76, 153);"
                                           "background-color: transparent;"
                                           "font-size: 40px;")
        self.looserNameLabel.move(885, 75)

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

        # eight ball shooting percentage
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
        self.winnerShootingPercentageLabel.resize(75, 75)
        self.winnerShootingPercentageLabel.setStyleSheet("color: white;"
                                                         "background-color: transparent;"
                                                         "font-size: 40px;")
        self.winnerShootingPercentageLabel.move(200, 275)

        self.winnerEightBallShootingPercentageLabel = QLabel("??", self)
        self.winnerEightBallShootingPercentageLabel.resize(75, 75)
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

        # looser key stats
        self.looserBallsSunkLabel = QLabel("??", self)
        self.looserBallsSunkLabel.resize(75, 75)
        self.looserBallsSunkLabel.setStyleSheet("color: white;"
                                                "background-color: transparent;"
                                                "font-size: 40px;")
        self.looserBallsSunkLabel.move(975, 210)

        self.looserShootingPercentageLabel = QLabel("??", self)
        self.looserShootingPercentageLabel.resize(75, 75)
        self.looserShootingPercentageLabel.setStyleSheet("color: white;"
                                                         "background-color: transparent;"
                                                         "font-size: 40px;")
        self.looserShootingPercentageLabel.move(975, 275)

        self.looserEightBallShootingPercentageLabel = QLabel("??", self)
        self.looserEightBallShootingPercentageLabel.resize(75, 75)
        self.looserEightBallShootingPercentageLabel.setStyleSheet("color: white;"
                                                                  "background-color: transparent;"
                                                                  "font-size: 40px;")
        self.looserEightBallShootingPercentageLabel.move(975, 340)

        self.looserBallsInHandLabel = QLabel("??", self)
        self.looserBallsInHandLabel.resize(75, 75)
        self.looserBallsInHandLabel.setStyleSheet("color: white;"
                                                  "background-color: transparent;"
                                                  "font-size: 40px;")
        self.looserBallsInHandLabel.move(975, 405)

        self.looserScratchesLabel = QLabel("??", self)
        self.looserScratchesLabel.resize(75, 75)
        self.looserScratchesLabel.setStyleSheet("color: white;"
                                                "background-color: transparent;"
                                                "font-size: 40px;")
        self.looserScratchesLabel.move(975, 470)

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
