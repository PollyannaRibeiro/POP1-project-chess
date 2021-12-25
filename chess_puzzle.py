import random

from piece import Piece
from random import *
from helpers import *


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


        # ????????????????????????????????????

        #  check if it is not overlapping any other piece
        piece_to_be_removed = None

        if is_equal(self.pos_x, pos_X):  # checking if the rook keep in the same row and move columns
            start: int = self.pos_y
            end: int = pos_Y
            counter: int = None

            # finding out if it's crescent or decrescent
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

            if start == end and is_piece_at(end, pos_Y, B) is True:
                piece_to_be_removed = piece_at(end, pos_Y, B)


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

                if start == end and is_piece_at(end, pos_Y, B) is True:
                    piece_to_be_removed = piece_at(end, pos_Y, B)

            if piece_to_be_removed is not None:
                B[1].remove(piece_to_be_removed) # removing the competitor piece
            #placing the new position of the piece
            piece_to_be_altered = piece_at(self.pos_x, self.pos_y, B)
            piece_to_be_altered.pos_x = pos_X;
            piece_to_be_altered.pos_y = pos_Y;

            if is_check(piece_to_be_altered.side, B):
                return False

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


class King(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

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


class Helper:
    @staticmethod
    def is_type(piece: Piece, type_of) -> bool:
        return type(piece) == type_of

    @staticmethod
    def is_not_type(piece: Piece, type_of) -> bool:
        return type(piece) != type_of

    @staticmethod
    def checkmate_info(side: bool, B: Board) -> tuple[bool, list[int, int], list[type, int, int, bool]]:

        move_to_save_from_checkmate = None
        piece_to_move_to_avoid_checkmate = None

        checkmate_cant_be_avoid = None

        board = B[1]
        is_check_possible: bool = is_check(side, B)

        king_in_check = None
        checkmate_pieces_options = list()

        if is_check_possible:
            # finding which pieces are putting the king in check
            for piece in board:
                if Helper.is_type(piece, King) and piece.side == side:
                    king_in_check = King(piece.pos_x, piece.pos_y, piece.side)
                if piece.side != side:
                    # king = King(king_in_check.pos_x, king_in_check.pos_y, king_in_check.side)

                    if Helper.is_type(piece, Rook):
                        rook = Rook(piece.pos_x, piece.pos_y, piece.side)
                        if rook.can_reach(king_in_check.pos_x, king_in_check.pos_y, B):
                            checkmate_pieces_options.append(rook)
                    elif Helper.is_type(piece, Bishop):
                        bishop = Bishop(piece.pos_x, piece.pos_y, piece.side)
                        if bishop.can_reach(king_in_check.pos_x, king_in_check.pos_y, B):
                            checkmate_pieces_options.append(bishop)
                    elif Helper.is_type(piece, King):
                        king_opposite = King(piece.pos_x, piece.pos_y, piece.side)
                        if king_opposite.can_reach(king_in_check.pos_x, king_in_check.pos_y, B):
                            checkmate_pieces_options.append(king_opposite)

            for piece in board:

                # king can run away?

                king = king_in_check

                all_King_moves_options = [[king.pos_x, king.pos_y + 1], [king.pos_x, king.pos_y - 1],
                                          [king.pos_x + 1, king.pos_y],
                                          [king.pos_x - 1, king.pos_y], [king.pos_x + 1, king.pos_y + 1],
                                          [king.pos_x - 1, king.pos_y - 1],
                                          [king.pos_x + 1, king.pos_y - 1], [king.pos_x - 1, king.pos_y + 1]]

                for index in range(0, len(all_King_moves_options) - 1):
                    king_moves = all_King_moves_options[index][0], all_King_moves_options[index][1]
                    can_walk = king.can_reach(king_moves[0], king_moves[1], B)
                    if can_walk:
                        new_board = king.move_to(king_moves[0], king_moves[1], B)
                        if (Helper.is_check(king.side, new_board)):
                            continue
                        else:
                            print("is not checkmate")
                            move_to_save_from_checkmate = [King, king_moves[0], king_moves[1], king.side]
                            checkmate_cant_be_avoid = False

                if Helper.is_not_type(piece, King) and piece.side == side:
                    rook = None
                    bishop = None

                    if Helper.is_type(piece, Rook):
                        rook = Rook(piece.pos_x, piece.pos_y, piece.side)
                    elif Helper.is_type(piece, Bishop):
                        bishop = Bishop(piece.pos_x, piece.pos_y, piece.side)

                    if (len(checkmate_pieces_options) == 1):
                        type_of = type(checkmate_pieces_options[0])
                        path_to_king = list()

                        opp_piece = checkmate_pieces_options[0]
                        x = king.pos_x
                        y = king.pos_y
                        x2 = checkmate_pieces_options[0].pos_x
                        y2 = checkmate_pieces_options[0].pos_y

                        if rook is not None and rook.can_reach(x2, y2, B):
                            move_to_save_from_checkmate = [Bishop, x2, y2, king.side]
                            return False
                        if bishop is not None and bishop.can_reach(x2, y2, B):
                            move_to_save_from_checkmate = [Bishop, x2, y2, king.side]
                            return False

                        # torre com a mesma row
                        if Helper.is_type(opp_piece, Rook):
                            if x2 == x:
                                while y2 != y:
                                    path_to_king.append([x2, y2])
                                    if y2 < y:
                                        y2 += 1
                                    else:
                                        y2 -= 1

                            # torre com a mesma col
                            if y2 == y:
                                while x2 != x:
                                    path_to_king.append([x2, y2])
                                    if x2 < x:
                                        x2 += 1
                                    else:
                                        x2 -= 1

                        elif Helper.is_type(opp_piece, Bishop):

                            while x2 < x:
                                if y2 < y:
                                    path_to_king.append([x2, y2])
                                    x2 += 1
                                    y2 += 1

                                if y2 > y:
                                    path_to_king.append([x2, y2])
                                    x2 += 1
                                    y2 -= 1

                            while x2 > x:
                                path_to_king.append([x2, y2])
                                if y2 < y:
                                    x2 -= 1
                                    y2 += 1
                                if y2 > y:
                                    x2 -= 1
                                    y2 -= 1
                        elif Helper.is_type(opp_piece, King):
                            # rook moves
                            if x2 == x:
                                while y2 != y:
                                    path_to_king.append([x2, y2])
                                    if y2 < y:
                                        y2 += 1
                                    else:
                                        y2 -= 1

                            if y2 == y:
                                while x2 != x:
                                    path_to_king.append([x2, y2])
                                    if x2 < x:
                                        x2 += 1
                                    else:
                                        x2 -= 1

                            # bishop moves
                            while x2 < x:
                                if y2 < y:
                                    path_to_king.append([x2, y2])
                                    x2 += 1
                                    y2 += 1

                                if y2 > y:
                                    path_to_king.append([x2, y2])
                                    x2 += 1
                                    y2 -= 1

                            while x2 > x:
                                path_to_king.append([x2, y2])
                                if y2 < y:
                                    x2 -= 1
                                    y2 += 1
                                if y2 > y:
                                    x2 -= 1
                                    y2 -= 1

                        new_board = B

                        for path in path_to_king:

                            if rook is not None and rook.can_reach(path[0], path[1], B):
                                rook.move_to(path[0], path[1], new_board)
                                if Helper.is_check(rook.side):
                                    new_board = B
                                    continue
                                else:
                                    move_to_save_from_checkmate = [path[0], path[1]]
                                    piece_to_move_to_avoid_checkmate = [Rook, rook.pos_x, rook.pos_y, rook.side]
                                checkmate_cant_be_avoid = False
                            if bishop is not None and bishop.can_reach(path[0], path[1], B):
                                bishop.move_to(path[0], path[1], new_board)
                                if Helper.is_check(bishop.side):
                                    new_board = B
                                    continue
                                else:
                                    move_to_save_from_checkmate = [path[0], path[1]]
                                    piece_to_move_to_avoid_checkmate = [Bishop, bishop.pos_x, bishop.pos_y, bishop.side]
                                checkmate_cant_be_avoid = False

                    elif len(checkmate_pieces_options) > 1:
                        checkmate_cant_be_avoid = True
            checkmate_cant_be_avoid = True

        else:
            checkmate_cant_be_avoid = False

        return checkmate_cant_be_avoid, move_to_save_from_checkmate, piece_to_move_to_avoid_checkmate


# find type
def type_of_piece(piece, option_rook, option_bishop, option_king):

    if type(piece) == Rook:
        return option_rook
    elif type(piece) == Bishop:
        return option_bishop
    elif type(piece) == King:
        return option_king
    else:
        print("error on the piece sent")

# variables for is_check and is_checkmate and

# king_in_check = None
# checkmate_pieces_options = list()

def is_check(side: bool, B: Board) -> bool:
    is_reachable = False

    board = B[1]
    for piece in board:

        if Helper.is_type(piece, King) and piece.side == side:
            for piece2 in board:
                if piece2.side != side:
                    if Helper.is_type(piece2, Rook):
                        rook = Rook(piece2.pos_x, piece2.pos_y, piece2.side)
                        if (rook.can_reach(piece.pos_x, piece.pos_y, B)):
                            is_reachable = True
                            print("it's check")

                    elif Helper.is_type(piece2, Bishop):
                        bishop = Bishop(piece2.pos_x, piece2.pos_y, piece2.side)
                        if (bishop.can_reach(piece.pos_x, piece.pos_y, B)):
                            is_reachable = True
                            print("it's check")

                    elif Helper.is_type(piece2, King):
                        king = King(piece2.pos_x, piece2.pos_y, piece2.side)
                        if (king.can_reach(piece.pos_x, piece.pos_y, B)):
                            is_reachable = True
                            print("it's check")

                    if is_reachable:
                        return True;
    return False

# def is_check(side: bool, B: Board) -> bool:
#     '''
#     checks if configuration of B is check for side
#     Hint: use can_reach
#     '''
#
#     is_reachable = False
#
#     board = B[1]
#     for piece in board:
#
#         if is_type(piece, King) and piece.side == side:
#             for piece2 in board:
#                 if piece2.side != side:
#                     if is_type(piece2, Rook):
#                         rook = Rook(piece2.pos_x, piece2.pos_y, piece2.side)
#                         if(rook.can_reach(piece.pos_x, piece.pos_y, B)):
#                             is_reachable = True
#                             print("it's check")
#
#                     elif is_type(piece2, Bishop):
#                         bishop = Bishop(piece2.pos_x, piece2.pos_y, piece2.side)
#                         if (bishop.can_reach(piece.pos_x, piece.pos_y, B)):
#                             is_reachable = True
#                             print("it's check")
#
#                     elif is_type(piece2, King):
#                         king = King(piece2.pos_x, piece2.pos_y, piece2.side)
#                         if (king.can_reach(piece.pos_x, piece.pos_y, B)):
#                             is_reachable = True
#                             print("it's check")
#
#                     if is_reachable:
#                         return True;
#     return False


# variables importants to is checkmate and find_black_move







def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_reach 
    '''

    info = Helper.checkmate_info(side, B)
    return info[0]

def get_piece_risk_checkmate_position(king_X, king_Y, type_of ,x, y, side, x2, y2, B: Board):
    king = King(king_X, king_Y, side)

    if type_of is Rook:
        rook = Rook(x, y, side)
    elif type_of is Bishop:
        bishop = Bishop(x, y, side)

    if rook.can_reach(x2, y2, B):
        next_move = [rook.pos_x, rook.pos_y, rook.side], [x2, y2]




def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''

    try:
        f = open(filename, "r")
        line1 = int(f.readline())   #size

        line2 = f.readline()       #white

        white_pieces_list = line2.replace("\n", "").split(", ")
        line3 = f.readline()       #black

        black_pieces_list = line3.replace("\n", "").split(", ")
        pieces_list = list()
        side_list = [white_pieces_list, black_pieces_list]
        print(side_list)

        # variables
        piece_obj = None

        for i in range(0, len(side_list)):
            for j in range(0, len(side_list[i])):
                piece = side_list[i][j]
                positions: tuple[int, int] = location2index(piece[1:])
                pos_x: int = positions[0]
                pos_y: int = positions[1]

                side = False
                if i == 0:
                    side = True

                if piece[0] == "B":
                    piece_obj = Bishop(pos_x, pos_y, side)
                elif piece[0] == "R":
                    piece_obj = Rook(pos_x, pos_y, side)
                elif piece[0] == "K":
                    piece_obj = King(pos_x, pos_y, side)
                else:
                    print("IO error")

                pieces_list.append(piece_obj)

        return line1, pieces_list
    except IOError:
        print("Oops! It's not possible to read this file")
        raise


def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''

    try:

        size = B[0]
        pieces_list = B[1]
        white_pieces_str = ""
        black_pieces_str = ""

        for i in range(0, len(pieces_list)):
            piece = pieces_list[i]
            piece_str = index2location(piece.pos_x, piece.pos_y)
            piece_type = None

            if type(piece) == Rook:
                piece_type = "R"
            elif type(piece) == Bishop:
                piece_type = "B"
            elif type(piece) == King:
                piece_type = "K"

            if piece.side is True:
                white_pieces_str += piece_type + piece_str + ", "
            else:
                black_pieces_str += piece_type + piece_str + ", "

        white_pieces_str = white_pieces_str[:-2]        # removing the last 2 char
        black_pieces_str = black_pieces_str[:-2]        # removing the last 2 char


        f = open(filename, "w")

        f.write(str(size) + "\n")
        f.write(white_pieces_str + "\n")
        f.write(black_pieces_str + "\n")
        f.close()

    except IOError:
        print("Error while writing")


def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''


    size = B[0]
    piece_list = B[1]
    black_elem_list = list()
    white_elem_list = list()

    can_reach_enemy = list()

    check_info = Helper.checkmate_info()
    move_to_save_from_checkmate = check_info[1]
    piece_to_move_to_avoid_checkmate = check_info[2]



    check_risk = is_check(False, B)

    if check_risk:

        #  to update move_to_save_from_checkmate and piece_to_move_to_avoid_checkmate
        is_checkmate(False, B)

        if piece_to_move_to_avoid_checkmate and move_to_save_from_checkmate:
            return move_to_save_from_checkmate[0], move_to_save_from_checkmate[1], move_to_save_from_checkmate[2]

    else:
        rook = None
        bishop = None
        king = None

        for piece in piece_list:
            if piece.side is False:
                black_elem_list.append(piece)
            else:
                white_elem_list.append(piece)

        for piece in black_elem_list:
            for piece2 in white_elem_list:

                if Helper.is_type(piece, Rook):
                    rook = Rook(piece.pos_x, piece.pos_y, piece.side)
                    if rook.can_reach(piece2.pos_x, piece2.pos_y, B):
                        can_reach_enemy.append(piece2)

                elif Helper.is_type(piece, Bishop):
                    bishop = Bishop(piece.pos_x, piece.pos_y, piece.side)
                    if bishop.can_reach(piece2.pos_x, piece2.pos_y, B):
                        can_reach_enemy.append(piece2)

                elif Helper.is_type(piece, King):
                    king = King(piece.pos_x, piece.pos_y, piece.side)
                    if king.can_reach(piece2.pos_x, piece2.pos_y, B):
                        can_reach_enemy.append(piece2)

        if len(can_reach_enemy) == 1:

            if rook is not None:
                return rook, can_reach_enemy[0][0], can_reach_enemy[0][1]
            elif bishop is not None:
                return bishop, can_reach_enemy[0][0], can_reach_enemy[0][1]
            elif King is not None:
                return king, can_reach_enemy[0][0], can_reach_enemy[0][1]

        elif len(can_reach_enemy) > 1:
            index = random.randrange(0, len(can_reach_enemy)-1)

            if rook is not None:
                return rook, can_reach_enemy[index][0], can_reach_enemy[index][1]
            elif bishop is not None:
                return bishop, can_reach_enemy[index][0], can_reach_enemy[index][1]
            elif King is not None:
                return king, can_reach_enemy[index][0], can_reach_enemy[index][1]

        else:

            while True:

                pos_x = random.randrange(1, size)
                pos_y = random.randrange(1, size)

                for piece in black_elem_list:

                    if Helper.is_type(piece, Rook):
                        rook = Rook(piece.pos_x, piece.pos_y, piece.side)
                        if rook.can_reach(pos_x, pos_y, B):

                            return rook, pos_x, pos_y

                    elif Helper.is_type(piece, Bishop):
                        bishop = Bishop(piece.pos_x, piece.pos_y, piece.side)
                        if bishop.can_reach(pos_x, pos_y, B):
                            return bishop, pos_x, pos_y

                    elif Helper.is_type(piece, King):
                        king = King(piece.pos_x, piece.pos_y, piece.side)
                        if king.can_reach(pos_x, pos_y, B):
                            return king, pos_x, pos_y


def conf2unicode(B: Board) -> str:
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''

    size = B[0]
    pieces_list = B[1]

    new_list = list()
    mini_list = list()

    # creating the matrix

    for i in range(0, size):
        mini_list = list()
        for j in range(0, size):
            mini_list.append(" ")
        new_list.append(mini_list);

    # insert unicodes

    for piece in pieces_list:

        pos_x: int = piece.pos_x-1
        pos_y: int = piece.pos_y-1
        side: bool = piece.side
        type: str = None

        if side:
            type = type_of_piece(piece, "♖", "♗", "♔")
        else:
            type = type_of_piece(piece, "♜", "♝", "♚")

        if type is not None:
            new_list[pos_x][pos_y] = type

    list_to_print = ""
    for i in reversed(range(0, size)):
        for j in range(0, size):
            list_to_print += new_list[j][i]
        list_to_print += "\n"

    return list_to_print[:-1]


def execute(filename) -> bool:
    try:
        board = read_board(filename)
        print("The initial configuration is:")
        print(conf2unicode(board))

        return True
    except IOError:
        print("This is not a valid file. File name for initial configuration: ")
        return False


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''

    print("File name for initial configuration:")

    # requires_input = True
    # while requires_input:
    #     filename = input()
    #     if filename == "QUIT":
    #         return
    #     requires_input = not execute(filename)


    execute("board_examp.txt")


if __name__ == '__main__':  # keep this in
    main()

# wb1 = Bishop(1, 1, True)
# wr1 = Rook(1, 2, True)
# wb2 = Bishop(5, 2, True)
# bk = King(2, 3, False)
# br1 = Rook(4, 3, False)
# br2 = Rook(2, 4, False)
# br3 = Rook(5, 4, False)
# wr2 = Rook(1, 5, True)
# wk = King(3, 5, True)
# br2a = Rook(1, 5, False)
# wr2a = Rook(2, 5, True)
# wr2b = Rook(2, 4, True)
#
# B2 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
#
# wk1 = King(3, 4, True)
# wb1 = Rook(1, 1, True)
# wr1 = Rook(1, 2, True)
# wb2 = Rook(5, 2, True)
# bk = Rook(2, 3, False)
# br1 = Bishop(4, 3, False)
# br2 = Rook(1, 4, False)
#
# B2 = (5, [wk1, wb1, wr1, wb2, bk, br1, br2, ])
# print(B2)
# wk1.move_to(2, 3, B2)
# br2.move_to(1, 2, B2)
# br1.move_to(5,2, B2)
# br2.move_to(1, 1, B2)
# print(B2)




# wk = King(1, 1, True)
# wr1 = Rook(4, 1, True)
# wb1 = Bishop(4, 2, True)
# br1 = Rook(2, 5, False)
# bb1 = Bishop(3, 5, False)
# bk = King(4, 4, False)
#
#
# B2 = (5, [wk, wr1, wb1, br1, bb1, bk])
# print(B2)
#
# print(wb1.move_to(3, 3, B2))
# is_check(False, B2)
#
# print(bk.move_to(3, 3, B2))

# wr1.move_to(3, 3, B2)
# is_check(wr1.side, B2)
# is_checkmate(wr1.side, B2)






# print(is_piece_at(5, 4, B2));
# print(is_piece_at(4, 4, B2));
#
# print("Can reach: " + str(br2.can_reach(5, 4, B2)))  # False
# print("Can reach: " + str(br2.can_reach(3, 4, B2)))  # true
# print("Can reach: " + str(br2.can_reach(2, 5, B2)))  # true, other side on it

# print(f" king - test reach {wb1.can_reach(3, 3, B2)}")
# print(f" king - can move to {wb1.can_move_to(3, 3, B2)}")
# print(f" king - move {bk.move_to(3, 3, B2)}")
#
# B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
# print(f" is check? --- {is_check(True, B2)}")
#
# print(type(bk))
# print(type(bk) == King)
