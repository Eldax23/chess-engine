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


    # Get All Valid Moves Considering Checks
    def getValidMoves(self):
        return self.getAllPossibleMoves() # for now we won't worry about checks


    # Get All Valid Moves NOT Considering Checks
    def getAllPossibleMoves(self):
        moves = [Move((6,4) , (4,4) , self.board)]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                curr_sq = self.board[r][c]
                turn = curr_sq[0] # --> whether its w or b
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = curr_sq[1]
                    if piece == 'p':
                        self.getPawnMoves(r , c , moves)
                    elif piece == 'R':
                        self.getRookMoves(r , c , moves)

        return moves

    # get all the moves of the pawn located at (r , c) and add it to moves list
    def getPawnMoves(self , r , c , moves):
        pass


    # get all the moves of the rook located at (r , c) and add it to moves list
    def getRookMoves(self , r , c , moves):
        pass









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
        self.moveId = self.startRow * 1000 + self.startCol  * 1000 + self.endRow * 1000 + self.startCol * 1000

    def __eq__(self, other): # overriding eq function
        if isinstance(other , Move):
            return self.moveId == other.moveId
        return False


    def getChessNotaion(self):
        return self.getRankFile(self.startRow , self.startCol) + " " +  self.getRankFile(self.endRow , self.endCol)




    def getRankFile(self , r , c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
