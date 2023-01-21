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
            playerObj.intentionalSinks = int(line[13])
            playerObj.unintentionalSinks = int(line[14])
            playerObj.bankShotsTaken = int(line[15])
            playerObj.bankShotsMade = int(line[16])
            playerObj.bankShotsMissed = int(line[17])
            playerObj.bridgeShotsTaken = int(line[18])
            playerObj.bridgeShotsMade = int(line[19])
            playerObj.bridgeShotsMissed = int(line[20])
            playerObj.behindTheBackShotsTaken = int(line[21])
            playerObj.behindTheBackShotsMade = int(line[22])
            playerObj.behindTheBackShotsMissed = int(line[23])
            playerObj.jumpShotsTaken = int(line[24])
            playerObj.jumpShotsMade = int(line[25])
            playerObj.jumpShotsMissed = int(line[26])
            playerObj.eightBallShotsTaken = int(line[27])
            playerObj.eightBallShotsMade = int(line[28])
            playerObj.eightBallShotsMissed = int(line[29])
            playerObj.opponentBallsSunk = int(line[30])
            playerObj.ballsSunkByOpponent = int(line[31])
            playerObj.scratchesMade = int(line[32])
            playerObj.opponentScratches = int(line[33])
            playerObj.ballsSunkInPocketA = int(line[34])
            playerObj.ballsSunkInPocketB = int(line[35])
            playerObj.ballsSunkInPocketC = int(line[36])
            playerObj.ballsSunkInPocketD = int(line[37])
            playerObj.ballsSunkInPocketE = int(line[38])
            playerObj.ballsSunkInPocketF = int(line[39])

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
            gameObj.BPIntentionalSinks = int(line[16])
            gameObj.BPUnintentionalSinks = int(line[17])
            gameObj.BPBridgeShotsTaken = int(line[18])
            gameObj.BPBridgeShotsMade = int(line[19])
            gameObj.BPBridgeShotsMissed = int(line[20])
            gameObj.BPBehindTheBackShotsTaken = int(line[21])
            gameObj.BPBehindTheBackShotsMade = int(line[22])
            gameObj.BPBehindTheBackShotsMissed = int(line[23])
            gameObj.BPJumpShotsTaken = int(line[24])
            gameObj.BPJumpShotsMade = int(line[25])
            gameObj.BPJumpShotsMissed = int(line[26])
            gameObj.BPEightBallShotsTaken = int(line[27])
            gameObj.BPEightBallShotsMade = int(line[28])
            gameObj.BPEightBallShotsMissed = int(line[29])
            gameObj.BPOpponentBallsSunk = int(line[30])
            gameObj.BPBallsSunkByOpponent = int(line[31])
            gameObj.BPScratchesMade = int(line[32])
            gameObj.BPOpponentScratches = int(line[33])
            gameObj.BPBallsSunkInPocketA = int(line[34])
            gameObj.BPBallsSunkInPocketB = int(line[35])
            gameObj.BPBallsSunkInPocketC = int(line[36])
            gameObj.BPBallsSunkInPocketD = int(line[37])
            gameObj.BPBallsSunkInPocketE = int(line[38])
            gameObj.BPBallsSunkInPocketF = int(line[39])
            gameObj.IPShotsTaken = int(line[40])
            gameObj.IPShotsMade = int(line[41])
            gameObj.IPShotsMissed = int(line[42])
            gameObj.IPIntentionalSinks = int(line[43])
            gameObj.IPUnintentionalSinks = int(line[44])
            gameObj.IPBankShotsTaken = int(line[45])
            gameObj.IPBankShotsMade = int(line[46])
            gameObj.IPBankShotsMissed = int(line[47])
            gameObj.IPBridgeShotsTaken = int(line[48])
            gameObj.IPBridgeShotsMade = int(line[49])
            gameObj.IPBridgeShotsMissed = int(line[50])
            gameObj.IPBehindTheBackShotsTaken = int(line[51])
            gameObj.IPBehindTheBackShotsMade = int(line[52])
            gameObj.IPBehindTheBackShotsMissed = int(line[53])
            gameObj.IPJumpShotsTaken = int(line[54])
            gameObj.IPJumpShotsMade = int(line[55])
            gameObj.IPJumpShotsMissed = int(line[56])
            gameObj.IPEightBallShotsTaken = int(line[57])
            gameObj.IPEightBallShotsMade = int(line[58])
            gameObj.IPEightBallShotsMissed = int(line[59])
            gameObj.IPOpponentBallsSunk = int(line[60])
            gameObj.IPBallsSunkByOpponent = int(line[61])
            gameObj.IPScratchesMade = int(line[62])
            gameObj.IPOpponentScratches = int(line[63])
            gameObj.IPBallsSunkInPocketA = int(line[64])
            gameObj.IPBallsSunkInPocketB = int(line[65])
            gameObj.IPBallsSunkInPocketC = int(line[66])
            gameObj.IPBallsSunkInPocketD = int(line[67])
            gameObj.IPBallsSunkInPocketE = int(line[68])
            gameObj.IPBallsSunkInPocketF = int(line[69])

            # adding the game object to the game list
            gameList.append(gameObj)

    return playerList, gameList, playerDict
