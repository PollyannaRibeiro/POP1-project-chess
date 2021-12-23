from piece import Piece
from helpers import *
from board import Board


class Rook(Piece):

    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule2] and [Rule4](see section Intro)
        Hint: use is_piece_at
        '''
        current_x = self.pos_x
        current_y = self.pos_y
        current_side = self.side

        # check if there is a piece of the same side on the new position
        if is_piece_at(pos_X, pos_Y, B):
            piece_on_there = piece_at(pos_X, pos_Y, B)
            if current_side == piece_on_there.side:
                return False

        # check if the movement is possible
        if is_equal(current_x, pos_X) and not is_equal(current_y, pos_Y) or not is_equal(current_x, pos_X) and is_equal(
                current_y, pos_Y):
            return True
        else:
            return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to all chess rules

        Hints:
        - firstly, check [Rule2] and [Rule4] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule5], use is_check on new board
        '''

        if self.can_reach(pos_X, pos_Y, B):

            #  check if it is not overlapping any other piece
            piece_to_be_removed = None

            if is_equal(self.pos_x, pos_X):  # checking if the rook keep in the same row and move columns
                start: int = self.pos_y
                end: int = pos_Y
                counter: int = None

                #finding out if it's crescent or decrescent
                if start < end:
                    counter = 1
                else:
                    counter = -1

                start += counter

                while start != end:

                    if is_piece_at(pos_X, start, B):
                        return False
                    start += counter

                if start == end and is_piece_at(pos_X, end, B) is True:
                    piece_to_be_removed = piece_at(pos_X, end, B)

            else:  # checking if the rook keep in the same column and move rows
                start: int = self.pos_x
                end: int = pos_X
                counter: int = None

                # finding out if it's crescent or decrescent
                if start < end:
                    counter = 1
                else:
                    counter = -1

                start += counter

                while start != end:

                    if is_piece_at(start, pos_Y, B):
                        return False
                    start += 1

                if start == end and is_piece_at(end, pos_Y, B) == True:
                    piece_to_be_removed = piece_at(end, pos_Y, B)

            B[1].remove(piece_to_be_removed) # removing the competitor piece
            #placing the new position of the piece
            piece_to_be_altered = piece_at(self.pos_x, self.pos_y, B)
            piece_to_be_altered.pos_x = pos_X;
            piece_to_be_altered.pos_y = pos_Y;
            return True;
        else:
            return False

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''
        new_board: tuple[int, list[Piece]]

        if self.can_move_to(pos_X, pos_Y, B):
            self.pos_x = pos_X
            self.pos_y = pos_Y
            new_board = B

            print(f"board - rook --- {new_board}")
            return new_board
