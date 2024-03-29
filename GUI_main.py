from datetime import date
from PyQt5.QtWidgets import *
import sys
from reading import findNewestStatSheetName
from reading import parseData
from writing import writeNewCSV, writeGameStatsToPlayers
from menuWindow import MenuWindow
from selectPlayersWindow import SelectPlayersWindow
from recordStatsWindow import RecordStatsWindow
from gameRecapWindow import GameRecapWindow
from objects import Game, Player

# variables
breakingPlayer = '?'
incomingPlayer = '?'
selectedBall = '?'
selectedPocket = '?'
currentGame = Game()


# mapped buttons
def moveToSelectPlayers():
    windowStack.setCurrentIndex(1)


def moveToMenu(currentGame):
    # writing a new csv
    gameList.append(recordStatsWindow.currentGame)
    writeNewCSV(playerList, gameList)

    currentGame = Game()
    # moving to the menu window
    windowStack.setCurrentIndex(0)


def moveToRecordStats():
    # checking that two players are not playing themselves
    if selectPlayersWindow.breakingPlayerComboBox.currentText() != selectPlayersWindow.incomingPlayerComboBox.currentText():

        # move to record stats window and update recordStatsWindow's instance variables
        windowStack.setCurrentIndex(2)

        breakingPlayerName = selectPlayersWindow.breakingPlayerComboBox.currentText()[5:]
        incomingPlayerName = selectPlayersWindow.incomingPlayerComboBox.currentText()[5:]
        recordStatsWindow.breakingPlayerLabel.setText(breakingPlayerName)
        recordStatsWindow.incomingPlayerLabel.setText(incomingPlayerName)
        breakingPlayer = playerDict[breakingPlayerName]
        incomingPlayer = playerDict[incomingPlayerName]
        recordStatsWindow.breakingPlayer = breakingPlayer
        recordStatsWindow.incomingPlayer = incomingPlayer
        recordStatsWindow.playerDict = playerDict
        recordStatsWindow.gameRecapWindow = gameRecapWindow
        # I don't know if this is necessary
        recordStatsWindow.breakingPlayer = breakingPlayer

        # creating a new object for the current game
        currentGame = Game()
        currentGame.gameNumber = len(gameList)
        currentGame.BP = breakingPlayer.playerName
        currentGame.IP = incomingPlayer.playerName
        currentGame.date = date.today()

        recordStatsWindow.breakingPlayerRecordLabel.setText( "(" + str(playerDict[currentGame.BP].wins)
                                                            + " - " + str(playerDict[currentGame.IP].losses) + ")")
        recordStatsWindow.incomingPlayerRecordLabel.setText("(" + str(playerDict[currentGame.IP].wins)
                                                            + " - " + str(playerDict[currentGame.IP].losses) + ")")
        # I don't know if this is necessary
        recordStatsWindow.breakingPlayer = breakingPlayer

        # changing recordStatsWindow's currentGame instance variable
        recordStatsWindow.currentGame = currentGame
        recordStatsWindow.breakingPlayer = currentGame.BP
        recordStatsWindow.incomingPlayer = currentGame.IP
        recordStatsWindow.windowStack = windowStack
        recordStatsWindow.BPPocketLetterDict = {'A': currentGame.BPBallsSunkInPocketA,
                                                'B': currentGame.BPBallsSunkInPocketB,
                                                'C': currentGame.BPBallsSunkInPocketC,
                                                'D': currentGame.BPBallsSunkInPocketD,
                                                'E': currentGame.BPBallsSunkInPocketE,
                                                'F': currentGame.BPBallsSunkInPocketF}
        recordStatsWindow.IPPocketLetterDict = {'A': currentGame.IPBallsSunkInPocketA,
                                                'B': currentGame.IPBallsSunkInPocketB,
                                                'C': currentGame.IPBallsSunkInPocketC,
                                                'D': currentGame.IPBallsSunkInPocketD,
                                                'E': currentGame.IPBallsSunkInPocketE,
                                                'F': currentGame.IPBallsSunkInPocketF}

        # resetting the turn and sink logs for a new game:
        recordStatsWindow.turnLog = []
        recordStatsWindow.sinkLog = []

        # resetting ballsOnTable list for a new game
        recordStatsWindow.ballsOnTable = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                                          '15']

    else:
        print("\n~~~~~UNABLE TO START GAME~~~~~")
        print("\tPlease select two unique players")


def moveToGameRecap():
    windowStack.setCurrentIndex(3)

# reading data
statSheetName = findNewestStatSheetName()
playerList, gameList, playerDict = parseData(statSheetName)

# create pyqt5 app
App = QApplication(sys.argv)

# initializing the stack
windowStack = QStackedWidget()
windowStack.setFixedHeight(800)
windowStack.setFixedWidth(1200)
windowStack.setWindowTitle("Programmed with <3 by Kyle James")

# initializing our windows, adding them to the stack, and mapping buttons
menuWindow = MenuWindow()
windowStack.addWidget(menuWindow)
menuWindow.newGameButton.clicked.connect(moveToSelectPlayers)

selectPlayersWindow = SelectPlayersWindow(playerList)
windowStack.addWidget(selectPlayersWindow)
selectPlayersWindow.startGameButton.clicked.connect(moveToRecordStats)
selectPlayersWindow.backButton.clicked.connect(moveToMenu)

recordStatsWindow = RecordStatsWindow()
windowStack.addWidget(recordStatsWindow)

gameRecapWindow = GameRecapWindow()
gameRecapWindow.returnToMenuButton.clicked.connect(moveToMenu)
windowStack.addWidget(gameRecapWindow)


# start the app
windowStack.show()
sys.exit(App.exec())
