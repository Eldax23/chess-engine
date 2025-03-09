"""
Responsible for containing the information the current state of the chess game.
and determining valid moves for the current state
"""

class GameState():
    def __init__(self):
        self.board = [
            ["bR" , "bN" , "bB" , "bQ" , "bK" , "bB" , "bN" , "bR"],
            ["bP" , "bP" , "bP" , "bP" , "bP" , "bP" , "bP" , "bP"],
            ["--" , "wP" , "--" , "--",  "--",  "--",  "--",  "--"],
            ["--" , "--" , "--" , "--",  "--",  "--",  "--",  "--"],
            ["--" , "--" , "--" , "--",  "--",  "--",  "--",  "--"],
            ["--" , "--" , "--" , "bP",  "--",  "--",  "--",  "--"],
            ["--" , "wP" , "wP" , "--" , "wP" , "wP" , "wP" , "wP"],
            ["wR" , "wN" , "wB" , "wQ" , "wK" , "wB" , "wN" , "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []
        self.piecesDic = {'P': self.getPawnMoves , 'R': self.getRookMoves , 'N': self.getKnightMoves
                         , 'B': self.getBishopMoves , 'Q': self.getQueenMoves , 'K': self.getKingMoves}
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
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                curr_sq = self.board[r][c]
                turn = curr_sq[0] # --> whether its w or b
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = curr_sq[1]
                    self.piecesDic[piece](r , c , moves)


        return moves

    # get all the moves of the pawn located at (r , c) and add it to moves list
    def getPawnMoves(self , r , c , moves):
        if self.whiteToMove:
            if self.board[r - 1][c] == "--": # 1 square pawn push
                moves.append(Move((r , c) , (r - 1 , c) , self.board))
                if r == 6 and self.board[r - 2][c] == "--": # 2 squares pawn push
                    moves.append(Move((r , c) , (r - 2 , c), self.board))

            if c - 1 >= 0: # capture the left piece
                 if self.board[r - 1][c - 1][0] == "b":
                     moves.append(Move((r , c) , (r - 1 , c - 1) , self.board))

            if c + 1 < len(self.board[r]): # capture the right piece
                 if self.board[r - 1][c + 1][0] == "b":
                     moves.append(Move((r , c) , (r - 1 , c + 1) , self.board))
        else:
            # pawn push forward.
            if r + 1 < 8 and self.board[r + 1][c] == "--":
                moves.append(Move((r , c) , (r + 1 , c) , self.board)) # 1 square
                if r == 1 and self.board[r + 2][c] == "--":
                    moves.append(Move((r , c) , (r + 2 , c) , self.board))

            # black pawn captures.
            if c + 1 <= 7 and r + 1 <= 7:
                # we capture the right white pawn
                if self.board[r + 1][c + 1][0] == "w":
                    moves.append(Move((r , c) , (r + 1 , c + 1), self.board))

            if c - 1 >= 0 and r + 1 < 8:
                # we capture left white pawn
                if self.board[r + 1][c - 1][0] == "w":
                    moves.append(Move((r , c) , (r + 1 , c - 1), self.board))






    # get all the moves of the rook located at (r , c) and add it to moves list
    def getRookMoves(self , r , c , moves):
        directions = ((-1 , 0) , (1 , 0) , (0 , -1) , (0 , 1)) # up - down - left - right
        enemyColor = "b" if self.whiteToMove else "w"
        print(f"moves before {moves}")
        for d in directions:
            for i in range(1 , 8):
                endRow = r + i * d[0]
                endCol = c + i * d[1]

                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    curr = self.board[endRow][endCol]
                    if curr == "--": # there is no piece to capture so we just move the rook.
                        moves.append(Move((r , c) , (endRow , endCol) , self.board))

                    elif curr[0] == enemyColor: # there is a piece of enemy to capture so we stop the possible moves in the diagonal.
                        moves.append(Move((r , c) , (endRow , endCol) , self.board))
                        break

                    else: # there is a piece of the same color , so we must stop the moves here too.
                        break
                else: # out of range indexes
                    break
        print(f"moves after: {moves}")




    # get all the moves of the Knight located at (r , c) and add it to moves list
    def getKnightMoves(self , r , c , moves):
        pass

    # get all the moves of the Bishop located at (r , c) and add it to moves list
    def getBishopMoves(self , r , c , moves):
        directions = ((-1 , -1) , (-1 , 1) , (1 , -1) , (1 , 1)) # we are moving diagonally so both (r , c) should change
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1 , 8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i

                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    curr = self.board[endRow][endCol]
                    if curr == "--":
                        moves.append(Move((r , c) , (endRow , endCol) , self.board))

                    elif curr[0] == enemyColor:
                        moves.append(Move((r , c) , (endRow , endCol) , self.board))
                        break
                    else:
                        break
                else:
                    break



    # get all the moves of the King located at (r , c) and add it to moves list
    def getKingMoves(self , r , c , moves):
        pass

    # get all the moves of the Queen located at (r , c) and add it to moves list
    def getQueenMoves(self , r , c , moves):
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
        self.moveId = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    def __eq__(self, other): # overriding eq function
        if isinstance(other , Move):
            return self.moveId == other.moveId
        return False


    def __str__(self):
        # return f"{self.startRow}{self.startCol} --> {self.endRow}{self.endCol}"
        return "foo"

    def getChessNotaion(self):
        return self.getRankFile(self.startRow , self.startCol) + " " +  self.getRankFile(self.endRow , self.endCol)




    def getRankFile(self , r , c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
