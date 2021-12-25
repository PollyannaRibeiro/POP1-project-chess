from logic import Logic
from piece import *
from helpers import *


class KingMovement:

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''

        # check if there is a piece of the same side on the new position
        if is_piece_at(pos_X, pos_Y, B):
            piece_on_there = piece_at(pos_X, pos_Y, B)
            if self.side == piece_on_there.side:
                return False

        if (self.pos_x == pos_X or self.pos_x == pos_X + 1 or self.pos_x == pos_X -1) and \
                (self.pos_y == pos_Y or self.pos_y == pos_Y + 1 or self.pos_y == pos_Y - 1):
            return True
        else:
            return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

        if self.can_reach(pos_X, pos_Y, B):

            piece_to_be_removed = piece_at(pos_X, pos_Y, B)
            if piece_to_be_removed is not None:
                B[1].remove(piece_to_be_removed)  # removing the competitor piece
            # placing the new position of the piece
            piece_to_be_altered = piece_at(self.pos_x, self.pos_y, B)
            piece_to_be_altered.pos_x = pos_X;
            piece_to_be_altered.pos_y = pos_Y;
            return True;
        else:
            return False

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''

        new_board: tuple[int, list[Piece]]

        if self.can_move_to(pos_X, pos_Y, B):

            self.pos_x = pos_X
            self.pos_y = pos_Y
            new_board = B

            print(f"board - king --- {new_board}")
            return new_board