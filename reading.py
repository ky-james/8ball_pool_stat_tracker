import os
from objects import Player, Game

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
    # contains keys of names and values of player objects
    playerDict = dict()

    for line in statSheet:
        line = line.split(',')

        # player headers 
        if line[0] == "\ufeffPlayer Name":
          pass

        # game headers 
        elif line[0] == "Game #":
            pass

        # player stats
        elif not line[0].isnumeric():
            playerObj = Player()
            playerObj.name = line[0]      
            playerObj.gamesPlayed = line[1]    
            playerObj.wins = line[2]      
            playerObj.losses = line[3]      
            playerObj.solids = line[4]      
            playerObj.stripes = line[5]      
            playerObj.chokeWins = line[6]      
            playerObj.chokeLosses = line[7]      
            playerObj.faceoffsTaken = line[8]      
            playerObj.faceoffWins = line[9]      
            playerObj.faceoffLosses = line[10]      
            playerObj.breaks = line[11]      
            playerObj.ballsSunkOffBreak = line[12]   
            playerObj.shotsTaken = line[13]   
            playerObj.shotsMade = line[14]      
            playerObj.shotsMissed = line[15]      
            playerObj.ballsSunkByOpponent = line[16]      
            playerObj.opponentBallsSunk = line[17]      
            playerObj.bankShotsTaken = line[18]      
            playerObj.bankShotsMade = line[19]      
            playerObj.bankShotsMissed = line[20]      
            playerObj.aimbotShotsTaken = line[21]    
            playerObj.aimbotShotsMade = line[22]      
            playerObj.aimbotShotsMissed = line[23]      
            playerObj.behindTheBackShotsTaken = line[24]      
            playerObj.behindTheBackShotsMade = line[25]      
            playerObj.behindTheBackshotsMissed = line[26]      
            playerObj.jumpShotsTaken = line[27]      
            playerObj.jumpShotsMade = line[28]      
            playerObj.jumpShotsMissed = line[29]      
            playerObj.eightBallShotsTaken = line[30]      
            playerObj.eightBallShotsMade = line[31]      
            playerObj.eightBallShotsMissed = line[32]   
            playerObj.ballsSunkInPocketA = line[33]
            playerObj.ballsSunkInPocketB = line[34]
            playerObj.ballsSunkInPocketC = line[35]
            playerObj.ballsSunkInPocketD = line[36]
            playerObj.ballsSunkInPocketE = line[37]
            playerObj.ballsSunkInPocketF = line[38]
            playerObj.mostShotsMadeInATurn = line[39] 
            playerObj.scratches = line[40]      
            playerObj.ballsInHand = line[41]      
            playerObj.ballsOffTable = line[42]      
            playerObj.redosTaken = line[43]    
            playerObj.redoTurns = line[44]  
            playerObj.mostRedos = line[45]     

            playerList.append(playerObj)   
            
        
        # game stats
        elif line[0].isnumeric():
            gameObj = Game()
            gameObj.gameNumber = line[0]
            gameObj.date = line[1]
            gameObj.home = line[2]
            gameObj.away = line[3]
            gameObj.winner = line[4]
            gameObj.gameWonByChoke = line[5]
            gameObj.broke = line[6]
            gameObj.ballsSunkOffBreak = line[7]
            gameObj.homeBallType = line[8]
            gameObj.homeShotsTaken = line[9]
            gameObj.homeShotsMade = line[10]
            gameObj.homeShotsMissed = line[11]
            gameObj.homeOpponentBallsSunk = line[12]
            gameObj.homeBallsSunkByOpponent = line[13]
            gameObj.homeBankShotstaken = line[14]
            gameObj.homeBankShotsMade = line[15]
            gameObj.homeBankShotsMissed = line[16]
            gameObj.homeAimbotShotsTaken = line[17]
            gameObj.homeAimbotShotsMade = line[18]
            gameObj.homeAimbotShotsMissed = line[19]
            gameObj.homeBehindTheBackShotsTaken = line[20]
            gameObj.homeBehindTheBackShotsMade = line[21]
            gameObj.homeBehindTheBackShotsMissed = line[22]
            gameObj.homeJumpShotsTaken = line[23]
            gameObj.homeJumpShotsMade = line[24]
            gameObj.homeJumpShotsMissed = line[25]
            gameObj.homeEightBallShotsTaken = line[26]
            gameObj.homeEightBallShotsMade = line[27]
            gameObj.homeEightBallShotsMissed = line[28]
            gameObj.homeBallsSunkInPocketA = line[29]
            gameObj.homeBallsSunkInPocketB = line[30]
            gameObj.homeBallsSunkInPocketC = line[31]
            gameObj.homeBallsSunkInPocketD = line[32]
            gameObj.homeBallsSunkInPocketE = line[33]
            gameObj.homeBallsSunkInPocketF = line[34]
            gameObj.homeScratches = line[35]
            gameObj.homeBallsInHand = line[36]
            gameObj.homeBallsOffTable = line[37]
            gameObj.homeChokes = line[38]
            gameObj.homeRedoTurns = line[39]
            gameObj.homeRedos = line[40]
            gameObj.homeMostRedos = line[41]

            gameObj.awayBallType = line[42]
            gameObj.awayShotsTaken = line[43]
            gameObj.awayShotsMade = line[44]
            gameObj.awayShotsMissed = line[45]
            gameObj.awayOpponentBallsSunk = line[45]
            gameObj.awayBallsSunkByOpponent = line[47]
            gameObj.awayBankShotstaken = line[48]
            gameObj.awayBankShotsMade = line[49]
            gameObj.awayBankShotsMissed = line[50]
            gameObj.awayAimbotShotsTaken = line[51]
            gameObj.awayAimbotShotsMade = line[52]
            gameObj.awayAimbotShotsMissed = line[53]
            gameObj.awayBehindTheBackShotsTaken = line[54]
            gameObj.awayBehindTheBackShotsMade = line[55]
            gameObj.awayBehindTheBackShotsMissed = line[56]
            gameObj.awayJumpShotsTaken = line[57]
            gameObj.awayJumpShotsMade = line[58]
            gameObj.awayJumpShotsMissed = line[59]
            gameObj.awayEightBallShotsTaken = line[60]
            gameObj.awayEightBallShotsMade = line[61]
            gameObj.awayEightBallShotsMissed = line[62]
            gameObj.awayBallsSunkInPocketA = line[63]
            gameObj.awayBallsSunkInPocketB = line[64]
            gameObj.awayBallsSunkInPocketC = line[65]
            gameObj.awayBallsSunkInPocketD = line[66]
            gameObj.awayBallsSunkInPocketE = line[67]
            gameObj.awayBallsSunkInPocketF = line[68]
            gameObj.awayScratches = line[69]
            gameObj.awayBallsInHand = line[70]
            gameObj.awayBallsOffTable = line[71]
            gameObj.awayChokes = line[72]
            gameObj.awayRedoTurns = line[73]
            gameObj.awayRedos = line[74]
            gameObj.awayMostRedos = line[75]

            gameList.append(gameObj)

    for player in playerList:
        playerDict[player.name] = player
    
    return playerList, gameList, playerDict
