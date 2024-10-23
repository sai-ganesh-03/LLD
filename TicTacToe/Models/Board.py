from .PlayingPiece import PlayingPiece
from Enums.PieceType import PieceType
class Board:
    def __init__(self,m,n):
        if m != n :
            raise ValueError("Rows and Cols should be equal")
        self.board:list[list[PlayingPiece]]=[[None for _ in range(n)] for _ in range(m)]
        self.m=m
        self.n=n
        
        
    def print_board(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j]:
                    print(self.board[i][j].piece_type.value,end=" ")
                else:
                    print("-",end=" ")
            print("\n")
            
    def check_rows(self)->PieceType | None :
        for row in self.board:
            if all(ele == row[0] and ele is not None for ele in row):
                return row[0].piece_type
        return None    
        
    def check_cols(self)->PieceType | None:
        for i in range(self.m):
            if all(self.board[0][i]==self.board[j][i] and self.board[j][i] is not None for j in range(self.n)):
                return self.board[0][i].piece_type
        return False
    
    def check_diagonals(self)->PieceType | None:
        if all(self.board[0][0]==self.board[i][i] and self.board[i][i] is not None for i in range(self.m)):
            return self.board[0][0].piece_type
        elif all(self.board[0][self.n-1]==self.board[i][self.n-i-1] and self.board[i][self.n-i-1] is not None for i in range(self.m)):
            return self.board[0][self.n-1].piece_type
        return False
    
    def check_winner(self)->PieceType | None:
        return self.check_rows() or self.check_cols() or self.check_diagonals()