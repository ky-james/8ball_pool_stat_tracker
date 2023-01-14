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
        self.gameWonByChoke = None
        self.ballsSunkOffBreak = None

        # breaking player stats below
        self.BPShotsTaken = None
        self.BPShotsMade = None
        self.BPShotsMissed = None
        self.BPBankShotsTaken = None
        self.BPBankShotsMade = None
        self.BPBankShotsMissed = None
        self.BPBridgeShotsTaken = None
        self.BPBridgeShotsMade = None
        self.BPBridgeShotsMissed = None
        self.BPBehindTheBackShotsTaken = None
        self.BPBehindTheBackShotsMade = None
        self.BPBehindTheBackShotsMissed = None
        self.BPJumpShotsTaken = None
        self.BPJumpShotsMade = None
        self.BPJumpShotsMissed = None
        self.BPEightBallShotsTaken = None
        self.BPEightBallShotsMade = None
        self.BPEightBallShotsMissed = None
        self.BPOpponentBallsSunk = None
        self.BPBallsSunkByOpponent = None
        self.BPScratchesMade = None
        self.BPOpponentScratches = None
        self.BPBallsSunkInPocketA = None
        self.BPBallsSunkInPocketB = None
        self.BPBallsSunkInPocketC = None
        self.BPBallsSunkInPocketD = None
        self.BPBallsSunkInPocketE = None
        self.BPBallsSunkInPocketF = None

        # incoming player stats below
        self.IPShotsTaken = None
        self.IPShotsMade = None
        self.IPShotsMissed = None
        self.IPBankShotsTaken = None
        self.IPBankShotsMade = None
        self.IPBankShotsMissed = None
        self.IPBridgeShotsTaken = None
        self.IPBridgeShotsMade = None
        self.IPBridgeShotsMissed = None
        self.IPBehindTheBackShotsTaken = None
        self.IPBehindTheBackShotsMade = None
        self.IPBehindTheBackShotsMissed = None
        self.IPJumpShotsTaken = None
        self.IPJumpShotsMade = None
        self.IPJumpShotsMissed = None
        self.IPEightBallShotsTaken = None
        self.IPEightBallShotsMade = None
        self.IPEightBallShotsMissed = None
        self.IPOpponentBallsSunk = None
        self.IPBallsSunkByOpponent = None
        self.IPScratchesMade = None
        self.IPOpponentScratches = None
        self.IPBallsSunkInPocketA = None
        self.IPBallsSunkInPocketB = None
        self.IPBallsSunkInPocketC = None
        self.IPBallsSunkInPocketD = None
        self.IPBallsSunkInPocketE = None
        self.IPBallsSunkInPocketF = None