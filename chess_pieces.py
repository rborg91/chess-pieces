class ChessPiece:
    # Attributes of chess pieces
    def __init__(self, name, moves, direction, shape, count):
        self.name = name
        self.moves = moves
        self.direction = direction
        self.shape = shape
        self.count = count