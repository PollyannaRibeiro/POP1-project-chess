from helpers import *
from board import Board

class King(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''

        current_x = self.pos_x
        current_y = self.pos_y
        current_side = self.side

        # check if there is a piece of the same side on the new position
        if is_piece_at(pos_X, pos_Y, B):
            piece_on_there = piece_at(pos_X, pos_Y, B)
            if current_side == piece_on_there.side:
                return False

        # check if the movement is possible
        if is_equal(current_x, pos_X) and abs(current_y - pos_Y) == 1 or abs(current_x - pos_X) == 1 and is_equal(
                current_y, pos_Y):
            return True
        elif abs(current_x - pos_X) == abs(current_y - pos_Y) == 1:
            return True
        else:
            return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

        if self.can_reach(pos_X, pos_Y, B):
            #  check if it is not overleaping any other piece
            if piece_at(pos_X, pos_Y, B):
                piece = piece_at(pos_X, pos_Y, B)
                if piece.side == self.side:
                    return False
                else:
                    return True
            else:
                return True
        return False

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''

        new_board: tuple[int, list[Piece]]

        if self.can_move_to(pos_X, pos_Y, B):
            board = B
            if piece_at(pos_X, pos_Y, B):
                piece_to_remove = piece_at(pos_X, pos_Y, B)
                board[1].remove(piece_to_remove)

            self.pos_x = pos_X
            self.pos_y = pos_Y
            new_board = board

            print(f"board - king --- {new_board}")
            return new_board