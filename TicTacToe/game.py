from Models.Board import Board
from Models.Player import Player
from Models.PlayingPiece import PlayingPieceX,PlayingPieceO

def main():
    m=int(input("Enter number of rows: "))
    n=int(input("Enter number of cols: "))
    
    print("Creating Board")
    try:
        board=Board(m,n)
    except Exception as e:
        print(e)
    
    playing_piece_x=PlayingPieceX()
    playing_piece_o=PlayingPieceO()
    
   
    player1=Player(playing_piece_x)
    player2=Player(playing_piece_o)
            

    print("Lets Start the Game")
    print(f"Player1: {player1.playing_piece.piece_type.value}, Player2: {player2.playing_piece.piece_type.value}")
    current_player=player1
    cnt=0
    while not board.check_winner():
        board.print_board()
        try:
            i,j=input(f"{current_player.playing_piece.piece_type.value}'s turn, \nEnter coordinates to place the piece (Ex: 1 1): ").split(" ")
            if not board.board[int(i)-1][int(j)-1]:
                current_player.place_piece(board,int(i)-1,int(j)-1)
            else:
                print("\nInvalid Input: Place is not empty\n")
                continue
        except IndexError:
            print("\nGiven coordinates are invalid\n")
            continue
        except Exception as e:
            print("\nInvalid values, Try Again\n")
            continue
            
        if current_player is player1:
            current_player=player2
        elif current_player is player2:
            current_player=player1
        cnt+=1
        
        if cnt==m*n:
            print("Game Ends with a Draw!!")
            break
    
    if cnt!=m*n:
        board.print_board()
        print(board.check_winner().value, "Wins!!")      
if __name__=="__main__":
    main()