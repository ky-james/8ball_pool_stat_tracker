from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap

# TODO: as of rn, you're unable to sink two balls into the same pocket - FIX
# TODO: sinking an opponent's balls should not count for stats


class RecordStatsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window stack instance variable
        self.currentGame = None
        self.windowStack = None

        # game recap window instance variable
        self.gameRecapWindow = None

        # game variables
        self.selectedBall = '?'
        self.selectedPocket = '?'

        self.breakingPlayer = '?'
        self.incomingPlayer = '?'
        self.solids = '?'
        self.stripes = '?'
        self.breakingPlayerTurn = True
        self.sinkLog = []
        self.currTurnLog = []
        self.turnLog = []
        self.turnNumber = 1

        self.openTable = True
        self.ballsOnTable = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
        self.solidBalls = ['1', '2', '3', '4', '5', '6', '7']
        self.stripeBalls = ['9', '10', '11', '12', '13', '14', '15']
        self.ballButtonDict = dict()
        self.pocketCoordinateDict = {'A': (117, 545), 'B': (117, 270), 'C': (420, 545), 'D': (420, 260),
                                     'E': (723, 545), 'F': (723, 270)}
        self.ballPositionCoordinateDict = {'1': (150, 360), '2': (225, 360), '3': (300, 360), '4': (375, 360),
                                           '5': (450, 360), '6': (525, 360), '7': (600, 360), '8': (675, 360),
                                           '9': (150, 435), '10': (225, 435), '11': (300, 435), '12': (375, 435),
                                           '13': (450, 435), '14': (525, 435), '15': (600, 435), 'cue': (675, 435)}
        self.shootingIconCoordinateDict = {'breakingPlayer': (135, 115), 'incomingPlayer': (820, 115)}
        self.BPPocketLetterDict = None
        self.IPPocketLetterDict = None


        self.turnLog = []
        self.jumpShot = False
        self.bankShot = False
        self.bridgeShot = False
        self.behindTheBackShot = False

        # window
        self.setGeometry(100, 0, 1200, 800)
        self.setWindowTitle("Pool Stat Tracker - Recording Game")
        self.setStyleSheet("background-color: rgb(0, 76, 153);")

        # title labels
        # TODO: add a graphic to the screen which shows a player's ball type
        # title background
        self.titleBackgroundLabel = QLabel("", self)
        self.titleBackgroundLabel.resize(1200, 200)
        self.titleBackgroundLabel.setStyleSheet("background-color: white;"
                                                "font-size: 80px;")
        self.titleBackgroundLabel.move(0, 0)

        # breaking label
        self.breakingLabel = QLabel("Breaking Player", self)
        self.breakingLabel.resize(500, 75)
        self.breakingLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 60px; background-color: transparent;")
        self.breakingLabel.move(100, 20)

        # incoming label
        self.incomingLabel = QLabel("Incoming Player", self)
        self.incomingLabel.resize(500, 75)
        self.incomingLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 60px; background-color: transparent;")
        self.incomingLabel.move(710, 20)

        # break player label
        self.breakingPlayerLabel = QLabel("Kyle", self)
        self.breakingPlayerLabel.resize(500, 75)
        self.breakingPlayerLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.breakingPlayerLabel.move(210, 85)

        # incoming player label
        self.incomingPlayerLabel = QLabel("Brady", self)
        self.incomingPlayerLabel.resize(500, 75)
        self.incomingPlayerLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.incomingPlayerLabel.move(880, 85)

        # breaking player record
        self.breakingPlayerRecordLabel = QLabel("", self)
        self.breakingPlayerRecordLabel.resize(500, 75)
        self.breakingPlayerRecordLabel.setStyleSheet(
            "color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.breakingPlayerRecordLabel.move(210, 130)

        # incoming player record
        self.incomingPlayerRecordLabel = QLabel("", self)
        self.incomingPlayerRecordLabel.resize(500, 75)
        self.incomingPlayerRecordLabel.setStyleSheet(
            "color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.incomingPlayerRecordLabel.move(880, 135)

        # shooting icon
        self.shootingIcon = QLabel('', self)
        self.shootingIcon.setStyleSheet("background-color: transparent;")
        self.shootingIcon.setPixmap(QtGui.QPixmap("images/shootingIcon.png"))
        self.shootingIcon.resize(64, 64)
        self.shootingIcon.setScaledContents(True)
        self.shootingIcon.move(135, 115)

        # versus label
        self.versusLabel = QLabel("vs", self)
        self.versusLabel.resize(500, 75)
        self.versusLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 90px; background-color: transparent;")
        self.versusLabel.move(560, 60)

        # table, pocket labels, undo turn, and end turn
        # table
        self.tableLabel = QLabel(self)
        self.labelPixmap = QPixmap('images/table.png')
        self.tableLabel.setScaledContents(True)
        self.tableLabel.setPixmap(self.labelPixmap)
        self.tableLabel.resize(675, 338)
        self.tableLabel.move(95, 250)

        # end turn button
        self.endTurnButton = QPushButton("End Turn", self)
        self.endTurnButton.resize(200, 75)
        self.endTurnButton.setStyleSheet("QPushButton{"
                                         "color: white; border-style: outset; border-width: 4px;"
                                         "background-color: rgb(0, 40, 80);"
                                         "font-size: 20px;"
                                         "border-radius: 20px;"
                                         "}"
                                         "QPushButton:hover{"
                                         "background-color: rgb(0, 76, 153);"
                                         "color: rgb(90, 255, 128);"
                                         "}"
                                         )
        self.endTurnButton.move(490, 600)

        # end turn button
        self.undoTurnButton = QPushButton("Undo Turn", self)
        self.undoTurnButton.resize(200, 75)
        self.undoTurnButton.setStyleSheet("QPushButton{"
                                          "color: white; border-style: outset; border-width: 4px;"
                                          "background-color: rgb(0, 40, 80);"
                                          "font-size: 20px;"
                                          "border-radius: 20px;"
                                          "}"
                                          "QPushButton:hover{"
                                          "background-color: rgb(0, 76, 153);"
                                          "color: rgb(255, 69, 40);"
                                          "}"
                                          )
        self.undoTurnButton.move(183, 600)

        # pockets
        # pocket A
        self.pocketALabel1 = QPushButton("A", self)
        self.pocketALabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketALabel1.resize(75, 75)
        self.pocketALabel1.move(74, 480)

        self.pocketALabel2 = QPushButton("A", self)
        self.pocketALabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketALabel2.resize(75, 75)
        self.pocketALabel2.move(135, 536)

        self.pocketAButton = QPushButton("", self)
        # self.pocketAButton.setStyleSheet("background-color: white; color: blue;")
        self.pocketAButton.setStyleSheet("background-color: transparent; color: rgb(255, 69, 40);")
        self.pocketAButton.resize(75, 75)
        self.pocketAButton.move(100, 510)

        # pocket B
        self.pocketBLabel1 = QPushButton("B", self)
        self.pocketBLabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketBLabel1.resize(75, 75)
        self.pocketBLabel1.move(74, 283)

        self.pocketBLabel2 = QPushButton("B", self)
        self.pocketBLabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketBLabel2.resize(75, 75)
        self.pocketBLabel2.move(135, 226)

        self.pocketBButton = QPushButton("", self)
        # self.pocketBButton.setStyleSheet("background-color: white; color: blue;")
        self.pocketBButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketBButton.resize(75, 75)
        self.pocketBButton.move(100, 250)

        # pocket C
        self.pocketCLabel1 = QPushButton("C", self)
        self.pocketCLabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketCLabel1.resize(75, 75)
        self.pocketCLabel1.move(355, 536)

        self.pocketCLabel2 = QPushButton("C", self)
        self.pocketCLabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketCLabel2.resize(75, 75)
        self.pocketCLabel2.move(435, 536)

        self.pocketCButton = QPushButton("", self)
        # self.pocketCButton.setStyleSheet("background-color: white; color: blue;")
        self.pocketCButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketCButton.resize(75, 75)
        self.pocketCButton.move(400, 510)

        # pocket D
        self.pocketDLabel1 = QPushButton("D", self)
        self.pocketDLabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketDLabel1.resize(75, 75)
        self.pocketDLabel1.move(355, 226)

        self.pocketDLabel2 = QPushButton("D", self)
        self.pocketDLabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketDLabel2.resize(75, 75)
        self.pocketDLabel2.move(435, 226)

        self.pocketDButton = QPushButton("", self)
        # self.pocketDButton.setStyleSheet("background-color: white; color: blue;")
        self.pocketDButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketDButton.resize(75, 75)
        self.pocketDButton.move(400, 250)

        # pocket E
        self.pocketELabel1 = QPushButton("E", self)
        self.pocketELabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketELabel1.resize(75, 75)
        self.pocketELabel1.move(718, 480)

        self.pocketELabel2 = QPushButton("E", self)
        self.pocketELabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketELabel2.resize(75, 75)
        self.pocketELabel2.move(660, 536)

        self.pocketEButton = QPushButton("", self)
        # self.pocketEButton.setStyleSheet("background-color: white; color: blue;")
        self.pocketEButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketEButton.resize(75, 75)
        self.pocketEButton.move(695, 510)

        # pocket F
        self.pocketFLabel1 = QPushButton("F", self)
        self.pocketFLabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketFLabel1.resize(75, 75)
        self.pocketFLabel1.move(718, 283)

        self.pocketFLabel2 = QPushButton("F", self)
        self.pocketFLabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketFLabel2.resize(75, 75)
        self.pocketFLabel2.move(660, 226)

        self.pocketFButton = QPushButton("", self)
        # self.pocketFButton.setStyleSheet("background-color: white; color: blue;")
        self.pocketFButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketFButton.resize(75, 75)
        self.pocketFButton.move(695, 250)

        # ball buttons
        # ball 1
        self.ball1Button = QPushButton('', self)
        self.ball1Button.setStyleSheet("background-color: transparent;")
        self.ball1Button.setIcon(QtGui.QIcon('images/1'))
        self.ball1Button.setIconSize(QtCore.QSize(50, 50))
        self.ball1Button.resize(50, 50)
        self.ball1Button.move(150, 360)
        self.ballButtonDict['1'] = self.ball1Button

        # ball 2
        self.ball2Button = QPushButton('', self)
        self.ball2Button.setStyleSheet("background-color: transparent;")
        self.ball2Button.setIcon(QtGui.QIcon('images/2'))
        self.ball2Button.setIconSize(QtCore.QSize(50, 50))
        self.ball2Button.resize(50, 50)
        self.ball2Button.move(225, 360)
        self.ballButtonDict['2'] = self.ball2Button

        # ball 3
        self.ball3Button = QPushButton('', self)
        self.ball3Button.setStyleSheet("background-color: transparent;")
        self.ball3Button.setIcon(QtGui.QIcon('images/3'))
        self.ball3Button.setIconSize(QtCore.QSize(50, 50))
        self.ball3Button.resize(50, 50)
        self.ball3Button.move(300, 360)
        self.ballButtonDict['3'] = self.ball3Button

        # ball 4
        self.ball4Button = QPushButton('', self)
        self.ball4Button.setStyleSheet("background-color: transparent;")
        self.ball4Button.setIcon(QtGui.QIcon('images/4'))
        self.ball4Button.setIconSize(QtCore.QSize(50, 50))
        self.ball4Button.resize(50, 50)
        self.ball4Button.move(375, 360)
        self.ballButtonDict['4'] = self.ball4Button

        # ball 5
        self.ball5Button = QPushButton('', self)
        self.ball5Button.setStyleSheet("background-color: transparent;")
        self.ball5Button.setIcon(QtGui.QIcon('images/5'))
        self.ball5Button.setIconSize(QtCore.QSize(50, 50))
        self.ball5Button.resize(50, 50)
        self.ball5Button.move(450, 360)
        self.ballButtonDict['5'] = self.ball5Button

        # ball 6
        self.ball6Button = QPushButton('', self)
        self.ball6Button.setStyleSheet("background-color: transparent;")
        self.ball6Button.setIcon(QtGui.QIcon('images/6'))
        self.ball6Button.setIconSize(QtCore.QSize(50, 50))
        self.ball6Button.resize(50, 50)
        self.ball6Button.move(525, 360)
        self.ballButtonDict['6'] = self.ball6Button

        # ball 7
        self.ball7Button = QPushButton('', self)
        self.ball7Button.setStyleSheet("background-color: transparent;")
        self.ball7Button.setIcon(QtGui.QIcon('images/7'))
        self.ball7Button.setIconSize(QtCore.QSize(50, 50))
        self.ball7Button.resize(50, 50)
        self.ball7Button.move(600, 360)
        self.ballButtonDict['7'] = self.ball7Button

        # ball 8
        self.ball8Button = QPushButton('', self)
        self.ball8Button.setStyleSheet("background-color: transparent;")
        self.ball8Button.setIcon(QtGui.QIcon('images/8'))
        self.ball8Button.setIconSize(QtCore.QSize(50, 50))
        self.ball8Button.resize(50, 50)
        self.ball8Button.move(675, 360)
        self.ballButtonDict['8'] = self.ball8Button

        # ball 9
        self.ball9Button = QPushButton('', self)
        self.ball9Button.setStyleSheet("background-color: transparent;")
        self.ball9Button.setIcon(QtGui.QIcon('images/9'))
        self.ball9Button.setIconSize(QtCore.QSize(50, 50))
        self.ball9Button.resize(50, 50)
        self.ball9Button.move(150, 435)
        self.ballButtonDict['9'] = self.ball9Button

        # ball 10
        self.ball10Button = QPushButton('', self)
        self.ball10Button.setStyleSheet("background-color: transparent;")
        self.ball10Button.setIcon(QtGui.QIcon('images/10'))
        self.ball10Button.setIconSize(QtCore.QSize(50, 50))
        self.ball10Button.resize(50, 50)
        self.ball10Button.move(225, 435)
        self.ballButtonDict['10'] = self.ball10Button

        # ball 11
        self.ball11Button = QPushButton('', self)
        self.ball11Button.setStyleSheet("background-color: transparent;")
        self.ball11Button.setIcon(QtGui.QIcon('images/11'))
        self.ball11Button.setIconSize(QtCore.QSize(50, 50))
        self.ball11Button.resize(50, 50)
        self.ball11Button.move(300, 435)
        self.ballButtonDict['11'] = self.ball11Button
        # ball 12
        self.ball12Button = QPushButton('', self)
        self.ball12Button.setStyleSheet("background-color: transparent;")
        self.ball12Button.setIcon(QtGui.QIcon('images/12'))
        self.ball12Button.setIconSize(QtCore.QSize(50, 50))
        self.ball12Button.resize(50, 50)
        self.ball12Button.move(375, 435)
        self.ballButtonDict['12'] = self.ball12Button

        # ball 13
        self.ball13Button = QPushButton('', self)
        self.ball13Button.setStyleSheet("background-color: transparent;")
        self.ball13Button.setIcon(QtGui.QIcon('images/13'))
        self.ball13Button.setIconSize(QtCore.QSize(50, 50))
        self.ball13Button.resize(50, 50)
        self.ball13Button.move(450, 435)
        self.ballButtonDict['13'] = self.ball13Button

        # ball 14
        self.ball14Button = QPushButton('', self)
        self.ball14Button.setStyleSheet("background-color: transparent;")
        self.ball14Button.setIcon(QtGui.QIcon('images/14'))
        self.ball14Button.setIconSize(QtCore.QSize(50, 50))
        self.ball14Button.resize(50, 50)
        self.ball14Button.move(525, 435)
        self.ballButtonDict['14'] = self.ball14Button

        # ball 15
        self.ball15Button = QPushButton('', self)
        self.ball15Button.setStyleSheet("background-color: transparent;")
        self.ball15Button.setIcon(QtGui.QIcon('images/15'))
        self.ball15Button.setIconSize(QtCore.QSize(50, 50))
        self.ball15Button.resize(50, 50)
        self.ball15Button.move(600, 435)
        self.ballButtonDict['15'] = self.ball15Button

        # cue ball
        self.cueBallButton = QPushButton('', self)
        self.cueBallButton.setStyleSheet("background-color: transparent")
        self.cueBallButton.setIcon(QtGui.QIcon('images/cue'))
        self.cueBallButton.setIconSize(QtCore.QSize(50, 50))
        self.cueBallButton.resize(50, 50)
        self.cueBallButton.move(675, 435)
        self.ballButtonDict['cue'] = self.cueBallButton

        # shot icons and labels

        # jump shot
        self.jumpShotLabel = QLabel("Jump Shot", self)
        self.jumpShotLabel.resize(100, 50)
        self.jumpShotLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.jumpShotLabel.move(800, 340)

        self.jumpShotButton = QPushButton('', self)
        self.jumpShotButton.setStyleSheet("background-color: transparent;")
        self.jumpShotButton.setIcon(QtGui.QIcon('images/jumpShotIcon.png'))
        self.jumpShotButton.setIconSize(QtCore.QSize(101, 49))
        self.jumpShotButton.resize(101, 49)
        self.jumpShotButton.move(800, 300)

        # bank shot
        self.bankShotLabel = QLabel("Bank Shot", self)
        self.bankShotLabel.resize(100, 50)
        self.bankShotLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.bankShotLabel.move(805, 520)

        self.bankShotButton = QPushButton('', self)
        self.bankShotButton.setStyleSheet("background-color: transparent;")
        self.bankShotButton.setIcon(QtGui.QIcon('images/bankShotIcon.png'))
        self.bankShotButton.setIconSize(QtCore.QSize(101, 49))
        self.bankShotButton.resize(101, 49)
        self.bankShotButton.move(800, 475)

        # bridge
        self.bridgeLabel = QLabel("Bridge Shot", self)
        self.bridgeLabel.resize(110, 50)
        self.bridgeLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.bridgeLabel.move(980, 520)

        self.bridgeButton = QPushButton('', self)
        self.bridgeButton.setStyleSheet("background-color: transparent;")
        self.bridgeButton.setIcon(QtGui.QIcon('images/bridgeIcon.png'))
        self.bridgeButton.setIconSize(QtCore.QSize(218, 107))
        self.bridgeButton.resize(168, 82)
        self.bridgeButton.move(943, 455)

        # behind the back
        self.behindTheBackLabel = QLabel("Behind the Back Shot", self)
        self.behindTheBackLabel.resize(200, 50)
        self.behindTheBackLabel.setStyleSheet(
            "color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.behindTheBackLabel.move(945, 340)

        self.behindTheBackButton = QPushButton('', self)
        self.behindTheBackButton.setStyleSheet("background-color: transparent;")
        self.behindTheBackButton.setIcon(QtGui.QIcon('images/behindTheBackIcon.png'))
        self.behindTheBackButton.setIconSize(QtCore.QSize(101, 49))
        self.behindTheBackButton.resize(101, 49)
        self.behindTheBackButton.move(980, 300)

        # mapping buttons
        self.jumpShotButton.clicked.connect(self.toggleJumpShot)
        self.bankShotButton.clicked.connect(self.toggleBankShot)
        self.bridgeButton.clicked.connect(self.toggleBridgeShot)
        self.behindTheBackButton.clicked.connect(self.toggleBehindTheBackShot)

        self.ball1Button.clicked.connect(self.ball1Clicked)
        self.ball2Button.clicked.connect(self.ball2Clicked)
        self.ball3Button.clicked.connect(self.ball3Clicked)
        self.ball4Button.clicked.connect(self.ball4Clicked)
        self.ball5Button.clicked.connect(self.ball5Clicked)
        self.ball6Button.clicked.connect(self.ball6Clicked)
        self.ball7Button.clicked.connect(self.ball7Clicked)
        self.ball8Button.clicked.connect(self.ball8Clicked)
        self.ball9Button.clicked.connect(self.ball9Clicked)
        self.ball10Button.clicked.connect(self.ball10Clicked)
        self.ball11Button.clicked.connect(self.ball11Clicked)
        self.ball12Button.clicked.connect(self.ball12Clicked)
        self.ball13Button.clicked.connect(self.ball13Clicked)
        self.ball14Button.clicked.connect(self.ball14Clicked)
        self.ball15Button.clicked.connect(self.ball15Clicked)
        self.cueBallButton.clicked.connect(self.cueBallClicked)

        self.pocketAButton.clicked.connect(self.pocketAClicked)
        self.pocketBButton.clicked.connect(self.pocketBClicked)
        self.pocketCButton.clicked.connect(self.pocketCClicked)
        self.pocketDButton.clicked.connect(self.pocketDClicked)
        self.pocketEButton.clicked.connect(self.pocketEClicked)
        self.pocketFButton.clicked.connect(self.pocketFClicked)

        self.endTurnButton.clicked.connect(self.endTurn)
        self.undoTurnButton.clicked.connect(self.undoTurn)

        self.show()

    def toggleJumpShot(self):
        if self.jumpShot:
            self.jumpShotLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")

        else:
            self.jumpShotLabel.setStyleSheet(
                "color: rgb(90, 255, 128); font-size: 20px; background-color: transparent;")

        self.jumpShot = not self.jumpShot

    def toggleBankShot(self):
        if self.bankShot:
            self.bankShotLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")

        else:
            self.bankShotLabel.setStyleSheet(
                "color: rgb(90, 255, 128); font-size: 20px; background-color: transparent;")

        self.bankShot = not self.bankShot

    def toggleBridgeShot(self):
        if self.bridgeShot:
            self.bridgeLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")

        else:
            self.bridgeLabel.setStyleSheet("color: rgb(90, 255, 128); font-size: 20px; background-color: transparent;")

        self.bridgeShot = not self.bridgeShot

    def toggleBehindTheBackShot(self):
        if self.behindTheBackShot:
            self.behindTheBackLabel.setStyleSheet(
                "color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")

        else:
            self.behindTheBackLabel.setStyleSheet(
                "color: rgb(90, 255, 128); font-size: 20px; background-color: transparent;")

        self.behindTheBackShot = not self.behindTheBackShot

    def ball1Clicked(self):
        self.selectedBall = '1'

    def ball2Clicked(self):
        self.selectedBall = '2'

    def ball3Clicked(self):
        self.selectedBall = '3'

    def ball4Clicked(self):
        self.selectedBall = '4'

    def ball5Clicked(self):
        self.selectedBall = '5'

    def ball6Clicked(self):
        self.selectedBall = '6'

    def ball7Clicked(self):
        self.selectedBall = '7'

    def ball8Clicked(self):
        self.selectedBall = '8'

    def ball9Clicked(self):
        self.selectedBall = '9'

    def ball10Clicked(self):
        self.selectedBall = '10'

    def ball11Clicked(self):
        self.selectedBall = '11'

    def ball12Clicked(self):
        self.selectedBall = '12'

    def ball13Clicked(self):
        self.selectedBall = '13'

    def ball14Clicked(self):
        self.selectedBall = '14'

    def ball15Clicked(self):
        self.selectedBall = '15'

    def cueBallClicked(self):
        self.selectedBall = 'cue'

    def pocketAClicked(self):
        self.selectedPocket = 'A'

        if self.selectedBall != '?':
            self.sinkBall(self.selectedBall, self.selectedPocket)

    def pocketBClicked(self):
        self.selectedPocket = 'B'

        if self.selectedBall != '?':
            self.sinkBall(self.selectedBall, self.selectedPocket)

    def pocketCClicked(self):
        self.selectedPocket = 'C'

        if self.selectedBall != '?':
            self.sinkBall(self.selectedBall, self.selectedPocket)

    def pocketDClicked(self):
        self.selectedPocket = 'D'

        if self.selectedBall != '?':
            self.sinkBall(self.selectedBall, self.selectedPocket)

    def pocketEClicked(self):
        self.selectedPocket = 'E'

        if self.selectedBall != '?':
            self.sinkBall(self.selectedBall, self.selectedPocket)

    def pocketFClicked(self):
        self.selectedPocket = 'F'

        if self.selectedBall != '?':
            self.sinkBall(self.selectedBall, self.selectedPocket)

    def sinkBall(self, ball, pocket):
        # creating a tuple containing relevant data from the last sink
        newestSinkEntry = (ball, pocket, self.bankShot, self.bridgeShot, self.behindTheBackShot, self.jumpShot)
        self.currTurnLog.append(newestSinkEntry)
        self.sinkLog.append(newestSinkEntry)

        if self.bankShot:
            self.toggleBankShot()

        if self.jumpShot:
            self.toggleJumpShot()

        if self.behindTheBackShot:
            self.toggleBehindTheBackShot()

        if self.bridgeShot:
            self.toggleBridgeShot()

        # updating the sunk ball's graphics
        self.sinkBallGraphics(self.ballButtonDict[ball], pocket)
        if ball != 'cue':
            self.ballsOnTable.remove(ball)

        # resetting instance variables for future use
        self.selectedBall = '?'
        self.selectedPocket = '?'



    def sinkBallGraphics(self, ball, pocket):
        ball.setIconSize(QtCore.QSize(25, 25))
        ball.resize(25, 25)
        ball.move(self.pocketCoordinateDict[pocket][0], self.pocketCoordinateDict[pocket][1])
        ball.setEnabled(False)

    def returnBallGraphics(self, ball):
        ballObj = self.ballButtonDict[ball]
        coors = self.ballPositionCoordinateDict[ball]
        ballObj.move(coors[0], coors[1])
        ballObj.setEnabled(True)
        ballObj.setIconSize(QtCore.QSize(50, 50))
        ballObj.resize(50, 50)
        ballObj.show()
        self.ballsOnTable.append(ball)

    def endTurn(self):
        gameOver = False
        if '8' not in self.ballsOnTable:
            gameOver = True

            # updating who won the game
            # the breaking player won the game
            if self.breakingPlayerTurn:
                breakingPlayerWon = True

                # breaking player was solids
                if self.solids == self.breakingPlayer:
                    for ball in self.ballsOnTable:
                        if ball in self.solids:
                            breakingPlayerWon = False

                # breaking player was stripes
                elif self.stripes == self.breakingPlayer:
                    for ball in self.ballsOnTable:
                        if ball in self.stripes:
                            breakingPlayerWon = False

                # updating the current game object's winner and loser
                if breakingPlayerWon:
                    self.currentGame.winner = self.breakingPlayer
                    self.currentGame.loser = self.incomingPlayer

                else:
                    self.currentGame.winner = self.incomingPlayer
                    self.currentGame.loser = self.breakingPlayer

            # the incoming player won the game
            elif not self.breakingPlayerTurn:
                incomingPlayerWon = True

                # incoming player was solids
                if self.solids == self.incomingPlayer:
                    for ball in self.ballsOnTable:
                        if ball in self.solids:
                            incomingPlayerWon = False

                # incoming player was stripes
                elif self.stripes == self.incomingPlayer:
                    for ball in self.ballsOnTable:
                        if ball in self.stripes:
                            incomingPlayerWon = False

                # updating the current game object's winner and loser
                if incomingPlayerWon:
                    self.currentGame.winner = self.incomingPlayer
                    self.currentGame.loser = self.breakingPlayer

                else:
                    self.currentGame.winner = self.breakingPlayer
                    self.currentGame.loser = self.incomingPlayer

        # TODO: fix the below bug
        """
        As of right now, a miss is being added after every turn.
        This is incorrect as misses should only be added if there were no sinks or the previous sink was the shooting 
        player's ball
        """

        # adding a miss if the game is not over
        if not gameOver:
            # finding out if the player was on the 8-ball at the time of the miss
            playerWasOnEightBall = True

            # the table was open, player was not on the 8-ball
            if self.openTable:
                playerWasOnEightBall = False

            # it was the breaking player's turn
            elif self.breakingPlayerTurn:
                # breaking player was solids
                if self.breakingPlayer == self.solids:
                    for ball in self.solids:
                        if ball in self.ballsOnTable:
                            playerWasOnEightBall = False

                # breaking player was stripes
                elif self.breakingPlayer == self.stripes:
                    for ball in self.stripes:
                        if ball in self.ballsOnTable:
                            playerWasOnEightBall = False

            # it was the incoming player's turn
            elif not self.breakingPlayerTurn:
                # incoming player was solids
                if self.incomingPlayer == self.solids:
                    for ball in self.solids:
                        if ball in self.ballsOnTable:
                            playerWasOnEightBall = False

                # incoming player was stripes
                elif self.incomingPlayer == self.stripes:
                    for ball in self.stripes:
                        if ball in self.ballsOnTable:
                            playerWasOnEightBall = False

            # creating a tuple containing relevant data from the last shot
            newestMissEntry = ("miss", self.bankShot, self.bridgeShot, self.behindTheBackShot, self.jumpShot,
                               playerWasOnEightBall)
            self.currTurnLog.append(newestMissEntry)

            # toggling off the type of shot buttons if clicked
            if self.bankShot:
                self.toggleBankShot()

            if self.jumpShot:
                self.toggleJumpShot()

            if self.behindTheBackShot:
                self.toggleBehindTheBackShot()

            if self.bridgeShot:
                self.toggleBridgeShot()

        # self.sinkLog and self.currTurnLog are both completed, we must add it to self.turnLog now
        self.turnLog.append(self.currTurnLog)

        # updating the game object's stats
        # updating the stats for the first n-1 shots, where n is the number of shots the player took this turn
        # note: that we know all of these shots must've sunk a solid or striped ball
        for i in range(len(self.currTurnLog) - 1):
            # pulling info from a sink
            sink = self.currTurnLog[i]
            pocket = sink[1]
            bankShot = sink[2]
            bridgeShot = sink[3]
            behindTheBackShot = sink[4]
            jumpShot = sink[5]

            # the breaking player sunk the ball
            if self.breakingPlayerTurn:
                # updating the overall stats
                self.currentGame.BPShotsTaken += 1
                self.currentGame.BPShotsMade += 1
                self.BPPocketLetterDict[pocket] += 1

                # updating the type of shot stats
                if bankShot:
                    self.currentGame.BPBankShotsTaken += 1
                    self.currentGame.BPBankShotsMade += 1

                if bridgeShot:
                    self.currentGame.BPBridgeShotsTaken += 1
                    self.currentGame.BPBridgeShotsMade += 1

                if behindTheBackShot:
                    self.currentGame.BPBehindTheBackShotsTaken += 1
                    self.currentGame.BPBehindTheBackShotsMade += 1

                if jumpShot:
                    self.currentGame.BPJumpShotsTaken += 1
                    self.currentGame.BPJumpShotsMade += 1

            # the incoming player sunk the ball
            if not self.breakingPlayerTurn:
                # updating the overall stats
                self.currentGame.IPShotsTaken += 1
                self.currentGame.IPShotsMade += 1
                self.IPPocketLetterDict[pocket] += 1

                # updating the type of shot stats
                if bankShot:
                    self.currentGame.IPBankShotsTaken += 1
                    self.currentGame.IPBankShotsMade += 1

                if bridgeShot:
                    self.currentGame.IPBridgeShotsTaken += 1
                    self.currentGame.IPBridgeShotsMade += 1

                if behindTheBackShot:
                    self.currentGame.IPBehindTheBackShotsTaken += 1
                    self.currentGame.IPBehindTheBackShotsTaken += 1

                if jumpShot:
                    self.currentGame.IPBehindTheBackShotsTaken += 1
                    self.currentGame.IPBehindTheBackShotsMade += 1

        # updating the stats for the last shot in the turn
        # note: this shot will either be a miss, 8-ball sink or a scratch
        lastTurn = self.currTurnLog[- 1]
        print(f"last turn: {lastTurn}")

        # the shot was a miss
        if lastTurn[0] == 'miss':
            # variables from the latest miss
            bankShot = lastTurn[1]
            bridgeShot = lastTurn[2]
            behindTheBackShot = lastTurn[3]
            jumpShot = lastTurn[4]
            playerWasOnEightBall = lastTurn[5]

            # the breaking player missed
            if self.breakingPlayerTurn:
                # updating the overall stats
                self.currentGame.BPShotsTaken += 1
                self.currentGame.BPShotsMissed += 1

                # updating the type of shot stats
                # bank shot
                if bankShot:
                    self.currentGame.BPBankShotsTaken += 1
                    self.currentGame.BPBankShotsMissed += 1

                # bridge shots
                if bridgeShot:
                    self.currentGame.BPBridgeShotsTaken += 1
                    self.currentGame.BPBridgeShotsMissed += 1

                # behind the back shots
                if behindTheBackShot:
                    self.currentGame.BPBehindTheBackShotsTaken += 1
                    self.currentGame.BPBehindTheBackShotsMissed += 1

                # jump shot
                if jumpShot:
                    self.currentGame.BPJumpShotsTaken += 1
                    self.currentGame.BPJumpShotsMissed += 1

                # updating 8-ball stats if breaking player is on the 8-ball
                if playerWasOnEightBall:
                    self.currentGame.BPEightBallShotsTaken += 1
                    self.currentGame.BPEightBallShotsMissed += 1

            # the incoming player missed
            if not self.breakingPlayerTurn:
                # updating the overall stats
                self.currentGame.IPShotsTaken += 1
                self.currentGame.IPShotsMissed += 1

                # updating the type of shot stats
                # bank shot
                if bankShot:
                    self.currentGame.IPBankShotsTaken += 1
                    self.currentGame.IPBankShotsMissed += 1

                # bridge shots
                if bridgeShot:
                    self.currentGame.IPBridgeShotsTaken += 1
                    self.currentGame.IPBridgeShotsMissed += 1

                # behind the back shots
                if behindTheBackShot:
                    self.currentGame.IPBehindTheBackShotsTaken += 1
                    self.currentGame.IPBehindTheBackShotsMissed += 1

                # jump shot
                if jumpShot:
                    self.currentGame.IPJumpShotsTaken += 1
                    self.currentGame.IPJumpShotsMissed += 1

                # updating 8-ball stats if incoming player is on the 8-ball
                if playerWasOnEightBall:
                    self.currentGame.IPEightBallShotsTaken += 1
                    self.currentGame.IPEightBallShotsMissed += 1

        # the shot was a scratch
        elif lastTurn[0] == 'cue':
            # variables from the latest scratch
            bankShot = lastTurn[2]
            bridgeShot = lastTurn[3]
            behindTheBackShot = lastTurn[4]
            jumpShot = lastTurn[5]

            # the breaking player scratched
            if self.breakingPlayerTurn:
                # updating the overall stats
                self.currentGame.BPShotsTaken += 1
                self.currentGame.BPShotsMissed += 1

                # updating the type of shot stats
                # bank shot
                if bankShot:
                    self.currentGame.BPBankShotsTaken += 1
                    self.currentGame.BPBankShotsMissed += 1

                # bridge shots
                if bridgeShot:
                    self.currentGame.BPBridgeShotsTaken += 1
                    self.currentGame.BPBridgeShotsMissed += 1

                # behind the back shots
                if behindTheBackShot:
                    self.currentGame.BPBehindTheBackShotsTaken += 1
                    self.currentGame.BPBehindTheBackShotsMissed += 1

                # jump shot
                if jumpShot:
                    self.currentGame.BPJumpShotsTaken += 1
                    self.currentGame.BPJumpShotsMissed += 1

                # updating the scratch stats
                self.currentGame.BPScratchesMade += 1
                self.currentGame.IPOpponentScratches += 1

            # the incoming player scratched
            if not self.breakingPlayerTurn:
                # updating the overall stats
                self.currentGame.IPShotsTaken += 1
                self.currentGame.IPShotsMissed += 1

                # updating the type of shot stats
                # bank shot
                if bankShot:
                    self.currentGame.IPBankShotsTaken += 1
                    self.currentGame.IPBankShotsMissed += 1

                # bridge shots
                if bridgeShot:
                    self.currentGame.IPBridgeShotsTaken += 1
                    self.currentGame.IPBridgeShotsMissed += 1

                # behind the back shots
                if behindTheBackShot:
                    self.currentGame.IPBehindTheBackShotsTaken += 1
                    self.currentGame.IPBehindTheBackShotsMissed += 1

                # jump shot
                if jumpShot:
                    self.currentGame.IPJumpShotsTaken += 1
                    self.currentGame.IPJumpShotsMissed += 1

                # updating the scratch stats
                self.currentGame.IPScratchesMade += 1
                self.currentGame.BPOpponentScratches += 1

        # the shot was an 8-ball sink
        elif lastTurn[0] == '8':
            # variables from the latest 8-ball sink
            bankShot = lastTurn[2]
            bridgeShot = lastTurn[3]
            behindTheBackShot = lastTurn[4]
            jumpShot = lastTurn[5]

            # the breaking player sunk the 8-ball
            if self.breakingPlayerTurn:
                # determining if the breaking player won the game
                breakingPlayerWon = True

                # the breaking player is solids
                if self.solids == self.breakingPlayer:
                    for ball in self.ballsOnTable:
                        if ball in self.solids:
                            breakingPlayerWon = False

                # the breaking player is stripes
                elif self.stripes == self.breakingPlayer:
                    for ball in self.breakingPlayer:
                        if ball in self.stripes:
                            breakingPlayerWon = False

                elif self.openTable:
                    breakingPlayerWon = False

                # the breaking player won the game with the 8-ball sink
                if breakingPlayerWon:
                    # updating the overall stats
                    self.currentGame.BPShotsTaken += 1
                    self.currentGame.BPShotsMade += 1

                    # updating the type of shot stats
                    # bank shot
                    if bankShot:
                        self.currentGame.BPBankShotsTaken += 1
                        self.currentGame.BPBankShotsMade += 1

                    # bridge shots
                    if bridgeShot:
                        self.currentGame.BPBridgeShotsTaken += 1
                        self.currentGame.BPBridgeShotsMade += 1

                    # behind the back shots
                    if behindTheBackShot:
                        self.currentGame.BPBehindTheBackShotsTaken += 1
                        self.currentGame.BPBehindTheBackShotsMade += 1

                    # jump shot
                    if jumpShot:
                        self.currentGame.BPJumpShotsTaken += 1
                        self.currentGame.BPJumpShotsMade += 1

                    # updating the 8-ball stats
                    self.currentGame.BPEightBallShotsTaken += 1
                    self.currentGame.BPEightBallShotsMade += 1

                # the breaking player lost the game with the 8-ball sink
                if not breakingPlayerWon:
                    # updating the overall stats
                    self.currentGame.BPShotsTaken += 1
                    self.currentGame.BPShotsMissed += 1

                    # updating the type of shot stats
                    # bank shot
                    if bankShot:
                        self.currentGame.BPBankShotsTaken += 1
                        self.currentGame.BPBankShotsMissed += 1

                    # bridge shots
                    if bridgeShot:
                        self.currentGame.BPBridgeShotsTaken += 1
                        self.currentGame.BPBridgeShotsMissed += 1

                    # behind the back shots
                    if behindTheBackShot:
                        self.currentGame.BPBehindTheBackShotsTaken += 1
                        self.currentGame.BPBehindTheBackShotsMissed += 1

                    # jump shot
                    if jumpShot:
                        self.currentGame.BPJumpShotsTaken += 1
                        self.currentGame.BPJumpShotsMissed += 1

                    # updating the current game object's choke stats
                    self.currentGame.gameWonByChoke = True

            # the incoming player sunk the 8-ball
            if not self.breakingPlayerTurn:
                # determining if the incoming player won the game
                incomingPlayerWon = True

                # the incoming player is solids
                if self.solids == self.incomingPlayer:
                    for ball in self.ballsOnTable:
                        if ball in self.solids:
                            incomingPlayerWon = False

                # the incoming player is stripes
                elif self.stripes == self.incomingPlayer:
                    for ball in self.incomingPlayer:
                        if ball in self.stripes:
                            incomingPlayerWon = False

                elif self.openTable:
                    incomingPlayerWon = False

                # the incoming player won the game with the 8-ball sink
                if incomingPlayerWon:
                    # updating the overall stats
                    self.currentGame.IPShotsTaken += 1
                    self.currentGame.IPShotsMade += 1

                    # updating the type of shot stats
                    # bank shot
                    if bankShot:
                        self.currentGame.IPBankShotsTaken += 1
                        self.currentGame.IPBankShotsMade += 1

                    # bridge shots
                    if bridgeShot:
                        self.currentGame.IPBridgeShotsTaken += 1
                        self.currentGame.IPBridgeShotsMade += 1

                    # behind the back shots
                    if behindTheBackShot:
                        self.currentGame.IPBehindTheBackShotsTaken += 1
                        self.currentGame.IPBehindTheBackShotsMade += 1

                    # jump shot
                    if jumpShot:
                        self.currentGame.IPJumpShotsTaken += 1
                        self.currentGame.IPJumpShotsMade += 1

                    # updating the 8-ball stats
                    self.currentGame.IPEightBallShotsTaken += 1
                    self.currentGame.IPEightBallShotsMade += 1

                # the incoming player lost the game with the 8-ball sink
                if not incomingPlayerWon:
                    # updating the overall stats
                    self.currentGame.IPShotsTaken += 1
                    self.currentGame.IPShotsMissed += 1

                    # updating the type of shot stats
                    # bank shot
                    if bankShot:
                        self.currentGame.IPBankShotsTaken += 1
                        self.currentGame.IPBankShotsMissed += 1

                    # bridge shots
                    if bridgeShot:
                        self.currentGame.IPBridgeShotsTaken += 1
                        self.currentGame.IPBridgeShotsMissed += 1

                    # behind the back shots
                    if behindTheBackShot:
                        self.currentGame.IPBehindTheBackShotsTaken += 1
                        self.currentGame.IPBehindTheBackShotsMissed += 1

                    # jump shot
                    if jumpShot:
                        self.currentGame.IPJumpShotsTaken += 1
                        self.currentGame.IPJumpShotsMissed += 1

                    # updating the current game object's choke stats
                    self.currentGame.gameWonByChoke = True

        print("\n~~~~~TURN ENDED~~~~~")
        print(f"Printing a recap of turn {self.turnNumber}")
        if self.breakingPlayerTurn: print("The breaking player's latest turn:")
        else: print("The incoming player's latest turn:")
        print(f"\t{self.currTurnLog}")
        print("The Game's updated sink log:")
        print(f"\t{self.sinkLog}")
        print("The game's updated turn log:")
        print(f"\t{self.turnLog}")

        # resetting self.currTurnLog now that the turn is over
        self.currTurnLog = []

        # putting the cue ball back on the table if sunk
        for shot in self.sinkLog:
            if shot[0] == 'cue':
                self.returnBallGraphics(shot[0])
            else:
                ball = self.ballButtonDict[shot[0]]
                ball.hide()

        # updating the turn
        self.breakingPlayerTurn = not self.breakingPlayerTurn
        self.turnNumber += 1

        # updating the shooting icon
        if self.breakingPlayerTurn:
            self.shootingIcon.move(self.shootingIconCoordinateDict['breakingPlayer'][0],
                                   self.shootingIconCoordinateDict['breakingPlayer'][1])
        else:
            self.shootingIcon.move(self.shootingIconCoordinateDict['incomingPlayer'][0],
                                   self.shootingIconCoordinateDict['incomingPlayer'][1])

        # resetting the graphics and changing windows now that the game is over
        if gameOver:

            # returning all the balls to the table
            for ball in self.ballButtonDict.keys():
                self.returnBallGraphics(ball)

            # resetting the shooting icon
            self.shootingIcon.move(self.shootingIconCoordinateDict['breakingPlayer'][0],
                                   self.shootingIconCoordinateDict['breakingPlayer'][1])

            # update the game recap window's stats
            print("\n~~~~~~GAME OVER~~~~~~")

            # the breaking player is the winner
            if self.currentGame.winner == self.breakingPlayer:
                print("\tBreaking player won!")

                # changing labels to reflect the latest game
                # winner
                self.gameRecapWindow.winnerNameLabel.setText(self.breakingPlayer)
                self.gameRecapWindow.winnerBallsSunkLabel.setText(str(self.currentGame.BPShotsMade))
                self.gameRecapWindow.winnerBallsInHandLabel.setText(str(self.currentGame.BPOpponentScratches))
                self.gameRecapWindow.winnerScratchesLabel.setText(str(self.currentGame.BPScratchesMade))

                # ensuring that shooting percentages do not divide by zero
                # 8-ball shots were taken
                if self.currentGame.BPEightBallShotsTaken != 0:
                    self.gameRecapWindow.winnerEightBallShootingPercentageLabel.setText(
                        str(int(
                        100 * self.currentGame.BPEightBallShotsMade / self.currentGame.BPEightBallShotsTaken)) + "%")

                # 8-ball shots were not taken
                elif self.currentGame.BPEightBallShotsTaken == 0:
                    self.gameRecapWindow.winnerEightBallShootingPercentageLabel.setText("N/A")

                # shots were taken
                if self.currentGame.BPShotsTaken != 0:
                    self.gameRecapWindow.winnerShootingPercentageLabel.setText(
                        str(int(100 * self.currentGame.BPShotsMade / self.currentGame.BPShotsTaken)) + "%")

                # shots were not taken
                elif self.currentGame.BPShotsTaken == 0:
                    self.gameRecapWindow.winnerShootingPercentageLabel.setText("N/A")

                # loser
                self.gameRecapWindow.loserNameLabel.setText(self.incomingPlayer)
                self.gameRecapWindow.loserBallsSunkLabel.setText(str(self.currentGame.IPShotsMade))
                self.gameRecapWindow.loserBallsInHandLabel.setText(str(self.currentGame.IPOpponentScratches))
                self.gameRecapWindow.loserScratchesLabel.setText(str(self.currentGame.IPScratchesMade))

                # ensuring that shooting percentages do not divide by zero
                # 8-ball shots were taken
                if self.currentGame.IPEightBallShotsTaken != 0:
                    self.gameRecapWindow.loserEightBallShootingPercentageLabel.setText(
                        str(int(
                            100 * self.currentGame.IPEightBallShotsMade / self.currentGame.IPEightBallShotsTaken)) + "%")

                # 8-ball shots were not taken
                elif self.currentGame.IPEightBallShotsTaken == 0:
                    self.gameRecapWindow.loserEightBallShootingPercentageLabel.setText("N/A")

                # shots were taken
                if self.currentGame.IPShotsTaken != 0:
                    self.gameRecapWindow.loserShootingPercentageLabel.setText(
                        str(int(100 * self.currentGame.IPShotsMade / self.currentGame.IPShotsTaken)) + "%")

                # shots were not taken
                elif self.currentGame.IPShotsTaken == 0:
                    self.gameRecapWindow.loserShootingPercentageLabel.setText("N/A")

            # the incoming player is the winner
            elif self.currentGame.winner == self.incomingPlayer:
                print("\tIncoming player won!")

                # changing the labels to reflect the latest game
                # winner
                self.gameRecapWindow.winnerNameLabel.setText(self.incomingPlayer)
                self.gameRecapWindow.winnerBallsSunkLabel.setText(str(self.currentGame.IPShotsMade))
                self.gameRecapWindow.winnerBallsInHandLabel.setText(str(self.currentGame.IPOpponentScratches))
                self.gameRecapWindow.winnerScratchesLabel.setText(str(self.currentGame.IPScratchesMade))

                # ensuring that shooting percentages do not divide by zero
                # 8-ball shots were taken
                if self.currentGame.IPEightBallShotsTaken != 0:
                    self.gameRecapWindow.winnerEightBallShootingPercentageLabel.setText(
                        str(int(100 * self.currentGame.IPEightBallShotsMade / self.currentGame.IPEightBallShotsTaken)) + "%")

                # 8-ball shots were not taken
                elif self.currentGame.IPEightBallShotsTaken == 0:
                    self.gameRecapWindow.winnerEightBallShootingPercentageLabel.setText("N/A")

                # shots were taken
                if self.currentGame.IPShotsTaken != 0:
                    self.gameRecapWindow.winnerShootingPercentageLabel.setText(
                        str(int(100 * self.currentGame.IPShotsMade / self.currentGame.IPShotsTaken)) + "%")

                # shots were not taken
                elif self.currentGame.IPShotsTaken == 0:
                    self.gameRecapWindow.winnerShootingPercentageLabel.setText("N/A")

                # loser
                self.gameRecapWindow.loserNameLabel.setText(self.breakingPlayer)
                self.gameRecapWindow.loserBallsSunkLabel.setText(str(self.currentGame.BPShotsMade))
                self.gameRecapWindow.loserBallsInHandLabel.setText(str(self.currentGame.BPOpponentScratches))
                self.gameRecapWindow.loserScratchesLabel.setText(str(self.currentGame.BPScratchesMade))

                # ensuring that shooting percentages do not divide by zero
                # 8-ball shots were taken
                if self.currentGame.BPEightBallShotsTaken != 0:
                    self.gameRecapWindow.loserEightBallShootingPercentageLabel.setText(
                        str(int(100 * self.currentGame.BPEightBallShotsMade / self.currentGame.BPEightBallShotsTaken)) + "%")

                # 8-ball shots were not taken
                elif self.currentGame.BPEightBallShotsTaken == 0:
                    self.gameRecapWindow.loserEightBallShootingPercentageLabel.setText("N/A")

                # shots were taken
                if self.currentGame.BPShotsTaken != 0:
                    self.gameRecapWindow.loserShootingPercentageLabel.setText(
                        str(int(100 * self.currentGame.BPShotsMade / self.currentGame.BPShotsTaken)) + "%")

                # shots were not taken
                elif self.currentGame.BPShotsTaken == 0:
                    self.gameRecapWindow.loserShootingPercentageLabel.setText("N/A")

            # move to the game recap window
            self.windowStack.setCurrentIndex(3)

        # resetting the selected ball
        self.selectedBall = '?'

    def undoTurn(self):
        # removing the last turn from the logs
        if len(self.turnLog) > 0:
            moveToUndo = self.turnLog[-1]

            # removing a sink
            if len(moveToUndo) != 1:

                # undoing the graphics of the latest miss
                ballsSunk = len(moveToUndo) - 1
                for i in range(ballsSunk):
                    sink = moveToUndo[i]
                    ballSunk = sink[0]
                    pocket = sink[1]
                    bankShot = sink[2]
                    bridgeShot = sink[3]
                    behindTheBackShot = sink[4]
                    jumpShot = sink[5]

                    # undoing the graphic for the sunk ball
                    self.returnBallGraphics(ballSunk)

                    # updating the current game object's stats
                    # if the breaking player sunk the ball
                    if not self.breakingPlayerTurn:
                        # updating the overall stats
                        self.currentGame.BPShotsTaken -= 1
                        self.currentGame.BPShotsMade -= 1
                        self.BPPocketLetterDict[pocket] -= 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.BPBankShotsTaken -= 1
                            self.currentGame.BPBankShotsMade -= 1
                        if bridgeShot:
                            self.currentGame.BPBridgeShotsTaken -= 1
                            self.currentGame.BPBridgeShotsMade -= 1
                        if behindTheBackShot:
                            self.currentGame.BPBehindTheBackShotsTaken -= 1
                            self.currentGame.BPBehindTheBackShotsMade -= 1
                        if jumpShot:
                            self.currentGame.BPJumpShotsTaken += 1
                            self.currentGame.BPJumpShotsMade += 1

                    # if the incoming player sunk the ball
                    if self.breakingPlayerTurn:
                        # updating the overall stats
                        self.currentGame.IPShotsTaken -= 1
                        self.currentGame.IPShotsMade -= 1
                        self.IPPocketLetterDict[pocket] -= 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.IPBankShotsTaken -= 1
                            self.currentGame.IPBankShotsMade -= 1
                        if bridgeShot:
                            self.currentGame.IPBridgeShotsTaken -= 1
                            self.currentGame.IPBridgeShotsMade -= 1
                        if behindTheBackShot:
                            self.currentGame.IPBehindTheBackShotsTaken -= 1
                            self.currentGame.IPBehindTheBackShotsMade -= 1
                        if jumpShot:
                            self.currentGame.IPJumpShotsTaken += 1
                            self.currentGame.IPJumpShotsMade += 1

                # checking if the move to undo was the first ball sunk
                if len(self.sinkLog) == 1:
                    # updating the window's instance variables
                    self.solids = '?'
                    self.stripes = '?'
                    self.openTable = True

                    # updating the current game object's stats
                    self.currentGame.solids = None
                    self.currentGame.stripes = None

                    # printing the update
                    print("\n~~~~~BALL TYPES UNDECLARED~~~~~")
                    print("The table is now open!")

                # undoing the logs
                self.sinkLog.pop()
                self.turnLog.pop()

                # printing the update
                print("\n~~~~~TURN UNDONE~~~~~")
                print(f"Printing a recap of turn {self.turnNumber}")
                print("The latest turn:")
                print(f"\t{self.currTurnLog}")
                print("The game's updated turn log:")
                print(f"\t{self.turnLog}")

            # removing a miss
            else:
                # updating the current game object's stats for this miss
                miss = moveToUndo[-1]
                bankShot = miss[1]
                bridgeShot = miss[2]
                behindTheBackShot = miss[3]
                jumpShot = miss[4]
                playerOnEightBall = miss[5]

                # the breaking player missed
                if not self.breakingPlayerTurn:
                    # updating the overall stats
                    self.currentGame.BPShotsTaken -= 1
                    self.currentGame.BPShotsMissed -= 1

                    # updating the type of shot stats
                    # bank shot
                    if bankShot:
                        self.currentGame.BPBankShotsTaken -= 1
                        self.currentGame.BPBankShotsMissed -= 1

                    # bridge shots
                    if bridgeShot:
                        self.currentGame.BPBridgeShotsTaken -= 1
                        self.currentGame.BPBridgeShotsMissed -= 1

                    # behind the back shots
                    if behindTheBackShot:
                        self.currentGame.BPBehindTheBackShotsTaken -= 1
                        self.currentGame.BPBehindTheBackShotsMissed -= 1

                    # jump shot
                    if jumpShot:
                        self.currentGame.BPJumpShotsTaken -= 1
                        self.currentGame.BPJumpShotsMissed -= 1

                    # updating the 8-ball stats if this turn was on the 8-ball
                    if playerOnEightBall:
                        self.currentGame.BPEightBallShotsTaken -= 1
                        self.currentGame.BPEightBallShotsMissed -= 1

                # the incoming player missed
                elif self.breakingPlayerTurn:
                    # updating the overall stats
                    self.currentGame.IPShotsTaken -= 1
                    self.currentGame.IPShotsMissed -= 1

                    # updating the type of shot stats
                    # bank shot
                    if bankShot:
                        self.currentGame.IPBankShotsTaken -= 1
                        self.currentGame.IPBankShotsMissed -= 1

                    # bridge shots
                    if bridgeShot:
                        self.currentGame.IPBridgeShotsTaken -= 1
                        self.currentGame.IPBridgeShotsMissed -= 1

                    # behind the back shots
                    if behindTheBackShot:
                        self.currentGame.IPBehindTheBackShotsTaken -= 1
                        self.currentGame.IPBehindTheBackShotsMissed -= 1

                    # jump shot
                    if jumpShot:
                        self.currentGame.IPJumpShotsTaken -= 1
                        self.currentGame.IPJumpShotsMissed -= 1

                    # updating the 8-ball stats if this turn was on the 8-ball
                    if playerOnEightBall:
                        self.currentGame.IPEightBallShotsTaken -= 1
                        self.currentGame.IPEightBallShotsMissed -= 1

                # undoing the logs of the latest miss
                self.turnLog.pop()

                # printing an update
                print("\n~~~~~TURN UNDONE~~~~~")
                print(f"Printing a recap of turn {self.turnNumber}")
                print("The latest turn:")
                print(f"\t{self.currTurnLog}")
                print("The game's updated turn log:")
                print(f"\t{self.turnLog}")

            # toggling the shooting icon
            if not self.breakingPlayerTurn:
                self.shootingIcon.move(self.shootingIconCoordinateDict['breakingPlayer'][0],
                                       self.shootingIconCoordinateDict['breakingPlayer'][1])
                self.breakingPlayerTurn = not self.breakingPlayerTurn

            else:
                self.shootingIcon.move(self.shootingIconCoordinateDict['incomingPlayer'][0],
                                       self.shootingIconCoordinateDict['incomingPlayer'][1])
                self.breakingPlayerTurn = not self.breakingPlayerTurn

            # updating the turn number
            self.turnNumber -= 1

        else:
            print("\n~~~~~UNABLE TO UNDO TURN~~~~~")
            print("\tNo moves in turn log to remove")
