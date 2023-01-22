from reading import findNewestStatSheetName
import csv
import shutil

# Testing: completed
# Integration: to be completed

# long lists which will be used in the writing functions
playerHeaders = ["Player Name", "Games Played", "Wins", "Losses", "Stripes", "Solids", "Wins by Choke",
                 "Losses by Choke", "Breaks", "Balls Sunk off Break", "Shots Taken", "Shots Made", "Shots Missed",
                 "Intentional Sinks", "Unintentional Sinks", "Bank Shots Taken", "Bank Shots Made", "Bank Shots Missed",
                 "Bridge Shots Taken", "Bridge Shots Made", "Bridge Shots Missed", "Behind the Back Shots Taken",
                 "Behind the Back Shots Made", "Behind the Back Shots Missed", "Jump Shots Taken", "Jump Shots Made",
                 "Jump Shots Missed", "8 Ball Shots Taken", "8 Ball Shots Made", "8 Ball Shots Missed",
                 "Opponent Balls Sunk", "Balls Sunk by Opponent", "Scratches Made", "Opponent Scratches",
                 "Balls Sunk in Pocket A", "Balls Sunk in Pocket B", "Balls Sunk in Pocket C", "Balls Sunk in Pocket D",
                 "Balls Sunk in Pocket E", "Balls Sunk in Pocket F"]

gameHeaders = ["Game Number", "Date", "BP", "IP", "Solids", "Stripes", "Winner", "Loser",
               "Game Won by Choke", "Balls Sunk off Break", "BP Shots Taken", "BP Shots Made", "BP Shots Missed",
               "BP Intentional Sinks", "BP Unintentional Sinks" "BP Bank Shots Taken", "BP Bank Shots Made",
               "BP Bank Shots Missed", "BP Bridge Shots Taken", "BP Bridge Shots Made", "BP Bridge Shots Missed",
               "BP Behind the Back Shots Taken", "BP Behind the Back Shots Made", "BP Behind the Back Shots Missed",
               "BP Jump Shots Taken", "BP Jump Shots Made", "BP Jump Shots Missed", "BP 8 Ball Shots Taken",
               "BP 8 Ball Shots Made", "BP 8 Ball Shots Missed", "BP Opponent Balls Sunk", "BP Balls Sunk by Opponent",
               "BP Scratches Made", "BP Opponent Scratches", "BP Balls Sunk in Pocket A", "BP Balls Sunk in Pocket B",
               "BP Balls Sunk in Pocket C", "BP Balls Sunk in Pocket D", "BP Balls Sunk in Pocket E",
               "BP  Balls Sunk in Pocket F", "IP Shots Taken", "IP Shots Made", "IP Shots Missed",
               "IP Intentional Sinks", "IP Unintentional Sinks" "IP Bank Shots Taken", "IP Bank Shots Made",
               "IP Bank Shots Missed", "IP Bridge Shots Taken", "IP Bridge Shots Made", "IP Bridge Shots Missed",
               "IP Behind the Back Shots Taken", "IP Behind the Back Shots Made", "IP Behind the Back Shots Missed",
               "IP Jump Shots Taken", "IP Jump Shots Made", "IP Jump Shots Missed", "IP 8 Ball Shots Taken",
               "IP 8 Ball Shots Made",  "IP 8 Ball Shots Missed", "IP Opponent Balls Sunk", "IP Balls Sunk by Opponent",
               "IP Scratches Made", "IP Opponent Scratches", "IP Balls Sunk in Pocket A", "IP Balls Sunk in Pocket B",
               "IP Balls Sunk in Pocket C", "IP Balls Sunk in Pocket D", "IP Balls Sunk in Pocket E",
               "IP  Balls Sunk in Pocket F"]


def writeNewCSV(playerList, gameList):
    # creating the name of the new stat sheet
    currStatSheetName = findNewestStatSheetName()
    newStatSheetNum = int(currStatSheetName[12]) + 1
    newStatSheetName = str(newStatSheetNum) + "_stat_sheet.csv"

    # writing stats to the file
    with open(newStatSheetName, 'w') as file:
        writer = csv.writer(file)

        # writing the player stats
        writer.writerow(playerHeaders)
        for player in playerList:
            playerVars = vars(player).values()
            writer.writerow(playerVars)

        # writing game stats
        writer.writerow(gameHeaders)
        for game in gameList:
            gameVars = vars(game).values()
            writer.writerow(gameVars)

    # moving the stat sheet to the proper directory
    shutil.move(newStatSheetName, "stat_sheets/")

    return newStatSheetName


