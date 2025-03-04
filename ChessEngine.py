"""
Responsible for containing the information the current state of the chess game.
and determining valid moves for the current state
"""

class GameState():
    def __init__(self):
        self.board = [
            ["bR" , "bN" , "bB" , "bQ" , "bK" , "bB" , "bN" , "bR"],
            ["bP" , "bP" , "bP" , "bP" , "bP" , "bP" , "bP" , "bP"],
            ["--" , "--" , "--" , "--",  "--",  "--",  "--",  "--"],
            ["--" , "--" , "--" , "--",  "--",  "--",  "--",  "--"],
            ["--" , "--" , "--" , "--",  "--",  "--",  "--",  "--"],
            ["--" , "--" , "--" , "--",  "--",  "--",  "--",  "--"],
            ["wP" , "wP" , "wP" , "wP" , "wP" , "wP" , "wP" , "wP"],
            ["wR" , "wN" , "wB" , "wQ" , "wK" , "wB" , "wN" , "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []
    def makeMove(self , move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove


    # this will undo the last move made
    def undoMove(self):
        if len(self.moveLog) != 0: # check if there is a move to undo.
            last_move = self.moveLog.pop()
            self.board[last_move.endRow][last_move.endCol] = last_move.pieceCaptured
            self.board[last_move.startRow][last_move.startCol] = last_move.pieceMoved
            self.whiteToMove = not self.whiteToMove





class Move():
    ranksToRows = {"1": 7 , "2": 6 , "3": 5 , "4": 4, "5": 3 , "6": 2 , "7": 1 , "8": 0}

    rowsToRanks = {v : k for k , v in ranksToRows.items()}

    filesToCols = {"a": 0 , "b": 1 , "c": 2 , "d": 3 , "e": 4 , "f": 5 , "g": 6 , "h": 7}

    colsToFiles = {v : k for k , v in filesToCols.items()}


    def __init__(self , startSq , endSq , board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]


    def getChessNotaion(self):
        return self.getRankFile(self.startRow , self.startCol) + " " +  self.getRankFile(self.endRow , self.endCol)




    def getRankFile(self , r , c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
