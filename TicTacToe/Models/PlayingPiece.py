from abc import ABC,abstractmethod
from Enums.PieceType import PieceType

class PlayingPiece(ABC):
    def __init__(self,piece_type):
        self.piece_type=piece_type
        
        
class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
        
class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)