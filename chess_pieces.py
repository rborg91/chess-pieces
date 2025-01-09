class ChessPiece:
    # Attributes of chess pieces
    def __init__(self, name, moves, direction, shape, count):
        self.name = name
        self.moves = moves
        self.direction = direction
        self.shape = shape
        self.count = count

    # Methods to obtain info on chess pieces
    def obtain_moves(self):
        return self.moves
    
    def obtain_direction(self):
        return self.direction
    
    def obtain_count(self):
        return self.count