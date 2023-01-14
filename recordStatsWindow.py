from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap

""""
READ THIS FIRST!!!
"""

class RecordStatsWindow(QMainWindow):
    def __init__(self, stack):
        super().__init__()

        # window stack instance variable
        self.windowStack = stack

        # game variables
        self.selectedBall = '?'
        self.selectedPocket = '?'

        self.breakingPlayer = '?'
        self.incomingPlayer = '?'
        self.solids = '?'
        self.stripes = '?'
        # TODO: change self.breakingPlayerTurn to true, as we always know the breaking player starts
        self.breakingPlayerTurn = '?'  # is changed to boolean in GUI_main.py
        self.sinkLog = []
        self.currTurnLog =[]
        self.turnLog = []
        self.turnNumber = 0
        # unsure if this is needed
        self.ballWasSunkThisTurn = False

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
        self.breakingPlayerRecordLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.breakingPlayerRecordLabel.move(210, 130)

        # incoming player record
        self.incomingPlayerRecordLabel = QLabel("", self)
        self.incomingPlayerRecordLabel.resize(500, 75)
        self.incomingPlayerRecordLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
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
        newestSinkEntry = (ball, pocket, self.bankShot, self.bridgeShot, self. behindTheBackShot, self.jumpShot)
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

        # unsure if this is needed
        self.ballWasSunkThisTurn = True

        # this was the first ball sunk outside the break, determining who's solids/stripes
        if ball != 'cue' and self.turnNumber != 0:
            if self.breakingPlayerTurn:
                if ball in self.solidBalls:
                    self.solids = 'breakingPlayer'
                else:
                    self.stripes = 'breakingPlayer'
            else:
                if ball in self.solidBalls:
                    self.solids = 'incomingPlayer'
                else:
                    self.solids = 'incomingPlayer'

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
        self.breakingPlayerTurn = not self.breakingPlayerTurn
        self.turnNumber += 1

        gameOver = False
        if '8' not in self.ballsOnTable:
            gameOver = True

        # adding a miss if the game is not over
        if not gameOver:
            self.currTurnLog.append("miss")

        # self.sinkLog and self.currTurnLog are both completed, we must add it to self.turnLog now
        self.turnLog.append(self.currTurnLog)

        # printing a recap to console of the logs, for testing purposes only
        print("\n~~~~~TURN ENDED~~~~~")
        print(f"Printing a recap of turn {self.turnNumber}")
        print("The latest turn:")
        print(f"\t{self.currTurnLog}")
        print("The game's updated turn log:")
        print(f"\t{self.turnLog}")

        # TODO: update the game object's stats of the latest turn

        # resetting self.currTurnLog now that the turn is over
        self.currTurnLog = []

        for item in self.sinkLog:
            if item[0] == 'cue':
                self.returnBallGraphics(item[0])
            else:
                ball = self.ballButtonDict[item[0]]
                ball.hide()

        # shooting icon
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

            self.windowStack.setCurrentIndex(3)


    def undoTurn(self):
        # removing the last turn from the logs
        if len(self.turnLog) > 0:
            moveToUndo = self.turnLog[-1]

            # removing a sink
            if len(moveToUndo) != 1:

                # undoing the graphics of the latest miss
                ballsSunk = len(moveToUndo) - 1

                # undoing each individual sink
                for i in range(ballsSunk):
                    ballSunk = moveToUndo[i]

                    # undoing the graphic for the sunk ball
                    self.returnBallGraphics(ballSunk[0])

                # undoing the logs
                self.sinkLog.pop()
                self.turnLog.pop()

                print("\n~~~~~TURN UNDONE~~~~~")
                print(f"Printing a recap of turn {self.turnNumber}")
                print("The latest turn:")
                print(f"\t{self.currTurnLog}")
                print("The game's updated turn log:")
                print(f"\t{self.turnLog}")

                # TODO: undoing the game object's stats of the latest miss
                pass

            # removing a miss
            else:
                # undoing the logs of the latest miss
                self.turnLog.pop()
                print("\n~~~~~TURN UNDONE~~~~~")
                print(f"Printing a recap of turn {self.turnNumber}")
                print("The latest turn:")
                print(f"\t{self.currTurnLog}")
                print("The game's updated turn log:")
                print(f"\t{self.turnLog}")

                # TODO: undoing the game object's stats of the latest miss
                pass

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