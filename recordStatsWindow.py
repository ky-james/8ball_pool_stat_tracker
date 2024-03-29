from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from writing import writeGameStatsToPlayers

# TODO: what if an opponent's ball is sunk off the break?
# TODO: add logic to track unintentional shots & break shots
# TODO: create a standardized way to test stats


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

        self.playerDict = '?'
        self.breakingPlayer = '?'
        self.incomingPlayer = '?'
        self.solids = '?'
        self.stripes = '?'
        self.breakingPlayerTurn = True
        self.sinkLog = []
        self.currentTurnLog = []
        self.turnLog = []
        self.turnNumber = 1

        self.openTable = True
        self.ballsOnTable = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
        self.solidBalls = ['1', '2', '3', '4', '5', '6', '7']
        self.stripeBalls = ['9', '10', '11', '12', '13', '14', '15']
        self.ballButtonDict = dict()
        self.pocketCoordinateDict = {'A': (57, 270), 'B': (360, 260), 'C': (663, 270), 'D': (663, 545),
                                     'E': (360, 548), 'F': (57, 545)}
        self.ballPositionCoordinateDict = {'1': (90, 360), '2': (165, 360),
                                           '3': (240, 360), '4': (315, 360),
                                           '5': (390, 360), '6': (465, 360),
                                           '7': (540, 360), '8': (615, 360),
                                           '9': (90, 435), '10': (165, 435),
                                           '11': (240, 435), '12': (315, 435),
                                           '13': (590, 435), '14': (455, 435),
                                           '15': (540, 435), 'cue': (615, 435)}
        self.shootingIconCoordinateDict = {'breakingPlayer': (210, 115), 'incomingPlayer': (805, 115)}
        self.BPPocketLetterDict = None
        self.IPPocketLetterDict = None

        self.turnLog = []
        self.jumpShot = False
        self.bankShot = False
        self.bridgeShot = False
        self.behindTheBackShot = False
        self.sunkOffBreak = True
        self.unintentionalShot = False
        self.sameShot = False

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

        # footer background
        self.footerBackgroundLabel = QLabel("", self)
        self.footerBackgroundLabel.resize(1200, 200)
        self.footerBackgroundLabel.setStyleSheet("background-color: white;" "font-size: 80px;")
        self.footerBackgroundLabel.move(0, 755)

        # shot type background
        self.footerBackgroundLabel = QLabel("", self)
        self.footerBackgroundLabel.resize(383, 455)
        self.footerBackgroundLabel.setStyleSheet("color: white; border-style: outset; border-width: 8px; "
                                                 "background-color: white;"
                                                 "border-radius: 20px;"
                                                 "border-color: rgb(0, 40, 80);"
                                                 "}"
                                                 "QLabel:hover{"
                                                 "border-color: rgb(0, 20, 80);"
                                                 "}")
        self.footerBackgroundLabel.move(790, 255)

        # breaking label
        self.breakingLabel = QLabel("Breaking Player", self)
        self.breakingLabel.resize(500, 75)
        self.breakingLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 60px; background-color: transparent;")
        self.breakingLabel.move(105, 20)

        # incoming label
        self.incomingLabel = QLabel("Incoming Player", self)
        self.incomingLabel.resize(500, 75)
        self.incomingLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 60px; background-color: transparent;")
        self.incomingLabel.move(687, 20)

        # breaking player label
        self.breakingPlayerLabel = QLabel("Kyle", self)
        self.breakingPlayerLabel.resize(500, 75)
        self.breakingPlayerLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.breakingPlayerLabel.move(278, 85)

        # incoming player label
        self.incomingPlayerLabel = QLabel("Brady", self)
        self.incomingPlayerLabel.resize(500, 75)
        self.incomingPlayerLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.incomingPlayerLabel.move(870, 85)

        # breaking player record
        self.breakingPlayerRecordLabel = QLabel("", self)
        self.breakingPlayerRecordLabel.resize(500, 75)
        self.breakingPlayerRecordLabel.setStyleSheet(
            "color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.breakingPlayerRecordLabel.move(270, 130)

        # incoming player record
        self.incomingPlayerRecordLabel = QLabel("", self)
        self.incomingPlayerRecordLabel.resize(500, 75)
        self.incomingPlayerRecordLabel.setStyleSheet(
            "color: rgb(0, 40, 80); font-size: 40px; background-color: transparent;")
        self.incomingPlayerRecordLabel.move(865, 130)

        # shooting icon
        self.shootingIcon = QLabel('', self)
        self.shootingIcon.setStyleSheet("background-color: transparent;")
        self.shootingIcon.setPixmap(QtGui.QPixmap("images/shootingIcon.png"))
        self.shootingIcon.resize(64, 64)
        self.shootingIcon.setScaledContents(True)
        self.shootingIcon.move(self.shootingIconCoordinateDict["breakingPlayer"][0],
                               self.shootingIconCoordinateDict["breakingPlayer"][1])

        # ball type icons
        self.breakingPlayerBallTypeIcon = QLabel('', self)
        self.breakingPlayerBallTypeIcon.setStyleSheet("background-color: transparent;")
        self.breakingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/openTable.png"))
        self.breakingPlayerBallTypeIcon.resize(64, 64)
        self.breakingPlayerBallTypeIcon.setScaledContents(True)
        self.breakingPlayerBallTypeIcon.move(395, 115)

        self.incomingPlayerBallTypeIcon = QLabel('', self)
        self.incomingPlayerBallTypeIcon.setStyleSheet("background-color: transparent;")
        self.incomingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/openTable.png"))
        self.incomingPlayerBallTypeIcon.resize(64, 64)
        self.incomingPlayerBallTypeIcon.setScaledContents(True)
        self.incomingPlayerBallTypeIcon.move(985, 115)

        # versus label
        self.versusLabel = QLabel("vs", self)
        self.versusLabel.resize(500, 75)
        self.versusLabel.setStyleSheet("color: rgb(0, 40, 80); font-size: 90px; background-color: transparent;")
        self.versusLabel.move(552, 55)

        # table, pocket labels, undo turn, and end turn
        # table
        self.tableLabel = QLabel(self)
        self.labelPixmap = QPixmap('images/table.png')
        self.tableLabel.setScaledContents(True)
        self.tableLabel.setPixmap(self.labelPixmap)
        self.tableLabel.resize(675, 338)
        self.tableLabel.move(35, 250)

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
                                         "color: rgb(0, 135, 32);"
                                         "}"
                                         )
        self.endTurnButton.move(495, 630)

        # undo turn button
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
        self.undoTurnButton.move(40, 630)

        # same turn button
        self.sunkOffBreakButton = QPushButton("Sunk Off Break", self)
        self.sunkOffBreakButton.resize(200, 75)
        self.sunkOffBreakButton.setStyleSheet("QPushButton{"
                                                      "color:  rgb(0, 135, 32); border-style: outset; border-width: 4px;"
                                                      "background-color: rgb(0, 40, 80);"
                                                      "font-size: 20px;"
                                                      "border-radius: 20px;"
                                                      "}"
                                                      "QPushButton:hover{"
                                                      "background-color: rgb(0, 76, 153);"
                                                      "}")
        self.sunkOffBreakButton.move(270, 630)

        # pockets
        # pocket F
        self.pocketFLabel1 = QPushButton("F", self)
        self.pocketFLabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketFLabel1.resize(75, 75)
        self.pocketFLabel1.move(14, 480)

        self.pocketFLabel2 = QPushButton("F", self)
        self.pocketFLabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketFLabel2.resize(75, 75)
        self.pocketFLabel2.move(75, 536)

        self.pocketFButton = QPushButton("", self)
        self.pocketFButton.setStyleSheet("background-color: transparent; color: rgb(255, 69, 40);")
        self.pocketFButton.resize(75, 75)
        self.pocketFButton.move(40, 510)

        # pocket A
        self.pocketALabel1 = QPushButton("A", self)
        self.pocketALabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketALabel1.resize(75, 75)
        self.pocketALabel1.move(14, 283)

        self.pocketALabel2 = QPushButton("A", self)
        self.pocketALabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketALabel2.resize(75, 75)
        self.pocketALabel2.move(75, 226)

        self.pocketAButton = QPushButton("", self)
        self.pocketAButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketAButton.resize(75, 75)
        self.pocketAButton.move(40, 250)

        # pocket E
        self.pocketELabel1 = QPushButton("E", self)
        self.pocketELabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketELabel1.resize(75, 75)
        self.pocketELabel1.move(295, 536)

        self.pocketELabel2 = QPushButton("E", self)
        self.pocketELabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketELabel2.resize(75, 75)
        self.pocketELabel2.move(375, 536)

        self.pocketEButton = QPushButton("", self)
        self.pocketEButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketEButton.resize(75, 75)
        self.pocketEButton.move(340, 510)

        # pocket B
        self.pocketBLabel1 = QPushButton("B", self)
        self.pocketBLabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketBLabel1.resize(75, 75)
        self.pocketBLabel1.move(295, 226)

        self.pocketBLabel2 = QPushButton("B", self)
        self.pocketBLabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketBLabel2.resize(75, 75)
        self.pocketBLabel2.move(375, 226)

        self.pocketBButton = QPushButton("", self)
        self.pocketBButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketBButton.resize(75, 75)
        self.pocketBButton.move(340, 250)

        # pocket D
        self.pocketDLabel1 = QPushButton("D", self)
        self.pocketDLabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketDLabel1.resize(75, 75)
        self.pocketDLabel1.move(658, 480)

        self.pocketDLabel2 = QPushButton("D", self)
        self.pocketDLabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketDLabel2.resize(75, 75)
        self.pocketDLabel2.move(600, 536)

        self.pocketDButton = QPushButton("", self)
        # self.pocketEButton.setStyleSheet("background-color: white; color: blue;")
        self.pocketDButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketDButton.resize(75, 75)
        self.pocketDButton.move(635, 510)

        # pocket C
        self.pocketCLabel1 = QPushButton("C", self)
        self.pocketCLabel1.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketCLabel1.resize(75, 75)
        self.pocketCLabel1.move(658, 283)

        self.pocketCLabel2 = QPushButton("C", self)
        self.pocketCLabel2.setStyleSheet("background-color: transparent; color: white; font-size: 25px ")
        self.pocketCLabel2.resize(75, 75)
        self.pocketCLabel2.move(600, 226)

        self.pocketCButton = QPushButton("", self)
        self.pocketCButton.setStyleSheet("background-color: transparent; color: transparent;")
        self.pocketCButton.resize(75, 75)
        self.pocketCButton.move(635, 250)

        # ball buttons
        # ball 1
        self.ball1Button = QPushButton('', self)
        self.ball1Button.setStyleSheet("background-color: transparent;")
        self.ball1Button.setIcon(QtGui.QIcon('images/1'))
        self.ball1Button.setIconSize(QtCore.QSize(50, 50))
        self.ball1Button.resize(50, 50)
        self.ball1Button.move(90, 360)
        self.ballButtonDict['1'] = self.ball1Button

        # ball 2
        self.ball2Button = QPushButton('', self)
        self.ball2Button.setStyleSheet("background-color: transparent;")
        self.ball2Button.setIcon(QtGui.QIcon('images/2'))
        self.ball2Button.setIconSize(QtCore.QSize(50, 50))
        self.ball2Button.resize(50, 50)
        self.ball2Button.move(165, 360)
        self.ballButtonDict['2'] = self.ball2Button

        # ball 3
        self.ball3Button = QPushButton('', self)
        self.ball3Button.setStyleSheet("background-color: transparent;")
        self.ball3Button.setIcon(QtGui.QIcon('images/3'))
        self.ball3Button.setIconSize(QtCore.QSize(50, 50))
        self.ball3Button.resize(50, 50)
        self.ball3Button.move(240, 360)
        self.ballButtonDict['3'] = self.ball3Button

        # ball 4
        self.ball4Button = QPushButton('', self)
        self.ball4Button.setStyleSheet("background-color: transparent;")
        self.ball4Button.setIcon(QtGui.QIcon('images/4'))
        self.ball4Button.setIconSize(QtCore.QSize(50, 50))
        self.ball4Button.resize(50, 50)
        self.ball4Button.move(315, 360)
        self.ballButtonDict['4'] = self.ball4Button

        # ball 5
        self.ball5Button = QPushButton('', self)
        self.ball5Button.setStyleSheet("background-color: transparent;")
        self.ball5Button.setIcon(QtGui.QIcon('images/5'))
        self.ball5Button.setIconSize(QtCore.QSize(50, 50))
        self.ball5Button.resize(50, 50)
        self.ball5Button.move(390, 360)
        self.ballButtonDict['5'] = self.ball5Button

        # ball 6
        self.ball6Button = QPushButton('', self)
        self.ball6Button.setStyleSheet("background-color: transparent;")
        self.ball6Button.setIcon(QtGui.QIcon('images/6'))
        self.ball6Button.setIconSize(QtCore.QSize(50, 50))
        self.ball6Button.resize(50, 50)
        self.ball6Button.move(465, 360)
        self.ballButtonDict['6'] = self.ball6Button

        # ball 7
        self.ball7Button = QPushButton('', self)
        self.ball7Button.setStyleSheet("background-color: transparent;")
        self.ball7Button.setIcon(QtGui.QIcon('images/7'))
        self.ball7Button.setIconSize(QtCore.QSize(50, 50))
        self.ball7Button.resize(50, 50)
        self.ball7Button.move(540, 360)
        self.ballButtonDict['7'] = self.ball7Button

        # ball 8
        self.ball8Button = QPushButton('', self)
        self.ball8Button.setStyleSheet("background-color: transparent;")
        self.ball8Button.setIcon(QtGui.QIcon('images/8'))
        self.ball8Button.setIconSize(QtCore.QSize(50, 50))
        self.ball8Button.resize(50, 50)
        self.ball8Button.move(615, 360)
        self.ballButtonDict['8'] = self.ball8Button

        # ball 9
        self.ball9Button = QPushButton('', self)
        self.ball9Button.setStyleSheet("background-color: transparent;")
        self.ball9Button.setIcon(QtGui.QIcon('images/9'))
        self.ball9Button.setIconSize(QtCore.QSize(50, 50))
        self.ball9Button.resize(50, 50)
        self.ball9Button.move(90, 435)
        self.ballButtonDict['9'] = self.ball9Button

        # ball 10
        self.ball10Button = QPushButton('', self)
        self.ball10Button.setStyleSheet("background-color: transparent;")
        self.ball10Button.setIcon(QtGui.QIcon('images/10'))
        self.ball10Button.setIconSize(QtCore.QSize(50, 50))
        self.ball10Button.resize(50, 50)
        self.ball10Button.move(165, 435)
        self.ballButtonDict['10'] = self.ball10Button

        # ball 11
        self.ball11Button = QPushButton('', self)
        self.ball11Button.setStyleSheet("background-color: transparent;")
        self.ball11Button.setIcon(QtGui.QIcon('images/11'))
        self.ball11Button.setIconSize(QtCore.QSize(50, 50))
        self.ball11Button.resize(50, 50)
        self.ball11Button.move(240, 435)
        self.ballButtonDict['11'] = self.ball11Button
        # ball 12
        self.ball12Button = QPushButton('', self)
        self.ball12Button.setStyleSheet("background-color: transparent;")
        self.ball12Button.setIcon(QtGui.QIcon('images/12'))
        self.ball12Button.setIconSize(QtCore.QSize(50, 50))
        self.ball12Button.resize(50, 50)
        self.ball12Button.move(315, 435)
        self.ballButtonDict['12'] = self.ball12Button

        # ball 13
        self.ball13Button = QPushButton('', self)
        self.ball13Button.setStyleSheet("background-color: transparent;")
        self.ball13Button.setIcon(QtGui.QIcon('images/13'))
        self.ball13Button.setIconSize(QtCore.QSize(50, 50))
        self.ball13Button.resize(50, 50)
        self.ball13Button.move(390, 435)
        self.ballButtonDict['13'] = self.ball13Button

        # ball 14
        self.ball14Button = QPushButton('', self)
        self.ball14Button.setStyleSheet("background-color: transparent;")
        self.ball14Button.setIcon(QtGui.QIcon('images/14'))
        self.ball14Button.setIconSize(QtCore.QSize(50, 50))
        self.ball14Button.resize(50, 50)
        self.ball14Button.move(465, 435)
        self.ballButtonDict['14'] = self.ball14Button

        # ball 15
        self.ball15Button = QPushButton('', self)
        self.ball15Button.setStyleSheet("background-color: transparent;")
        self.ball15Button.setIcon(QtGui.QIcon('images/15'))
        self.ball15Button.setIconSize(QtCore.QSize(50, 50))
        self.ball15Button.resize(50, 50)
        self.ball15Button.move(540, 435)
        self.ballButtonDict['15'] = self.ball15Button

        # cue ball
        self.cueBallButton = QPushButton('', self)
        self.cueBallButton.setStyleSheet("background-color: transparent")
        self.cueBallButton.setIcon(QtGui.QIcon('images/cue'))
        self.cueBallButton.setIconSize(QtCore.QSize(50, 50))
        self.cueBallButton.resize(50, 50)
        self.cueBallButton.move(615, 435)
        self.ballButtonDict['cue'] = self.cueBallButton

        # shot icons and labels
        # bank shot
        self.bankShotLabel = QLabel("Bank Shot", self)
        self.bankShotLabel.resize(200, 50)
        self.bankShotLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.bankShotLabel.move(840, 340)

        self.bankShotButton = QPushButton('', self)
        self.bankShotButton.setStyleSheet("background-color: transparent;")
        self.bankShotButton.setIcon(QtGui.QIcon('images/bankShotIcon.png'))
        self.bankShotButton.setIconSize(QtCore.QSize(130, 64))
        self.bankShotButton.resize(130, 64)
        self.bankShotButton.move(820, 285)

        # behind the back
        self.behindTheBackLabel = QLabel("Behind the\n Back Shot", self)
        self.behindTheBackLabel.resize(200, 50)
        self.behindTheBackLabel.setStyleSheet(
            "color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.behindTheBackLabel.move(1043, 350)

        self.behindTheBackButton = QPushButton('', self)
        self.behindTheBackButton.setStyleSheet("background-color: transparent;")
        self.behindTheBackButton.setIcon(QtGui.QIcon('images/behindTheBackIcon.png'))
        self.behindTheBackButton.setIconSize(QtCore.QSize(130, 64))
        self.behindTheBackButton.resize(130, 64)
        self.behindTheBackButton.move(1025, 285)

        # bridge
        self.bridgeLabel = QLabel("Bridge Shot", self)
        self.bridgeLabel.resize(110, 50)
        self.bridgeLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.bridgeLabel.move(835, 485)

        self.bridgeButton = QPushButton('', self)
        self.bridgeButton.setStyleSheet("background-color: transparent;")
        self.bridgeButton.setIcon(QtGui.QIcon('images/bridgeIcon.png'))
        self.bridgeButton.setIconSize(QtCore.QSize(130, 64))
        self.bridgeButton.resize(130, 64)
        self.bridgeButton.move(820, 430)

        # jump shot
        self.jumpShotLabel = QLabel("Jump Shot", self)
        self.jumpShotLabel.resize(100, 50)
        self.jumpShotLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.jumpShotLabel.move(1035, 485)

        self.jumpShotButton = QPushButton('', self)
        self.jumpShotButton.setStyleSheet("background-color: transparent;")
        self.jumpShotButton.setIcon(QtGui.QIcon('images/jumpShotIcon.png'))
        self.jumpShotButton.setIconSize(QtCore.QSize(130, 64))
        self.jumpShotButton.resize(130, 64)
        self.jumpShotButton.move(1020, 430)

        # same shot
        self.sameShotLabel = QLabel("Same Turn", self)
        self.sameShotLabel.resize(200, 50)
        self.sameShotLabel.setStyleSheet(
            "color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.sameShotLabel.move(835, 645)

        self.sameShotButton = QPushButton('', self)
        self.sameShotButton.setStyleSheet("background-color: transparent;")
        self.sameShotButton.setIcon(QtGui.QIcon('images/sameShotIcon.png'))
        self.sameShotButton.setIconSize(QtCore.QSize(130, 94))
        self.sameShotButton.resize(130, 94)
        self.sameShotButton.move(820, 555)

        # unintentional shot
        self.unintentionalShotLabel = QLabel("Unintentional\n        Shot", self)
        self.unintentionalShotLabel.resize(200, 50)
        self.unintentionalShotLabel.setStyleSheet(
            "color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        self.unintentionalShotLabel.move(1027, 650)

        self.unintentionalShotButton = QPushButton("", self)
        self.unintentionalShotButton.setStyleSheet("background-color: transparent;")
        self.unintentionalShotButton.setIcon(QtGui.QIcon('images/unintentionalShotRed.png'))
        self.unintentionalShotButton.setIconSize(QtCore.QSize(130, 94))
        self.unintentionalShotButton.resize(130, 94)
        self.unintentionalShotButton.move(1020, 555)

        # mapping buttons
        self.jumpShotButton.clicked.connect(self.toggleJumpShot)
        self.bankShotButton.clicked.connect(self.toggleBankShot)
        self.bridgeButton.clicked.connect(self.toggleBridgeShot)
        self.behindTheBackButton.clicked.connect(self.toggleBehindTheBackShot)
        self.sunkOffBreakButton.clicked.connect(self.toggleSunkOffBreak)
        self.unintentionalShotButton.clicked.connect(self.toggleUnintentionalShot)
        self.sameShotButton.clicked.connect(self.toggleSameShot)

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
                "color: rgb(0, 135, 32); font-size: 20px; background-color: transparent;")

        self.jumpShot = not self.jumpShot

    def toggleBankShot(self):
        if self.bankShot:
            self.bankShotLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")

        else:
            self.bankShotLabel.setStyleSheet(
                "color: rgb(0, 135, 32); font-size: 20px; background-color: transparent;")

        self.bankShot = not self.bankShot

    def toggleBridgeShot(self):
        if self.bridgeShot:
            self.bridgeLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")

        else:
            self.bridgeLabel.setStyleSheet("color: rgb(0, 135, 32); font-size: 20px; background-color: transparent;")

        self.bridgeShot = not self.bridgeShot

    def toggleBehindTheBackShot(self):
        if self.behindTheBackShot:
            self.behindTheBackLabel.setStyleSheet(
                "color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")

        else:
            self.behindTheBackLabel.setStyleSheet(
                "color: rgb(0, 135, 32); font-size: 20px; background-color: transparent;")

        self.behindTheBackShot = not self.behindTheBackShot

    def toggleSunkOffBreak(self):
        if self.breakingPlayerTurn and len(self.turnLog) < 2:
            if self.sunkOffBreak:
                self.sunkOffBreakButton.setStyleSheet("QPushButton{"
                                                      "color: rgb(255, 69, 40); border-style: outset; border-width: 4px;"
                                                      "background-color: rgb(0, 40, 80);"
                                                      "font-size: 20px;"
                                                      "border-radius: 20px;"
                                                      "}"
                                                      "QPushButton:hover{"
                                                      "background-color: rgb(0, 76, 153);"
                                                      "}"
                                                      )
            else:
                self.sunkOffBreakButton.setStyleSheet("QPushButton{"
                                                      "color: rgb(0, 135, 32); border-style: outset; border-width: 4px;"
                                                      "background-color: rgb(0, 40, 80);"
                                                      "font-size: 20px;"
                                                      "border-radius: 20px;"
                                                      "}"
                                                      "QPushButton:hover{"
                                                      "background-color: rgb(0, 76, 153);"
                                                      "}"
                                                      )
        self.sunkOffBreak = not self.sunkOffBreak

    def toggleUnintentionalShot(self):
        if self.unintentionalShot:
            self.unintentionalShotLabel.setStyleSheet(
                "color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
            self.unintentionalShotButton.setIcon(QtGui.QIcon('images/unintentionalShotRed.png'))
        else:
            self.unintentionalShotLabel.setStyleSheet(
                "color: rgb(0, 135, 32); font-size: 20px; background-color: transparent;")
            self.unintentionalShotButton.setIcon(QtGui.QIcon('images/unintentionalShotGreen.png'))
        self.unintentionalShot = not self.unintentionalShot

    def toggleSameShot(self):
        if self.sameShot:
            self.sameShotLabel.setStyleSheet("color: rgb(255, 69, 40); font-size: 20px; background-color: transparent;")
        else:
            self.sameShotLabel.setStyleSheet("color: rgb(0, 135, 32); font-size: 20px; background-color: transparent;")

        self.sameShot = not self.sameShot

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

    def wasPlayerShootingForEightBall(self):
        # determining whether the player is shooting for the 8-ball
        playerOnEightball = True

        if not self.openTable:
            # breaking player sunk the ball
            if self.breakingPlayerTurn:
                # breaking player is solids
                if self.breakingPlayer == self.solids:
                    for ball in self.solidBalls:
                        if ball in self.ballsOnTable:
                            playerOnEightball = False

                # breaking player is stripes
                elif self.breakingPlayer == self.stripes:
                    for ball in self.stripeBalls:
                        if ball in self.ballsOnTable:
                            playerOnEightball = False

            # incoming player sunk the ball
            elif not self.breakingPlayerTurn:
                # incoming player is solids
                if self.incomingPlayer == self.solids:
                    for ball in self.solidBalls:
                        if ball in self.ballsOnTable:
                            playerOnEightball = False

                # incoming player is stripes
                elif self.incomingPlayer == self.stripes:
                    for ball in self.stripeBalls:
                        if ball in self.ballsOnTable:
                            playerOnEightball = False

        return playerOnEightball

    def turnOffShotTypeButtons(self):
        if self.bankShot:
            self.toggleBankShot()

        if self.jumpShot:
            self.toggleJumpShot()

        if self.behindTheBackShot:
            self.toggleBehindTheBackShot()

        if self.bridgeShot:
            self.toggleBridgeShot()

        if self.sunkOffBreak:
            self.toggleSunkOffBreak()

        if self.unintentionalShot:
            self.toggleUnintentionalShot()

    def didPlayerSinkOwnBallType(self, ball):
        playerSunkOwnBallType = True

        # if the table is not open, we must check
        if not self.openTable:
            # the breaking player sunk the ball
            if self.breakingPlayerTurn:
                # the breaking player is solids
                if self.solids == self.breakingPlayer:
                    if ball not in self.solidBalls:
                        playerSunkOwnBallType = False

                # the breaking player is stripes
                elif self.stripes == self.breakingPlayer:
                    if ball not in self.stripeBalls:
                        playerSunkOwnBallType = False

            # the incoming player sunk the ball
            elif not self.breakingPlayerTurn:
                # the incoming player is solids
                if self.solids == self.incomingPlayer:
                    if ball not in self.solidBalls:
                        playerSunkOwnBallType = False

                # the incoming player is stripes
                elif self.stripes == self.incomingPlayer:
                    if ball not in self.stripeBalls:
                        playerSunkOwnBallType = False

        return playerSunkOwnBallType

    def sinkBall(self, ball, pocket):
        # if this is the first ball sunk, we must update solids/stripes
        if not self.sunkOffBreak and self.solids == "?" and self.stripes == "?":
            # breaking player sunk this ball
            if self.breakingPlayerTurn:
                # the ball was a solid
                if ball in self.solidBalls:
                    self.solids = self.breakingPlayer
                    self.stripes = self.incomingPlayer
                    self.currentGame.solids = self.solids
                    self.currentGame.stripes = self.stripes
                    self.breakingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/solids.png"))
                    self.incomingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/stripes.png"))

                    # the breaking player sunk the solid ball, we must see if any stripes were sunk off the break
                    for ballSunk in self.sinkLog:
                        ball = ballSunk[0]
                        # updating the current game's stats if opponent's ball was sunk
                        if ball in self.stripeBalls:
                            self.currentGame.BPOpponentBallsSunk += 1
                            self.currentGame.IPBallsSunkByOpponent += 1

                # the ball was a stripe
                elif ball in self.stripeBalls:
                    self.stripes = self.breakingPlayer
                    self.solids = self.incomingPlayer
                    self.currentGame.solids = self.solids
                    self.currentGame.stripes = self.stripes
                    self.breakingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/stripes.png"))
                    self.incomingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/solids.png"))

                    # the breaking player sunk the striped ball, we must see if any solids were sunk off the break
                    for ballSunk in self.sinkLog:
                        ball = ballSunk[0]
                        # updating the current game's stats if opponent's ball was sunk
                        if ball in self.solidBalls:
                            self.currentGame.BPOpponentBallsSunk += 1
                            self.currentGame.IPBallsSunkByOpponent += 1

            # incoming player sunk this ball
            elif not self.breakingPlayerTurn:
                # the ball was a solid
                if ball in self.solidBalls:
                    self.solids = self.incomingPlayer
                    self.stripes = self.breakingPlayer
                    self.currentGame.solids = self.solids
                    self.currentGame.stripes = self.stripes
                    self.incomingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/solids.png"))
                    self.breakingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/stripes.png"))

                    # the incoming player sunk the solid ball, we must see if any stripes were sunk off the break
                    for ballSunk in self.sinkLog:
                        ball = ballSunk[0]
                        # updating the current game's stats if opponent's ball was sunk
                        if ball in self.stripeBalls:
                            self.currentGame.IPOpponentBallsSunk += 1
                            self.currentGame.BPBallsSunkByOpponent += 1

                # the ball was a stripe
                elif ball in self.stripeBalls:
                    self.stripes = self.incomingPlayer
                    self.solids = self.breakingPlayer
                    self.currentGame.solids = self.solids
                    self.currentGame.stripes = self.stripes
                    self.incomingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/stripes.png"))
                    self.breakingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/solids.png"))

                    # the incoming player sunk the striped ball, we must see if any solids were sunk off the break
                    for ballSunk in self.sinkLog:
                        ball = ballSunk[0]
                        # updating the current game's stats if opponent's ball was sunk
                        if ball in self.solidBalls:
                            self.currentGame.IPOpponentBallsSunk += 1
                            self.currentGame.BPBallsSunkByOpponent += 1

            self.openTable = False

            # printing an update on ball types
            print(f"{self.solids} is now solids!")
            print(f"{self.stripes} is now stripes!")

        # determining whether the player is shooting for the 8-ball
        playerOnEightBall = self.wasPlayerShootingForEightBall()

        # determining whether the player sunk one of their ball types
        playerSunkOwnBallType = self.didPlayerSinkOwnBallType(ball)

        # creating a tuple containing relevant data from the last sink
        newestSinkEntry = (ball, pocket, self.bankShot, self.behindTheBackShot, self.bridgeShot, self.jumpShot,
                           playerSunkOwnBallType, playerOnEightBall, self.sunkOffBreak, self.unintentionalShot)
        self.currentTurnLog.append(newestSinkEntry)
        self.sinkLog.append(newestSinkEntry)

        # turning off shot type buttons
        self.turnOffShotTypeButtons()

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

    def moveToGameRecapWindow(self):
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
                    str(int(
                        100 * self.currentGame.IPEightBallShotsMade / self.currentGame.IPEightBallShotsTaken)) + "%")

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
                    str(int(
                        100 * self.currentGame.BPEightBallShotsMade / self.currentGame.BPEightBallShotsTaken)) + "%")

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

        # resetting the selected ball
        self.selectedBall = '?'

        # resetting solids/stripes variables
        self.solids = '?'
        self.stripes = '?'
        self.breakingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/openTable.png"))
        self.incomingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/sopenTable.png"))

        # writing the game stats onto the players playing
        writeGameStatsToPlayers(self.currentGame, self.playerDict[self.breakingPlayer],
                                self.playerDict[self.incomingPlayer])

        # moving to the game recap window
        self.windowStack.setCurrentIndex(3)

    def endTurn(self):
        # the player sunk at least 1 ball
        if len(self.currentTurnLog) > 0:
            # looping over the first n-1 shots, where n is the number of shots taken this turn
            # note: we know that all of these shots must've been legal sinks
            for i in range(len(self.currentTurnLog) - 1):
                sink = self.currentTurnLog[i]
                ball = sink[0]
                pocket = sink[1]
                bankShot = sink[2]
                behindTheBackShot = sink[3]
                bridgeShot = sink[4]
                jumpShot = sink[5]
                sunkOffBreak = sink[8]
                unintentionalSink = sink[9]

                # it was the breaking player's turn
                if self.breakingPlayerTurn:
                    # updating the current game object's stats
                    # updating the all-time shooting stats
                    self.currentGame.BPShotsTaken += 1
                    self.currentGame.BPShotsMade += 1
                    self.BPPocketLetterDict[pocket] += 1

                    # updating the type of shot stats
                    if bankShot:
                        self.currentGame.BPBankShotsTaken += 1
                        self.currentGame.BPBankShotsMade += 1

                    if behindTheBackShot:
                        self.currentGame.BPBehindTheBackShotsTaken += 1
                        self.currentGame.BPBehindTheBackShotsMade += 1

                    if bridgeShot:
                        self.currentGame.BPBridgeShotsTaken += 1
                        self.currentGame.BPBridgeShotsMade += 1

                    if jumpShot:
                        self.currentGame.BPJumpShotsTaken += 1
                        self.currentGame.BPJumpShotsMade += 1

                    if sunkOffBreak:
                        self.currentGame.ballsSunkOffBreak += 1

                    if unintentionalSink:
                        self.currentGame.BPUnintentionalSinks += 1
                    else:
                        self.currentGame.BPIntentionalSinks += 1

                # it was the incoming player's turn
                elif not self.breakingPlayerTurn:
                    # updating the current game object's stats
                    # updating the all-time shooting stats
                    self.currentGame.IPShotsTaken += 1
                    self.currentGame.IPShotsMade += 1
                    self.IPPocketLetterDict[pocket] += 1

                    # updating the type of shot stats
                    if bankShot:
                        self.currentGame.IPBankShotsTaken += 1
                        self.currentGame.IPBankShotsMade += 1

                    if behindTheBackShot:
                        self.currentGame.IPBehindTheBackShotsTaken += 1
                        self.currentGame.IPBehindTheBackShotsMade += 1

                    if bridgeShot:
                        self.currentGame.IPBridgeShotsTaken += 1
                        self.currentGame.IPBridgeShotsMade += 1

                    if jumpShot:
                        self.currentGame.IPJumpShotsTaken += 1
                        self.currentGame.IPJumpShotsMade += 1

                    # Note: the program does not check for sunkOffBreak here, that is because the incoming player
                    # can not sink a ball off the break

                    if unintentionalSink:
                        self.currentGame.IPUnintentionalSinks += 1
                    else:
                        self.currentGame.IPIntentionalSinks += 1

                # updating the graphics of the balls that were sunk
                self.ballButtonDict[ball].hide()

            lastShot = self.currentTurnLog[-1]
            # the player sunk the 8-ball on their last shot, the game is now over
            if lastShot[0] == "8":
                ball = lastShot[0]
                pocket = lastShot[1]
                bankShot = lastShot[2]
                behindTheBackShot = lastShot[3]
                bridgeShot = lastShot[4]
                jumpShot = lastShot[5]
                playerShootingForEight = lastShot[7]
                sunkOffBreak = lastShot[8]
                unintentionalSink = lastShot[9]
                # there are two ways to sink the break
                # 1) player was shooting for the eight and sunk off the break
                # 2) player was shooting for the eight and sunk the eight intentionally
                playerWonFromSinkingEight = playerShootingForEight and (sunkOffBreak or not unintentionalSink)

                # it was the breaking player's turn
                if self.breakingPlayerTurn:
                    # the breaking player wins after sinking the 8-ball
                    if playerWonFromSinkingEight:
                        # updating the all-time shooting stats
                        self.currentGame.BPShotsTaken += 1
                        self.currentGame.BPShotsMade += 1
                        self.currentGame.BPIntentionalSinks += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.BPBankShotsTaken += 1
                            self.currentGame.BPBankShotsMade += 1

                        if behindTheBackShot:
                            self.currentGame.BPBehindTheBackShotsTaken += 1
                            self.currentGame.BPBehindTheBackShotsMade += 1

                        if bridgeShot:
                            self.currentGame.BPBridgeShotsTaken += 1
                            self.currentGame.BPBridgeShotsMade += 1

                        if jumpShot:
                            self.currentGame.BPJumpShotsTaken += 1
                            self.currentGame.BPJumpShotsMade += 1

                        if sunkOffBreak:
                            self.currentGame.ballsSunkOffBreak += 1

                        if unintentionalSink:
                            self.currentGame.BPUnintentionalSinks += 1

                        elif not unintentionalSink:
                            self.currentGame.BPIntentionalSinks += 1

                        # updating 8-ball shooting stats
                        self.currentGame.BPEightBallShotsTaken += 1
                        self.currentGame.BPEightBallShotsMade += 1

                        # updating the current game object's end of game stats
                        self.currentGame.winner = self.breakingPlayer
                        self.currentGame.loser = self.incomingPlayer

                    # the breaking player loses after sinking the 8-ball
                    elif not playerWonFromSinkingEight:
                        # updating the all-time shooting stats
                        self.currentGame.BPShotsTaken += 1
                        self.currentGame.BPShotsMissed += 1
                        self.currentGame.BPUnintentionalSinks += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.BPBankShotsTaken += 1
                            self.currentGame.BPBankShotsMissed += 1

                        if behindTheBackShot:
                            self.currentGame.BPBehindTheBackShotsTaken += 1
                            self.currentGame.BPBehindTheBackShotsMissed += 1

                        if bridgeShot:
                            self.currentGame.BPBridgeShotsTaken += 1
                            self.currentGame.BPBridgeShotsMissed += 1

                        if jumpShot:
                            self.currentGame.BPJumpShotsTaken += 1
                            self.currentGame.BPJumpShotsMissed += 1

                        # Note: we are not checking if the 8-ball was sunk off the break as the player would've won

                        if unintentionalSink:
                            self.currentGame.BPUnintentionalSinks += 1

                        elif not unintentionalSink:
                            self.currentGame.BPIntentionalSinks += 1

                        # updating the current game object's end of game stats
                        self.currentGame.winner = self.incomingPlayer
                        self.currentGame.loser = self.breakingPlayer
                        self.currentGame.gameWonByChoke = True

                # it was the incoming player's turn
                elif not self.breakingPlayerTurn:
                    # the incoming player wins after sinking the 8-ball
                    if playerWonFromSinkingEight:
                        # updating the all-time shooting stats
                        self.currentGame.IPShotsTaken += 1
                        self.currentGame.IPShotsMade += 1
                        self.currentGame.IPIntentionalSinks += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.IPBankShotsTaken += 1
                            self.currentGame.IPBankShotsMade += 1

                        if behindTheBackShot:
                            self.currentGame.IPBehindTheBackShotsTaken += 1
                            self.currentGame.IPBehindTheBackShotsMade += 1

                        if bridgeShot:
                            self.currentGame.IPBridgeShotsTaken += 1
                            self.currentGame.IPBridgeShotsMade += 1

                        if jumpShot:
                            self.currentGame.IPJumpShotsTaken += 1
                            self.currentGame.IPJumpShotsMade += 1

                        # updating 8-ball shooting stats
                        self.currentGame.IPEightBallShotsTaken += 1
                        self.currentGame.IPEightBallShotsMade += 1

                        # updating the current game object's end of game stats
                        self.currentGame.winner = self.incomingPlayer
                        self.currentGame.loser = self.breakingPlayer

                    # the incoming player loses after sinking the 8-ball
                    elif not playerWonFromSinkingEight:
                        # updating the all-time shooting stats
                        self.currentGame.IPShotsTaken += 1
                        self.currentGame.IPShotsMissed += 1
                        self.currentGame.IPUnintentionalSinks += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.IPBankShotsTaken += 1
                            self.currentGame.IPBankShotsMissed += 1

                        if behindTheBackShot:
                            self.currentGame.IPBehindTheBackShotsTaken += 1
                            self.currentGame.IPBehindTheBackShotsMissed += 1

                        if bridgeShot:
                            self.currentGame.IPBridgeShotsTaken += 1
                            self.currentGame.IPBridgeShotsMissed += 1

                        if jumpShot:
                            self.currentGame.IPJumpShotsTaken += 1
                            self.currentGame.IPJumpShotsMissed += 1

                        # updating the current game object's end of game stats
                        self.currentGame.winner = self.breakingPlayer
                        self.currentGame.loser = self.incomingPlayer
                        self.currentGame.gameWonByChoke = True

                # the game is now over, moving to the game recap window
                self.moveToGameRecapWindow()

            # the player did not sink the 8-ball on their last shot, the game is not over
            elif lastShot[0] != "8":
                ball = lastShot[0]
                pocket = lastShot[1]
                bankShot = lastShot[2]
                behindTheBackShot = lastShot[3]
                bridgeShot = lastShot[4]
                jumpShot = lastShot[5]

                # the last shot was a scratch (an opponent's or the cue ball was sunk)
                if not lastShot[6] or lastShot[0] == "cue":
                    # Note: we do not check if the cue was sunk off the break as it is not considered a ball
                    # Note: we do not check if sinking the cue was intentional, as sinking the cue is never intentional

                    # it was the breaking player's turn
                    if self.breakingPlayerTurn:
                        # updating the all-time shooting stats
                        self.currentGame.BPShotsTaken += 1
                        self.currentGame.BPShotsMissed += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.BPBankShotsTaken += 1
                            self.currentGame.BPBankShotsMissed += 1

                        if behindTheBackShot:
                            self.currentGame.BPBehindTheBackShotsTaken += 1
                            self.currentGame.BPBehindTheBackShotsMissed += 1

                        if bridgeShot:
                            self.currentGame.BPBridgeShotsTaken += 1
                            self.currentGame.BPBridgeShotsMissed += 1

                        if jumpShot:
                            self.currentGame.BPJumpShotsTaken += 1
                            self.currentGame.BPJumpShotsMissed += 1

                        # updating scratch stats
                        self.currentGame.BPScratchesMade += 1
                        self.currentGame.IPOpponentScratches += 1

                        # updating opponent balls sunk stats if applicable
                        if not lastShot[6]:
                            self.currentGame.BPOpponentBallsSunk += 1
                            self.currentGame.IPBallsSunkByOpponent += 1

                        # returning the cue ball to the table if the cue ball was sunk
                        if lastShot[0] == "cue":
                            self.returnBallGraphics("cue")

                    # it was the incoming player's turn
                    elif not self.breakingPlayerTurn:
                        # updating the all-time shooting stats
                        self.currentGame.IPShotsTaken += 1
                        self.currentGame.IPShotsMissed += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.IPBankShotsTaken += 1
                            self.currentGame.IPBankShotsMissed += 1

                        if behindTheBackShot:
                            self.currentGame.IPBehindTheBackShotsTaken += 1
                            self.currentGame.IPBehindTheBackShotsMissed += 1

                        if bridgeShot:
                            self.currentGame.IPBridgeShotsTaken += 1
                            self.currentGame.IPBridgeShotsMissed += 1

                        if jumpShot:
                            self.currentGame.IPJumpShotsTaken += 1
                            self.currentGame.IPJumpShotsMissed += 1

                        # updating scratch stats
                        self.currentGame.IPScratchesMade += 1
                        self.currentGame.BPOpponentScratches += 1

                        # updating opponent balls sunk stats if applicable
                        if not lastShot[6]:
                            self.currentGame.IPOpponentBallsSunk += 1
                            self.currentGame.BPBallsSunkByOpponent += 1

                    # updating the ball graphics if the player sunk an opponent's ball
                    if not lastShot[6]:
                        self.ballButtonDict[ball].hide()

                    # updating the cue ball graphics if sunk
                    if ball == "cue":
                        self.returnBallGraphics("cue")

                # the last sink was of the player's ball type
                elif lastShot[6]:
                    # adding a miss to the current turn log
                    latestMiss = ("miss", self.bankShot, self.behindTheBackShot, self.bridgeShot, self.jumpShot,
                                  self.wasPlayerShootingForEightBall())
                    self.currentTurnLog.append(latestMiss)

                    # it was the breaking player's turn
                    if self.breakingPlayerTurn:
                        # updating the current game object's stats
                        # updating the stats for the sink
                        # updating the all-time shooting stats
                        self.currentGame.BPShotsTaken += 1
                        self.currentGame.BPShotsMade += 1
                        self.BPPocketLetterDict[pocket] += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.BPBankShotsTaken += 1
                            self.currentGame.BPBankShotsMade += 1

                        if behindTheBackShot:
                            self.currentGame.BPBehindTheBackShotsTaken += 1
                            self.currentGame.BPBehindTheBackShotsMade += 1

                        if bridgeShot:
                            self.currentGame.BPBridgeShotsTaken += 1
                            self.currentGame.BPBridgeShotsMade += 1

                        if jumpShot:
                            self.currentGame.BPJumpShotsTaken += 1
                            self.currentGame.BPJumpShotsMade += 1

                        # updating the stats for the latest miss
                        # updating the all-time shooting stats
                        self.currentGame.BPShotsTaken += 1
                        self.currentGame.BPShotsMissed += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.BPBankShotsTaken += 1
                            self.currentGame.BPBankShotsMissed += 1

                        if behindTheBackShot:
                            self.currentGame.BPBehindTheBackShotsTaken += 1
                            self.currentGame.BPBehindTheBackShotsMissed += 1

                        if bridgeShot:
                            self.currentGame.BPBridgeShotsTaken += 1
                            self.currentGame.BPBridgeShotsMissed += 1

                        if jumpShot:
                            self.currentGame.BPJumpShotsTaken += 1
                            self.currentGame.BPJumpShotsMissed += 1

                        # updating 8-ball shooting stats if applicable
                        if self.wasPlayerShootingForEightBall():
                            self.currentGame.BPEightBallShotsTaken += 1
                            self.currentGame.BPEightBallShotsMissed += 1

                    # it was the incoming player's turn
                    elif not self.breakingPlayerTurn:
                        # updating the current game object's stats
                        # updating the stats for the sink
                        # updating the all-time shooting stats
                        self.currentGame.IPShotsTaken += 1
                        self.currentGame.IPShotsMade += 1
                        self.IPPocketLetterDict[pocket] += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.IPBankShotsTaken += 1
                            self.currentGame.IPBankShotsMade += 1
                        if behindTheBackShot:
                            self.currentGame.IPBehindTheBackShotsTaken += 1
                            self.currentGame.IPBehindTheBackShotsMade += 1

                        if bridgeShot:
                            self.currentGame.IPBridgeShotsTaken += 1
                            self.currentGame.IPBridgeShotsMade += 1

                        if jumpShot:
                            self.currentGame.IPJumpShotsTaken += 1
                            self.currentGame.IPJumpShotsMade += 1

                        # updating the stats for the latest miss
                        # updating the all-time shooting stats
                        self.currentGame.IPShotsTaken += 1
                        self.currentGame.IPShotsMissed += 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.IPBankShotsTaken += 1
                            self.currentGame.IPBankShotsMissed += 1

                        if behindTheBackShot:
                            self.currentGame.IPBehindTheBackShotsTaken += 1
                            self.currentGame.IPBehindTheBackShotsMissed += 1

                        if bridgeShot:
                            self.currentGame.IPBridgeShotsTaken += 1
                            self.currentGame.IPBridgeShotsMissed += 1

                        if jumpShot:
                            self.currentGame.IPJumpShotsTaken += 1
                            self.currentGame.IPJumpShotsMissed += 1

                            # updating 8-ball shooting stats if applicable
                            if self.wasPlayerShootingForEightBall():
                                self.currentGame.IPEightBallShotsTaken += 1
                                self.currentGame.IPEightBallShotsMissed += 1

                    # updating the ball button's graphics
                    self.ballButtonDict[ball].hide()

        # the player sunk no balls
        elif len(self.currentTurnLog) == 0:
            # determining if the player was shooting for the 8-ball
            playerShootingForEightBall = self.wasPlayerShootingForEightBall()

            # creating a miss and appending it to the current turn log
            miss = ("miss", self.bankShot, self.behindTheBackShot, self.bridgeShot, self.jumpShot,
                    playerShootingForEightBall)
            self.currentTurnLog.append(miss)

            # updating the miss stats to the current game object
            # it was the breaking player's turn
            if self.breakingPlayerTurn:
                # updating the all-time shooting stats
                self.currentGame.BPShotsTaken += 1
                self.currentGame.BPShotsMissed += 1

                # updating the type of shot stats
                if self.bankShot:
                    self.currentGame.BPBankShotsTaken += 1
                    self.currentGame.BPBankShotsMissed += 1

                if self.behindTheBackShot:
                    self.currentGame.BPBehindTheBackShotsTaken += 1
                    self.currentGame.BPBehindTheBackShotsMissed += 1

                if self.bridgeShot:
                    self.currentGame.BPBridgeShotsTaken += 1
                    self.currentGame.BPBridgeShotsMissed += 1

                if self.jumpShot:
                    self.currentGame.BPJumpShotsTaken += 1
                    self.currentGame.BPJumpShotsMissed += 1

                # updating 8-ball shooting stats if applicable
                if playerShootingForEightBall:
                    self.currentGame.BPEightBallShotsTaken += 1
                    self.currentGame.BPEightBallShotsMissed += 1

            # it was the incoming player's turn
            elif not self.breakingPlayerTurn:
                # updating the all-time shooting stats
                self.currentGame.IPShotsTaken += 1
                self.currentGame.IPShotsMissed += 1

                # updating the type of shot stats
                if self.bankShot:
                    self.currentGame.IPBankShotsTaken += 1
                    self.currentGame.IPBankShotsMissed += 1

                if self.behindTheBackShot:
                    self.currentGame.IPBehindTheBackShotsTaken += 1
                    self.currentGame.IPBehindTheBackShotsMissed += 1

                if self.bridgeShot:
                    self.currentGame.IPBridgeShotsTaken += 1
                    self.currentGame.IPBridgeShotsMissed += 1

                if self.jumpShot:
                    self.currentGame.IPJumpShotsTaken += 1
                    self.currentGame.IPJumpShotsMissed += 1

                # updating 8-ball shooting stats if applicable
                if playerShootingForEightBall:
                    self.currentGame.IPEightBallShotsTaken += 1
                    self.currentGame.IPEightBallShotsMissed += 1

        # printing a recap of the turn
        print("\n~~~~~TURN ENDED~~~~~")
        print(f"Printing a recap of turn {self.turnNumber}")
        if self.breakingPlayerTurn:
            print("The breaking player's latest turn:")
        else:
            print("The incoming player's latest turn:")
        print(f"\t{self.currentTurnLog}")
        print("The Game's updated sink log:")
        print(f"\t{self.sinkLog}")
        print("The game's updated turn log:")
        print(f"\t{self.turnLog}")

        # appending the current turn log to the turn log
        self.turnLog.append(self.currentTurnLog)

        # resetting the current turn log now that the turn is over
        self.currentTurnLog = []

        # toggling off sunkOffBreak
        if self.sunkOffBreak:
            self.toggleSunkOffBreak()

        # updating info regarding the turn
        self.breakingPlayerTurn = not self.breakingPlayerTurn
        self.turnNumber += 1

        # updating and toggling graphics now that the turn is over
        if self.breakingPlayerTurn:
            self.shootingIcon.move(self.shootingIconCoordinateDict['breakingPlayer'][0],
                                   self.shootingIconCoordinateDict['breakingPlayer'][1])
        else:
            self.shootingIcon.move(self.shootingIconCoordinateDict['incomingPlayer'][0],
                                   self.shootingIconCoordinateDict['incomingPlayer'][1])

        # toggling/turning off shot buttons
        self.turnOffShotTypeButtons()

    def undoTurn(self):
        # there is a turn to undo
        if len(self.turnLog) > 0:
            # for loop iterating over ever shot in the latest turn, in reverse order
            turnToUndo = self.turnLog[-1]
            for i in range(1, len(turnToUndo) + 1):
                shotToUndo = turnToUndo[-i]

                # the shot to undo is a miss
                if shotToUndo[0] == "miss":
                    bankShot = shotToUndo[1]
                    behindTheBackShot = shotToUndo[2]
                    bridgeShot = shotToUndo[3]
                    jumpShot = shotToUndo[4]
                    playerShootingForEightBall = shotToUndo[5]

                    # it was the breaking player's miss
                    if not self.breakingPlayerTurn:
                        # undoing the all-time stats
                        self.currentGame.BPShotsTaken -= 1
                        self.currentGame.BPShotsMissed -= 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.BPBankShotsTaken -= 1
                            self.currentGame.BPBankShotsMissed -= 1

                        if behindTheBackShot:
                            self.currentGame.BPBehindTheBackShotsTaken -= 1
                            self.currentGame.BPBehindTheBackShotsMissed -= 1

                        if bridgeShot:
                            self.currentGame.BPBridgeShotsTaken -= 1
                            self.currentGame.BPBridgeShotsMissed -= 1

                        if jumpShot:
                            self.currentGame.BPJumpShotsTaken -= 1
                            self.currentGame.BPJumpShotsMissed -= 1

                        # updating 8-ball shooting stats if applicable
                        if playerShootingForEightBall:
                            self.currentGame.BPEightBallShotsTaken -= 1
                            self.currentGame.BPEightBallShotsMissed -= 1

                    # it was the incoming player's miss
                    elif self.breakingPlayerTurn:
                        # undoing the all-time stats
                        self.currentGame.IPShotsTaken -= 1
                        self.currentGame.IPShotsMissed -= 1

                        # updating the type of shot stats
                        if bankShot:
                            self.currentGame.IPBankShotsTaken -= 1
                            self.currentGame.IPBankShotsMissed -= 1

                        if behindTheBackShot:
                            self.currentGame.IPBehindTheBackShotsTaken -= 1
                            self.currentGame.IPBehindTheBackShotsMissed -= 1

                        if bridgeShot:
                            self.currentGame.IPBridgeShotsTaken -= 1
                            self.currentGame.IPBridgeShotsMissed -= 1

                        if jumpShot:
                            self.currentGame.IPJumpShotsTaken -= 1
                            self.currentGame.IPJumpShotsMissed -= 1

                        # updating 8-ball shooting stats if applicable
                        if playerShootingForEightBall:
                            self.currentGame.BPEightBallShotsTaken -= 1
                            self.currentGame.BPEightBallShotsMissed -= 1

                # the shot to undo is not a miss
                elif shotToUndo[0] != "miss":
                    ball = shotToUndo[0]
                    pocket = shotToUndo[1]
                    bankShot = shotToUndo[2]
                    behindTheBackShot = shotToUndo[3]
                    bridgeShot = shotToUndo[4]
                    jumpShot = shotToUndo[5]
                    playerSunkOwnBallType = shotToUndo[6]
                    playerOnEightBall = shotToUndo[7]
                    sunkOffBreak = shotToUndo[8]
                    unintentionalSink = shotToUndo[9]

                    # the player sunk their own ball
                    if playerSunkOwnBallType and ball != "cue":
                        # it was the breaking player's sink
                        if not self.breakingPlayerTurn:
                            # updating the all-time shooting stats
                            self.currentGame.BPShotsTaken -= 1
                            self.currentGame.BPShotsMade -= 1
                            self.BPPocketLetterDict[pocket] -= 1

                            # updating the type of shot stats
                            if bankShot:
                                self.currentGame.BPBankShotsTaken -= 1
                                self.currentGame.BPBankShotsMade -= 1

                            if behindTheBackShot:
                                self.currentGame.BPBehindTheBackShotsTaken -= 1
                                self.currentGame.BPBehindTheBackShotsMade -= 1

                            if bridgeShot:
                                self.currentGame.BPBridgeShotsTaken -= 1
                                self.currentGame.BPBridgeShotsMade -= 1

                            if jumpShot:
                                self.currentGame.BPJumpShotsTaken -= 1
                                self.currentGame.BPJumpShotsMade -= 1

                            if unintentionalSink:
                                self.currentGame.BPUnintentionalSinks -= 1
                            else:
                                self.currentGame.BPIntentionalSinks -= 1

                            if sunkOffBreak:
                                self.currentGame.ballsSunkOffBreak -= 1

                        # it was the incoming player's sink
                        elif self.breakingPlayerTurn:
                            # updating the all-time shooting stats
                            self.currentGame.IPShotsTaken -= 1
                            self.currentGame.IPShotsMade -= 1
                            self.IPPocketLetterDict[pocket] -= 1

                            # updating the type of shot stats
                            if bankShot:
                                self.currentGame.IPBankShotsTaken -= 1
                                self.currentGame.IPBankShotsMade -= 1

                            if behindTheBackShot:
                                self.currentGame.IPBehindTheBackShotsTaken -= 1
                                self.currentGame.IPBehindTheBackShotsMade -= 1

                            if bridgeShot:
                                self.currentGame.IPBridgeShotsTaken -= 1
                                self.currentGame.IPBridgeShotsMade -= 1

                            if jumpShot:
                                self.currentGame.IPJumpShotsTaken -= 1
                                self.currentGame.IPJumpShotsMade -= 1

                            if unintentionalSink:
                                self.currentGame.IPUnintentionalSinks -= 1
                            else:
                                self.currentGame.IPIntentionalSinks -= 1

                    # the player scratched (sunk their opponent's ball or the cue ball)
                    elif not playerSunkOwnBallType or ball == "cue":
                        # the breaking player scratched
                        if not self.breakingPlayerTurn:
                            # updating the all-time shooting stats
                            self.currentGame.BPShotsTaken -= 1
                            self.currentGame.BPShotsMissed -= 1

                            # updating the type of shot stats
                            if bankShot:
                                self.currentGame.BPBankShotsTaken -= 1
                                self.currentGame.BPBankShotsMissed -= 1

                            if behindTheBackShot:
                                self.currentGame.BPBehindTheBackShotsTaken -= 1
                                self.currentGame.BPBehindTheBackShotsMissed -= 1

                            if bridgeShot:
                                self.currentGame.BPBridgeShotsTaken -= 1
                                self.currentGame.BPBridgeShotsMissed -= 1

                            if jumpShot:
                                self.currentGame.BPJumpShotsTaken -= 1
                                self.currentGame.BPJumpShotsMissed -= 1

                            # updating scratch stats
                            self.currentGame.BPScratchesMade -= 1
                            self.currentGame.IPOpponentScratches -= 1

                            # updating opponent balls sunk stats if applicable
                            if not playerSunkOwnBallType:
                                self.currentGame.BPOpponentBallsSunk -= 1
                                self.currentGame.IPBallsSunkByOpponent -= 1

                        # the incoming payer scratched
                        elif self.breakingPlayerTurn:
                            # updating the all-time shooting stats
                            self.currentGame.IPShotsTaken -= 1
                            self.currentGame.IPShotsMissed -= 1

                            # updating the type of shot stats
                            if bankShot:
                                self.currentGame.IPBankShotsTaken -= 1
                                self.currentGame.IPBankShotsMissed -= 1

                            if behindTheBackShot:
                                self.currentGame.IPBehindTheBackShotsTaken -= 1
                                self.currentGame.IPBehindTheBackShotsMissed -= 1

                            if bridgeShot:
                                self.currentGame.IPBridgeShotsTaken -= 1
                                self.currentGame.IPBridgeShotsMissed -= 1

                            if jumpShot:
                                self.currentGame.IPJumpShotsTaken -= 1
                                self.currentGame.IPJumpShotsMissed -= 1

                            # updating scratch stats
                            self.currentGame.IPScratchesMade -= 1
                            self.currentGame.BPOpponentScratches -= 1

                            # updating opponent balls sunk stats if applicable
                            if not playerSunkOwnBallType:
                                self.currentGame.IPOpponentBallsSunk -= 1
                                self.currentGame.BPBallsSunkByOpponent -= 1

                    # checking to see if we have to revert which player is stripes and solids
                    ballsSunk = 0
                    # determining how many non-cue balls have been sunk
                    # TODO: look at all the balls sunk on the break, determine if any of those balls were an opponent's ball
                    for sink in self.sinkLog:
                        ballSunk = sink[0]
                        if ballSunk != "cue":
                            ballsSunk += 1

                    # this was the first ball sunk, we must revert solids/stripes
                    if ballsSunk == 1:
                        # reverting instance variables
                        self.solids = "?"
                        self.stripes = "?"
                        self.openTable = True

                        # reverting the current game object's stats
                        self.currentGame.BPBallGroup = None
                        self.currentGame.IPBallGroup = None
                        self.breakingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/openTable.png"))
                        self.incomingPlayerBallTypeIcon.setPixmap(QtGui.QPixmap("images/openTable.png"))

                    # undoing the graphics for the sunk ball
                    self.returnBallGraphics(ball)

                    # removing the sink from the sink log
                    self.sinkLog.pop()

            # removing the latest turn from the turn log
            self.turnLog.pop()

            # setting the current turn to the last turn in the turn log if applicable
            if len(self.turnLog) > 0:
                self.currentTurnLog = self.turnLog[-1]

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

        # no turns have been played, we are unable to undo the turn
        else:
            print("\n~~~~~UNABLE TO UNDO TURN~~~~~")
            print("\tNo moves in turn log to remove")
