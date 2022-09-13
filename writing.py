from reading import findNewestStatSheetName
import csv
import shutil


def writeNewCSV(playerList, gameList):
    curStatSheetName = findNewestStatSheetName()
    newStatSheetNum = '?'

    for i in range(len(curStatSheetName)):
        if curStatSheetName[i].isnumeric():
            newStatSheetNum = int(curStatSheetName[i]) + 1
            break

    newStatSheetName = str(newStatSheetNum) + "_stat_sheet.csv"

    playerHeaders = ['Player Name', 'Games played', 'Wins', 'Losses', 'Solids', 'Stripes', 'Choke wins', 'Choke losses',
                     'Faceoffs taken', 'Faceoff wins', 'Faceoff losses', 'Breaks', 'Balls sunk off break',
                     'Shots taken', 'Balls sunk', 'Shots missed', 'Balls sunk by opponent', 'Opponent balls sunk',
                     'Bank shots taken', 'Bank shots made', 'Bank shots missed', 'Aimbot shots taken',
                     'Aimbot shots made', 'Aimbot shots missed', 'Behind the back shots taken',
                     'Behind the back shots made', 'Behind the back shots missed', 'Jump shots taken',
                     'Jump shots made', 'Jump shots missed', 'Eight ball shots taken', 'Eight ball shots made',
                     'Eight ball shots missed', 'Balls sunk in pocket A', 'Balls sunk in pocket B',
                     'Balls sunk in pocket C', 'Balls sunk in pocket D', 'Balls sunk in pocket E',
                     'Balls sunk in pocket F', 'Most shots made in a turn', 'Scratches', 'Balls in hand',
                     'Balls off table', 'Redo turns', 'Redos taken', 'Most Redos']
    gameHeaders = ['Game #', 'Date', 'Home', 'Away', 'Winner', 'Game won by choke', 'Break', 'Balls sunk off break',
                   'Home ball type', 'Home shots taken', 'Home shots made', 'Home shots missed',
                   'Home opponent balls sunk', 'Home balls sunk by opponent', 'Home bank shots taken',
                   'Home bank shots made', 'Home bank shots missed', 'Home aimbot shots taken',
                   'Home aimbot shots made', 'Home aimbot shots missed', 'Home behind the back shots taken',
                   'Home behind the back shots made', 'Home behind the back shots missed', 'Home jump shots taken',
                   'Home jump shots made', 'Home jump shots missed', 'Home eight ball shots taken',
                   'Home eight ball shots made', 'Home eight ball shots missed', 'Home balls sunk in pocket A',
                   'Home balls sunk in pocket B', 'Home balls sunk in pocket C', 'Home balls sunk in pocket D',
                   'Home balls sunk in pocket E', 'Home balls sunk in pocket F', 'Home scratches', 'Home balls in hand',
                   'Home balls off table', 'Home chokes', 'Home redo turns', 'Home redos taken', 'Home most redos',
                   'Away ball type', 'Away shots taken', 'Away shots made', 'Away shots missed',
                   'Away opponent balls sunk', 'Away balls sunk by opponent', 'Away bank shots taken',
                   'Away bank shots made', 'Away bank shots missed', 'Away aimbot shots taken',
                   'Away aimbot shots made', 'Away aimbot shots missed', 'Away behind the back shots taken',
                   'Away behind the back shots made', 'Away behind the back shots missed', 'Away jump shots taken',
                   'Away jump shots made', 'Away jump shots missed', 'Away eight ball shots taken',
                   'Away eight ball shots made', 'Away eight ball shots missed', 'Away balls sunk in pocket A',
                   'Away balls sunk in pocket B', 'Away balls sunk in pocket C', 'Away balls sunk in pocket D',
                   'Away balls sunk in pocket E', 'Away balls sunk in pocket F', 'Away scratches', 'Away balls in hand',
                   'Away balls off table', 'Away chokes', 'Away redo turns', 'Away redos taken', 'Away most redos']

    with open(newStatSheetName, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(playerHeaders)

        # write player stats
        for player in playerList:
            playerVars = vars(player).values()
            writer.writerow(playerVars)

        writer.writerow(gameHeaders)

        # write game stats
        for game in gameList:
            gameVars = vars(game).values()
            writer.writerow(gameVars)

    return newStatSheetName