def writeGameStatsToPlayers(game, breakingPlayerObj, incomingPlayerObj):
    # writing game stats
    breakingPlayerObj.gamesPlayed += 1
    incomingPlayerObj.gamesPlayed += 1
    breakingPlayerObj.breaks += 1
    breakingPlayerObj.ballsSunkOffBreak += game.ballsSunkOffBreak

    # updating winner and loser
    if game.winner == game.BP:
        breakingPlayerObj.wins += 1
        incomingPlayerObj.losses += 1
        if game.gameWonByChoke:
            breakingPlayerObj.winsByChoke += 1
            incomingPlayerObj.lossesByChoke += 1
    elif game.winner == game.IP:
        incomingPlayerObj.wins += 1
        breakingPlayerObj.losses += 1
        if game.gameWonByChoke:
            incomingPlayerObj.winsByChoke += 1
            breakingPlayerObj.lossesByChoke += 1

    # updating solids and stripes
    if game.solids == game.BP:
        breakingPlayerObj.solids += 1
        incomingPlayerObj.stripes += 1
    elif game.solids == game.IP:
        incomingPlayerObj.solids += 1
        breakingPlayerObj.stripes += 1

    # updating breaking player stats
    breakingPlayerObj.shotsTaken += game.BPShotsTaken
    breakingPlayerObj.shotsMade += game.BPShotsMade
    breakingPlayerObj.shotsMissed += game.BPShotsMissed
    breakingPlayerObj.intentionalSinks += game.BPIntentionalSinks
    breakingPlayerObj.unintentionalSinks += game.BPUnintentionalSinks
    breakingPlayerObj.bankShotsTaken += game.BPBankShotsTaken
    breakingPlayerObj.bankShotsMade += game.BPBankShotsMade
    breakingPlayerObj.bankShotsMissed += game.BPBankShotsMissed
    breakingPlayerObj.bridgeShotsTaken += game.BPBridgeShotsTaken
    breakingPlayerObj.bridgeShotsMade += game.BPBridgeShotsMade
    breakingPlayerObj.bridgeShotsMissed += game.BPBridgeShotsMissed
    breakingPlayerObj.behindTheBackShotsTaken += game.BPBehindTheBackShotsTaken
    breakingPlayerObj.behindTheBackShotsMade += game.BPBehindTheBackShotsMade
    breakingPlayerObj.behindTheBackShotsMissed += game.BPBehindTheBackShotsMissed
    breakingPlayerObj.jumpShotsTaken += game.BPJumpShotsTaken
    breakingPlayerObj.jumpShotsMade += game.BPJumpShotsMade
    breakingPlayerObj.jumpShotsMissed += game.BPJumpShotsMissed
    breakingPlayerObj.eightBallShotsTaken += game.BPEightBallShotsTaken
    breakingPlayerObj.eightBallShotsMade += game.BPEightBallShotsMade
    breakingPlayerObj.eightBallShotsMissed += game.BPEightBallShotsMissed
    breakingPlayerObj.opponentBallsSunk += game.BPOpponentBallsSunk
    breakingPlayerObj.ballsSunkByOpponent += game.BPBallsSunkByOpponent
    breakingPlayerObj.scratchesMade += game.BPScratchesMade
    breakingPlayerObj.opponentScratches += game.BPOpponentScratches
    breakingPlayerObj.ballsSunkInPocketA += game.BPBallsSunkInPocketA
    breakingPlayerObj.ballsSunkInPocketB += game.BPBallsSunkInPocketB
    breakingPlayerObj.ballsSunkInPocketC += game.BPBallsSunkInPocketC
    breakingPlayerObj.ballsSunkInPocketD += game.BPBallsSunkInPocketD
    breakingPlayerObj.ballsSunkInPocketE += game.BPBallsSunkInPocketE
    breakingPlayerObj.ballsSunkInPocketF += game.BPBallsSunkInPocketF

    incomingPlayerObj.shotsTaken += game.IPShotsTaken
    incomingPlayerObj.shotsMade += game.IPShotsMade
    incomingPlayerObj.shotsMissed += game.IPShotsMissed
    incomingPlayerObj.intentionalSinks += game.IPIntentionalSinks
    incomingPlayerObj.unintentionalSinks += game.IPUnintentionalSinks
    incomingPlayerObj.bankShotsTaken += game.IPBankShotsTaken
    incomingPlayerObj.bankShotsMade += game.IPBankShotsMade
    incomingPlayerObj.bankShotsMissed += game.IPBankShotsMissed
    incomingPlayerObj.bridgeShotsTaken += game.IPBridgeShotsTaken
    incomingPlayerObj.bridgeShotsMade += game.IPBridgeShotsMade
    incomingPlayerObj.bridgeShotsMissed += game.IPBridgeShotsMissed
    incomingPlayerObj.behindTheBackShotsTaken += game.IPBehindTheBackShotsTaken
    incomingPlayerObj.behindTheBackShotsMade += game.IPBehindTheBackShotsMade
    incomingPlayerObj.behindTheBackShotsMissed += game.IPBehindTheBackShotsMissed
    incomingPlayerObj.jumpShotsTaken += game.IPJumpShotsTaken
    incomingPlayerObj.jumpShotsMade += game.IPJumpShotsMade
    incomingPlayerObj.jumpShotsMissed += game.IPJumpShotsMissed
    incomingPlayerObj.eightBallShotsTaken += game.IPEightBallShotsTaken
    incomingPlayerObj.eightBallShotsMade += game.IPEightBallShotsMade
    incomingPlayerObj.eightBallShotsMissed += game.IPEightBallShotsMissed
    incomingPlayerObj.opponentBallsSunk += game.IPOpponentBallsSunk
    incomingPlayerObj.ballsSunkByOpponent += game.IPBallsSunkByOpponent
    incomingPlayerObj.scratchesMade += game.IPScratchesMade
    incomingPlayerObj.opponentScratches += game.IPOpponentScratches
    incomingPlayerObj.ballsSunkInPocketA += game.IPBallsSunkInPocketA
    incomingPlayerObj.ballsSunkInPocketB += game.IPBallsSunkInPocketB
    incomingPlayerObj.ballsSunkInPocketC += game.IPBallsSunkInPocketC
    incomingPlayerObj.ballsSunkInPocketD += game.IPBallsSunkInPocketD
    incomingPlayerObj.ballsSunkInPocketE += game.IPBallsSunkInPocketE
    incomingPlayerObj.ballsSunkInPocketF += game.IPBallsSunkInPocketF