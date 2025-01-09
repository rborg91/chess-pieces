from chess_pieces import ChessPiece

chess_pieces = [
    ChessPiece("Pawn", "1-2", "forward", "straight (or diagnonal on certain circumstances)", "8"),
    ChessPiece("Castle", "any", "any", "straight", "2"),
    ChessPiece("Knight", "3", "any", "L-shape", "2"),
    ChessPiece("Bishop", "any", "any", "diagonal", "2"),
    ChessPiece("Queen", "any", "any", "straight", "1"),
    ChessPiece("King", "1", "any", "straight", "1"),
]

def main():
    for piece in chess_pieces:
        print(f"{piece.name}")
        print(f"Number of spaces that can move: {piece.obtain_moves()}")
        print(f"Direction of movement: {piece.obtain_direction()}")
        print(f"Shape of movement: {piece.shape}")
        print(f"Number of pieces on the board: {piece.obtain_count()}")
        print()

if __name__ == "__main__":
    main()