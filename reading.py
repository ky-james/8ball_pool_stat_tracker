import os
from objects import Player, Game

# Testing: completed
# Integration: to be completed


def findNewestStatSheetName():
    statSheetList = os.listdir("stat_sheets")
    statSheetNum = 0

    for sheet in statSheetList:
        sheetNum = ""
        for i in range(len(sheet)):
            if sheet[i].isnumeric():
                sheetNum += sheet[i]
                if int(sheetNum) > statSheetNum:
                    statSheetNum = int(sheetNum)
            else:
                break

    statSheetName = str(statSheetNum) + "_stat_sheet.csv"

    return "stat_sheets/" + statSheetName


def parseData(statSheetName):

    statSheet = open(statSheetName)
    playerList = []
    gameList = []
    playerDict = dict()  # keys: string of a player name & value: player object

    # parsing the stat sheet
    for line in statSheet:
        line = line.split(',')

        # if the line is the header for players
        if line[0] == "Player Name":
            pass

        # if the line is the header for games
        elif line[0] == "Game Number":
            pass

        # the line is a player's stats
        elif not line[0].isnumeric():
            # creating a player object for the player
            playerObj = Player()

            # filling the player object with the player's stats
            playerObj.playerName = line[0]
            playerObj.gamesPlayed = int(line[1])
            playerObj.wins = int(line[2])
            playerObj.losses = int(line[3])
            playerObj.solids = int(line[4])
            playerObj.stripes = int(line[5])
            playerObj.winsByChoke = int(line[6])
            playerObj.lossesByChoke = int(line[7])
            playerObj.breaks = int(line[8])
            playerObj.ballsSunkOffBreak = int(line[9])
            playerObj.shotsTaken = int(line[10])
            playerObj.shotsMade = int(line[11])
            playerObj.shotsMissed = int(line[12])
            playerObj.bankShotsTaken = int(line[13])
            playerObj.bankShotsMade = int(line[14])
            playerObj.bankShotsMissed = int(line[15])
            playerObj.bridgeShotsTaken = int(line[16])
            playerObj.bridgeShotsMade = int(line[17])
            playerObj.bridgeShotsMissed = int(line[18])
            playerObj.behindTheBackShotsTaken = int(line[19])
            playerObj.behindTheBackShotsMade = int(line[20])
            playerObj.behindTheBackShotsMissed = int(line[21])
            playerObj.jumpShotsTaken = int(line[22])
            playerObj.jumpShotsMade = int(line[23])
            playerObj.jumpShotsMissed = int(line[24])
            playerObj.eightBallShotsTaken = int(line[25])
            playerObj.eightBallShotsMade = int(line[26])
            playerObj.eightBallShotsMissed = int(line[27])
            playerObj.opponentBallsSunk = int(line[28])
            playerObj.ballsSunkByOpponent = int(line[29])
            playerObj.scratchesMade = int(line[30])
            playerObj.opponentScratches = int(line[31])
            playerObj.ballsSunkInPocketA = int(line[32])
            playerObj.ballsSunkInPocketB = int(line[33])
            playerObj.ballsSunkInPocketC = int(line[34])
            playerObj.ballsSunkInPocketD = int(line[35])
            playerObj.ballsSunkInPocketE = int(line[36])
            playerObj.ballsSunkInPocketF = int(line[37])

            # appending the player to the player list and dictionary
            playerList.append(playerObj)
            playerDict[playerObj.playerName] = playerObj

        # this line is a game's stats
        elif line[0].isnumeric():
            # creating a game object for the game
            gameObj = Game()

            # filling the game object with the game's stats
            gameObj.gameNumber = int(line[0])
            gameObj.date = int(line[1])
            gameObj.BP = int(line[2])
            gameObj.IP = int(line[3])
            gameObj.solids = int(line[4])
            gameObj.stripes = int(line[5])
            gameObj.winner = int(line[6])
            gameObj.loser = int(line[7])
            gameObj.gameWonByChoke = int(line[8])
            gameObj.ballsSunkOffBreak = int(line[9])
            gameObj.BPShotsTaken = int(line[10])
            gameObj.BPShotsMade = int(line[11])
            gameObj.BPShotsMissed = int(line[12])
            gameObj.BPBankShotsTaken = int(line[13])
            gameObj.BPBankShotsMade = int(line[14])
            gameObj.BPBankShotsMissed = int(line[15])
            gameObj.BPBridgeShotsTaken = int(line[16])
            gameObj.BPBridgeShotsMade = int(line[17])
            gameObj.BPBridgeShotsMissed = int(line[18])
            gameObj.BPBehindTheBackShotsTaken = int(line[19])
            gameObj.BPBehindTheBackShotsMade = int(line[20])
            gameObj.BPBehindTheBackShotsMissed = int(line[21])
            gameObj.BPJumpShotsTaken = int(line[22])
            gameObj.BPJumpShotsMade = int(line[23])
            gameObj.BPJumpShotsMissed = int(line[24])
            gameObj.BPEightBallShotsTaken = int(line[25])
            gameObj.BPEightBallShotsMade = int(line[26])
            gameObj.BPEightBallShotsMissed = int(line[27])
            gameObj.BPOpponentBallsSunk = int(line[28])
            gameObj.BPBallsSunkByOpponent = int(line[29])
            gameObj.BPScratchesMade = int(line[30])
            gameObj.BPOpponentScratches = int(line[31])
            gameObj.BPBallsSunkInPocketA = int(line[32])
            gameObj.BPBallsSunkInPocketB = int(line[33])
            gameObj.BPBallsSunkInPocketC = int(line[34])
            gameObj.BPBallsSunkInPocketD = int(line[35])
            gameObj.BPBallsSunkInPocketE = int(line[36])
            gameObj.BPBallsSunkInPocketF = int(line[37])
            gameObj.IPShotsTaken = int(line[38])
            gameObj.IPShotsMade = int(line[39])
            gameObj.IPShotsMissed = int(line[40])
            gameObj.IPBankShotsTaken = int(line[41])
            gameObj.IPBankShotsMade = int(line[42])
            gameObj.IPBankShotsMissed = int(line[43])
            gameObj.IPBridgeShotsTaken = int(line[44])
            gameObj.IPBridgeShotsMade = int(line[45])
            gameObj.IPBridgeShotsMissed = int(line[46])
            gameObj.IPBehindTheBackShotsTaken = int(line[47])
            gameObj.IPBehindTheBackShotsMade = int(line[48])
            gameObj.IPBehindTheBackShotsMissed = int(line[49])
            gameObj.IPJumpShotsTaken = int(line[50])
            gameObj.IPJumpShotsMade = int(line[51])
            gameObj.IPJumpShotsMissed = int(line[52])
            gameObj.IPEightBallShotsTaken = int(line[53])
            gameObj.IPEightBallShotsMade = int(line[54])
            gameObj.IPEightBallShotsMissed = int(line[55])
            gameObj.IPOpponentBallsSunk = int(line[56])
            gameObj.IPBallsSunkByOpponent = int(line[57])
            gameObj.IPScratchesMade = int(line[58])
            gameObj.IPOpponentScratches = int(line[59])
            gameObj.IPBallsSunkInPocketA = int(line[60])
            gameObj.IPBallsSunkInPocketB = int(line[61])
            gameObj.IPBallsSunkInPocketC = int(line[62])
            gameObj.IPBallsSunkInPocketD = int(line[63])
            gameObj.IPBallsSunkInPocketE = int(line[64])
            gameObj.IPBallsSunkInPocketF = int(line[65])

            # adding the game object to the game list
            gameList.append(gameObj)

    return playerList, gameList, playerDict
