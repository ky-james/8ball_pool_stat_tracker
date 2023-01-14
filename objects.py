class Player:
    def __init__(self):
        # all individual player stats being tracked are below
        # the values will be changed from None during the file reading
        self.playerName = None
        self.gamesPlayed = None
        self.wins = None
        self.losses = None
        self.solids = None
        self.stripes = None
        self.winsByChoke = None
        self.lossesByChoke = None
        self.breaks = None
        self.ballsSunkOffBreak = None
        self.shotsTaken = None
        self.shotsMade = None
        self.shotsMissed = None
        self.bankShotsTaken = None
        self.bankShotsMade = None
        self.bankShotsMissed = None
        self.bridgeShotsTaken = None
        self.bridgeShotsMade = None
        self.bridgeShotsMissed = None
        self.behindTheBackShotsTaken = None
        self.behindTheBackShotsMade = None
        self.behindTheBackShotsMissed = None
        self.jumpShotsTaken = None
        self.jumpShotsMade = None
        self.jumpShotsMissed = None
        self.eightBallShotsTaken = None
        self.eightBallShotsMade = None
        self.eightBallShotsMissed = None
        self.opponentBallsSunk = None
        self.ballsSunkByOpponent = None
        self.scratchesMade = None
        self.opponentScratches = None
        self.ballsSunkInPocketA = None
        self.ballsSunkInPocketB = None
        self.ballsSunkInPocketC = None
        self.ballsSunkInPocketD = None
        self.ballsSunkInPocketE = None
        self.ballsSunkInPocketF = None


class Game:
    def __init__(self):
        # all game stats are below
        # values will be changed from None while the game is being played

        # game stats
        self.gameNumber = None
        self.date = None
        self.BP = None
        self.IP = None
        self.BPBallGroup = None
        self.IPBallGroup = None
        self.winner = None
        self.loser = None
        self.gameWonByChoke = False # will be set to true if needed
        self.ballsSunkOffBreak = None

        # breaking player stats below
        self.BPShotsTaken = 0
        self.BPShotsMade = 0
        self.BPShotsMissed = 0
        self.BPBankShotsTaken = 0
        self.BPBankShotsMade = 0
        self.BPBankShotsMissed = 0
        self.BPBridgeShotsTaken = 0
        self.BPBridgeShotsMade = 0
        self.BPBridgeShotsMissed = 0
        self.BPBehindTheBackShotsTaken = 0
        self.BPBehindTheBackShotsMade = 0
        self.BPBehindTheBackShotsMissed = 0
        self.BPJumpShotsTaken = 0
        self.BPJumpShotsMade = 0
        self.BPJumpShotsMissed = 0
        self.BPEightBallShotsTaken = 0
        self.BPEightBallShotsMade = 0
        self.BPEightBallShotsMissed = 0
        self.BPOpponentBallsSunk = 0
        self.BPBallsSunkByOpponent = 0
        self.BPScratchesMade = 0
        self.BPOpponentScratches = 0
        self.BPBallsSunkInPocketA = 0
        self.BPBallsSunkInPocketB = 0
        self.BPBallsSunkInPocketC = 0
        self.BPBallsSunkInPocketD = 0
        self.BPBallsSunkInPocketE = 0
        self.BPBallsSunkInPocketF = 0

        # incoming player stats below
        self.IPShotsTaken = 0
        self.IPShotsMade = 0
        self.IPShotsMissed = 0
        self.IPBankShotsTaken = 0
        self.IPBankShotsMade = 0
        self.IPBankShotsMissed = 0
        self.IPBridgeShotsTaken = 0
        self.IPBridgeShotsMade = 0
        self.IPBridgeShotsMissed = 0
        self.IPBehindTheBackShotsTaken = 0
        self.IPBehindTheBackShotsMade = 0
        self.IPBehindTheBackShotsMissed = 0
        self.IPJumpShotsTaken = 0
        self.IPJumpShotsMade = 0
        self.IPJumpShotsMissed = 0
        self.IPEightBallShotsTaken = 0
        self.IPEightBallShotsMade = 0
        self.IPEightBallShotsMissed = 0
        self.IPOpponentBallsSunk = 0
        self.IPBallsSunkByOpponent = 0
        self.IPScratchesMade = 0
        self.IPOpponentScratches = 0
        self.IPBallsSunkInPocketA = 0
        self.IPBallsSunkInPocketB = 0
        self.IPBallsSunkInPocketC = 0
        self.IPBallsSunkInPocketD = 0
        self.IPBallsSunkInPocketE = 0
        self.IPBallsSunkInPocketF = 0