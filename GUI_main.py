from datetime import date
from PyQt5.QtWidgets import *
import sys
from reading import findNewestStatSheetName
from reading import parseData
from writing import writeNewCSV
from menuWindow import MenuWindow
from selectPlayersWindow import SelectPlayersWindow
from recordStatsWindow import RecordStatsWindow
from gameRecapWindow import GameRecapWindow
from objects import Game, Player

# TODO:
# replace and integrate objectsNEW.py, readingNEW.py and writingNEW.py
# Things to consider while integrating:


# TODO after integration:
# change all variable names that include home and away, including both variables in this file and instance variables
# removing breaking checkbox in selectPlayersWindow
# change window text from home and away player to breaking and incoming


# variables
homePlayer = '?'
awayPlayer = '?'
selectedBall = '?'
selectedPocket = '?'
currentGame = "??"

# mapped buttons
def moveToSelectPlayers():
    windowStack.setCurrentIndex(1)


def moveToMenu():
    windowStack.setCurrentIndex(0)


def moveToRecordStats():

    # checking that two players are not playing themselves
    if selectPlayersWindow.homeComboBox.currentText() != selectPlayersWindow.awayComboBox.currentText():

        # move to record stats window and update recordStatsWindow's instance variables
        windowStack.setCurrentIndex(2)
        # TODO: home and away combo boxes will no longer exist, must change their variable names
        recordStatsWindow.homePlayerLabel.setText(selectPlayersWindow.homeComboBox.currentText())
        recordStatsWindow.awayPlayerLabel.setText(selectPlayersWindow.awayComboBox.currentText())

        # START: remove after integration as breaking player will already be known
        if selectPlayersWindow.breakCheckBox.isChecked():
            breakingPlayer = 'home'
            recordStatsWindow.homeTurn = True

        else:
            breakingPlayer = 'away'
            recordStatsWindow.homeTurn = False
            recordStatsWindow.shootingIcon.move(recordStatsWindow.shootingIconCoordinateDict['away'][0],
                                                recordStatsWindow.shootingIconCoordinateDict['away'][1])
        # END: remove after integration as breaking player will already be known

        # TODO: change variable names as home and away players no longer exist
        homePlayer = playerDict[selectPlayersWindow.homeComboBox.currentText()]
        awayPlayer = playerDict[selectPlayersWindow.awayComboBox.currentText()]
        recordStatsWindow.homePlayer = homePlayer
        recordStatsWindow.awayPlayer = awayPlayer
        recordStatsWindow.breakingPlayer = breakingPlayer

        # creating a new object for the current game
        # TODO: change variable names as home and away players no longer exist
        currentGame = Game()
        currentGame.gameNumber = len(gameList)
        currentGame.home = homePlayer.name
        currentGame.away = awayPlayer.name
        currentGame.date = date.today()
        currentGame.broke = breakingPlayer

        # resetting the turn and sink logs for a new game:
        recordStatsWindow.turnLog = []
        recordStatsWindow.sinkLog = []

        # resetting ballsOnTable list for a new game
        recordStatsWindow.ballsOnTable = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                                          '15']

    else:
        print("\nUnable to start a new game, two players are currently playing themselves.")
        print("To start a game, please select two unique players.")


def moveToGameRecap():
    windowStack.setCurrentIndex(3)
    currentGame = "?"

# reading data
statSheetName = findNewestStatSheetName()
playerList, gameList, playerDict = parseData(statSheetName)

# create pyqt5 app
App = QApplication(sys.argv)

# initializing the stack
windowStack = QStackedWidget()
windowStack.setFixedHeight(800)
windowStack.setFixedWidth(1200)

# initializing our windows, adding them to the stack, and mapping buttons
menuWindow = MenuWindow()
windowStack.addWidget(menuWindow)
menuWindow.newGameButton.clicked.connect(moveToSelectPlayers)

selectPlayersWindow = SelectPlayersWindow(playerList)
windowStack.addWidget(selectPlayersWindow)
selectPlayersWindow.startGameButton.clicked.connect(moveToRecordStats)
selectPlayersWindow.backButton.clicked.connect(moveToMenu)

recordStatsWindow = RecordStatsWindow(windowStack)
windowStack.addWidget(recordStatsWindow)

gameRecapWindow = GameRecapWindow()
gameRecapWindow.returnToMenuButton.clicked.connect(moveToMenu)
windowStack.addWidget(gameRecapWindow)

# TODO: remove the line of code below
# windowStack.setCurrentIndex(3)

# start the app
windowStack.show()
sys.exit(App.exec())
