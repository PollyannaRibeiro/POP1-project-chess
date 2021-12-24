from helpers import *
from board import Board

class Bishop(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''

        current_x = self.pos_x
        current_y = self.pos_y
        current_side = self.side

        # check if there is a piece of the same side on the new position
        if is_piece_at(pos_X, pos_Y, B):
            piece_on_there = piece_at(pos_X, pos_Y, B)
            if current_side == piece_on_there.side:
                return False

        # check if the movement is possible
        if abs(current_x - pos_X) == abs(current_y - pos_Y) and abs(current_x - pos_X) > 0:
            return True
        else:
            return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

        piece_to_be_removed = None

        if self.can_reach(pos_X, pos_Y, B):
            current_x = self.pos_x
            current_y = self.pos_y

            # find out the moves
            x_move = pos_X - current_x
            y_move = pos_Y - self.pos_y
            find_moves = x_move + y_move

            x_counter: int
            y_counter: int

            if find_moves > 0:
                x_counter = 1
                y_counter = 1

            elif find_moves < 0:
                x_counter = -1
                y_counter = -1
            else:
                if x_move > 0:
                    x_counter = 1
                    y_counter = -1
                else:
                    x_counter = -1
                    y_counter = 1

            while current_x != pos_X and current_y != pos_Y:
                current_x += x_counter
                current_y += y_counter
                if is_piece_at(current_x, current_y, B):
                    return False

            if current_x == pos_X and current_y == pos_Y and is_piece_at(current_x, current_y, B) is True:
                piece_to_be_removed = piece_at(current_x, current_y, B)

            if piece_to_be_removed is not None:
                B[1].remove(piece_to_be_removed)  # removing the competitor piece
            # placing the new position of the piece
            piece_to_be_altered = piece_at(self.pos_x, self.pos_y, B)
            piece_to_be_altered.pos_x = current_x;
            piece_to_be_altered.pos_y = current_y;
            return True
        else:
            return False


    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''

        new_board: tuple[int, list[Piece]]

        if self.can_move_to(pos_X, pos_Y, B):

            self.pos_x = pos_X
            self.pos_y = pos_Y
            new_board = B

            print(f"board - bishop --- {new_board}")
            return new_board
