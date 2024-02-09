
"""
board:
    ismate() => {true, false}
    isStalemate() => {true, false}
    isCheck() => {true, false}
    boardState
    print(self)
    movesNumber => int
    wichTurn => {white , black}
    isLegalMove(move) => {true, false}
    
"""
defaultBoard = [
     ["R", "N", "B", "Q", "K", "B", "N", "R"], 
     ["P", "P" ,"P", "P", "P", "P", "P", "P"], 
     [" ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " "],
     ["P", "P", "P", "P", "P", "P", "P", "P"],
     ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


class Board:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.__B = defaultBoard 
        

    def __str__(self):
        acc = ""
        for line in self.__B:
            for j in line:
                acc += f" {j}"
            acc += "\n"
        return acc

def main():
    board = Board(8)
    print(board)
main()
