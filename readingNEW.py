import os
from objectsNEW import Player, Game


def findNewestStatSheetName():
    """
    :return: a string of the newest stat sheet's name
    """

    # This code below is a simplified re-write of the function
    # unsure if this will work, so it'll need to be tested
    """
    statSheetList = os.listdir("stat_sheets")
    newestStatSheetNum = 0
    
    for sheet in statSheetList:
        if sheet[0].isnumeric():
            if int(sheet[0]) > newestStatSheetNum:
                newestStatSheetNum = int(sheet[0])
    
    return "stat_sheets/" + str(newestStatSheetNum) + "_stat_sheet.csv"
    """

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
    """
    :param statSheetName:
    :return: playerList, gameList, playerDict (keys: string of a player name & values: player object
    """

    statSheet = open(statSheetName)
    playerList = []
    gameList = []
    playerDict = dict()  # keys: string of a player name & value: player object

    # parsing the stat sheet
    for line in statSheet:
        line = line.split(',')

        # if the line is the header for players
        if line[0] == "\ufeffPlayerName":
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
            playerObj.gamesPlayed = line[1]
            playerObj.wins = line[2]
            playerObj.losses = line[3]
            playerObj.solids = line[4]
            playerObj.stripes = line[5]
            playerObj.winsByChoke = line[6]
            playerObj.lossesByChoke = line[7]
            playerObj.breaks = line[8]
            playerObj.ballsSunkOffBreak = line[9]
            playerObj.shotsTaken = line[10]
            playerObj.shotsMade = line[11]
            playerObj.shotsMissed = line[12]
            playerObj.bankShotsTaken = line[13]
            playerObj.bankShotsMade = line[14]
            playerObj.bankShotsMissed = line[15]
            playerObj.bridgeShotsTaken = line[16]
            playerObj.bridgeShotsMade = line[17]
            playerObj.bridgeShotsMissed = line[18]
            playerObj.behindTheBackShotsTaken = line[19]
            playerObj.behindTheBackShotsMade = line[20]
            playerObj.behindTheBackShotsMissed = line[21]
            playerObj.jumpShotsTaken = line[22]
            playerObj.jumpShotsMade = line[23]
            playerObj.jumpShotsMissed = line[24]
            playerObj.eightBallShotsTaken = line[25]
            playerObj.eightBallShotsMade = line[26]
            playerObj.eightBallShotsMissed = line[27]
            playerObj.opponentBallsSunk = line[28]
            playerObj.ballsSunkByOpponent = line[29]
            playerObj.scratchesMade = line[30]
            playerObj.opponentScratches = line[31]
            playerObj.ballsSunkInPocketA = line[32]
            playerObj.ballsSunkInPocketB = line[33]
            playerObj.ballsSunkInPocketC = line[34]
            playerObj.ballsSunkInPocketD = line[35]
            playerObj.ballsSunkInPocketE = line[36]
            playerObj.ballsSunkInPocketF = line[37]

            # appending the player to the player list and dictionary
            playerList.append(playerObj)
            playerDict[playerObj.playerName] = playerObj

        # this line is a game's stats
        elif line[0].isnumeric():
            # creating a game object for the game
            gameObj = Game()

            # filling the game object with the game's stats
            gameObj.gameNumber = line[0]
            gameObj.date = line[1]
            gameObj.BP = line[2]
            gameObj.IP = line[3]
            gameObj.BPBallGroup = line[4]
            gameObj.IPBallGroup = line[5]
            gameObj.winner = line[6]
            gameObj.loser = line[7]
            gameObj.gameWonByChoke = line[8]
            gameObj.ballsSunkOffBreak = line[9]
            gameObj.BPShotsTaken = line[10]
            gameObj.BPShotsMade = line[11]
            gameObj.BPShotsMissed = line[12]
            gameObj.BPBankShotsTaken = line[13]
            gameObj.BPBankShotsMade = line[14]
            gameObj.BPBankShotsMissed = line[15]
            gameObj.BPBridgeShotsTaken = line[16]
            gameObj.BPBridgeShotsMade = line[17]
            gameObj.BPBridgeShotsMissed = line[18]
            gameObj.BPBehindTheBackShotsTaken = line[19]
            gameObj.BPBehindTheBackShotsMade = line[20]
            gameObj.BPBehindTheBackShotsMissed = line[21]
            gameObj.BPJumpShotsTaken = line[22]
            gameObj.BPJumpShotsMade = line[23]
            gameObj.BPJumpShotsMissed = line[24]
            gameObj.BPEightBallShotsTaken = line[25]
            gameObj.BPEightBallShotsMade = line[26]
            gameObj.BPEightBallShotsMissed = line[27]
            gameObj.BPOpponentBallsSunk = line[28]
            gameObj.BPBallsSunkByOpponent = line[29]
            gameObj.BPScratchesMade = line[30]
            gameObj.BPOpponentScratches = line[31]
            gameObj.BPBallsSunkInPocketA = line[32]
            gameObj.BPBallsSunkInPocketB = line[33]
            gameObj.BPBallsSunkInPocketC = line[34]
            gameObj.BPBallsSunkInPocketD = line[35]
            gameObj.BPBallsSunkInPocketE = line[36]
            gameObj.BPBallsSunkInPocketF = line[37]
            gameObj.IPShotsTaken = line[38]
            gameObj.IPShotsMade = line[39]
            gameObj.IPShotsMissed = line[40]
            gameObj.IPBankShotsTaken = line[41]
            gameObj.IPBankShotsMade = line[42]
            gameObj.IPBankShotsMissed = line[43]
            gameObj.IPBridgeShotsTaken = line[44]
            gameObj.IPBridgeShotsMade = line[45]
            gameObj.IPBridgeShotsMissed = line[46]
            gameObj.IPBehindTheBackShotsTaken = line[47]
            gameObj.IPBehindTheBackShotsMade = line[48]
            gameObj.IPBehindTheBackShotsMissed = line[49]
            gameObj.IPJumpShotsTaken = line[50]
            gameObj.IPJumpShotsMade = line[51]
            gameObj.IPJumpShotsMissed = line[52]
            gameObj.IPEightBallShotsTaken = line[53]
            gameObj.IPEightBallShotsMade = line[54]
            gameObj.IPEightBallShotsMissed = line[55]
            gameObj.IPOpponentBallsSunk = line[56]
            gameObj.IPBallsSunkByOpponent = line[57]
            gameObj.IPScratchesMade = line[58]
            gameObj.IPOpponentScratches = line[59]
            gameObj.IPBallsSunkInPocketA = line[60]
            gameObj.IPBallsSunkInPocketB = line[61]
            gameObj.IPBallsSunkInPocketC = line[62]
            gameObj.IPBallsSunkInPocketD = line[63]
            gameObj.IPBallsSunkInPocketE = line[64]
            gameObj.IPBallsSunkInPocketF = line[65]

            # adding the game object to the game list
            gameList.append(gameObj)

    return playerList, gameList, playerDict
