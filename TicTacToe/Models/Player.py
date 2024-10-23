from .PlayingPiece import PlayingPiece
from .Board import Board
class Player:
    def __init__(self,playing_piece:PlayingPiece):
        self.playing_piece=playing_piece
        
    def place_piece(self,board:Board,x:int,y:int):
        # print(f"Placing {self.playing_piece.piece_type.value} at {x},{y}")
        board.board[x][y]=self.playing_piece