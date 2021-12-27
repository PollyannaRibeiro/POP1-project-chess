import random

from typing import Optional
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
        if self.pos_x == pos_X or self.pos_y == pos_Y:
            squares_to_check = list()
            if self.pos_x == pos_X:
                listY = range_list(pos_Y, self.pos_y)
                for y in listY:
                    squares_to_check.append((self.pos_x, y))
            else:
                listX = range_list(pos_X, self.pos_x)
                for x in listX:
                    squares_to_check.append((x, self.pos_y))

            for pos in squares_to_check:
                if pos[0] == pos_X and pos[1] == pos_Y:
                    if is_piece_at(pos[0], pos[1], B):
                        piece = piece_at(pos[0], pos[1], B)
                        if piece.side == self.side:
                            return False
                else:
                    if is_piece_at(pos[0], pos[1], B):
                        return False
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

            new_board = Helper.copy_board(B)
            if is_piece_at(pos_X, pos_Y, new_board):
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board)) # removing the competitor piece

            #placing the new position of the piece
            piece_to_be_altered = piece_at(self.pos_x, self.pos_y, new_board)
            piece_to_be_altered.pos_x = pos_X
            piece_to_be_altered.pos_y = pos_Y

            if is_check(piece_to_be_altered.side, new_board):
                return False
            return True
        else:
            return False

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''

        if self.can_move_to(pos_X, pos_Y, B):
            new_board = Helper.copy_board(B)
            if is_piece_at(pos_X, pos_Y, new_board):
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board)) # removing the competitor piece
            new_piece = piece_at(self.pos_x, self.pos_y)
            new_piece.pos_x = pos_X
            new_piece.pos_y = pos_Y

            print(f"board - rook --- {new_board}")
            return new_board
        return B

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

        new_board = Helper.copy_board(B)
        if self.can_reach(pos_X, pos_Y, new_board):

            if is_piece_at(pos_X, pos_Y, new_board):
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))  # removing the competitor piece

            # placing the new position of the piece
            piece_to_be_altered = piece_at(self.pos_x, self.pos_y, new_board)
            piece_to_be_altered.pos_x = pos_X
            piece_to_be_altered.pos_y = pos_Y

            if is_check(piece_to_be_altered.side, new_board):
                return False
            return True
        else:
            return False

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''

        if self.can_move_to(pos_X, pos_Y, B):
            new_board = Helper.copy_board(B)
            if is_piece_at(pos_X, pos_Y, new_board):
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))  # removing the competitor piece
            new_piece = piece_at(self.pos_x, self.pos_y, new_board)
            new_piece.pos_x = pos_X
            new_piece.pos_y = pos_Y

            print(f"board - king --- {new_board}")
            return new_board

        return B

class Bishop(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''

        current_x = self.pos_x
        current_y = self.pos_y
        current_side = self.side

        # check if the movement is possible
        if abs(current_x - pos_X) == abs(current_y - pos_Y) and abs(current_x - pos_X) > 0:

            # check if there is a piece of the same side on the new position
            if is_piece_at(pos_X, pos_Y, B):
                piece_on_there = piece_at(pos_X, pos_Y, B)
                if current_side == piece_on_there.side:
                    return False

            # checking overlaping

            x_move = pos_X - current_x
            y_move = pos_Y - current_y
            find_moves = x_move + y_move

            x_counter: int
            y_counter: int

            #  moves possibles
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
                if current_x is not pos_X and current_y is not pos_Y and is_piece_at(current_x, current_y, B):
                    return False
            return True
        else:
            return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

        new_board = Helper.copy_board(B)
        if self.can_reach(pos_X, pos_Y, new_board):

            if is_piece_at(pos_X, pos_X):
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))  # removing the competitor piece
            # placing the new position of the piece
            piece_to_be_altered = piece_at(self.pos_x, self.pos_y, new_board)
            piece_to_be_altered.pos_x = pos_X;
            piece_to_be_altered.pos_y = pos_Y;
            return True
        else:
            return False


    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''

        # new_board: tuple[int, list[Piece]]
        if self.can_move_to(pos_X, pos_Y, B):
            new_board = Helper.copy_board(B)
            if is_piece_at(pos_X, pos_X, new_board):
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))  # removing the competitor piece
            new_piece = piece_at(self.pos_x, self.pos_y, new_board)
            new_piece.pos_x = pos_X
            new_piece.pos_y = pos_Y

            print(f"board - bishop --- {new_board}")
            return new_board

        return B

class Helper:
    @staticmethod
    def is_type(piece: Piece, type_of) -> bool:
        return type(piece) == type_of

    @staticmethod
    def is_not_type(piece: Piece, type_of) -> bool:
        return type(piece) != type_of

    @staticmethod
    def checkmate_info(side: bool, B: Board) -> tuple[bool, Optional[Piece], tuple[int, int]]:

        board = B[1]
        is_check_possible: bool = is_check(side, B)

        if not is_check_possible:
            return False, None, (0, 0)

        king_in_check = None
        checkmate_pieces_options = list()

        # finding which pieces are putting the king in check
        for piece in board:
            if Helper.is_type(piece, King) and piece.side == side:
                king_in_check = King(piece.pos_x, piece.pos_y, piece.side)

                for piece2 in board:
                    if piece2.side != side:
                        if Helper.is_not_type(piece2, King) and piece2.can_reach(king_in_check.pos_x, king_in_check.pos_y, B):
                            checkmate_pieces_options.append(piece2)

        # king can run away?
        king = king_in_check
        all_King_moves_options = [[king.pos_x, king.pos_y + 1],
                                  [king.pos_x, king.pos_y - 1],
                                  [king.pos_x + 1, king.pos_y],
                                  [king.pos_x - 1, king.pos_y],
                                  [king.pos_x + 1, king.pos_y + 1],
                                  [king.pos_x - 1, king.pos_y - 1],
                                  [king.pos_x + 1, king.pos_y - 1],
                                  [king.pos_x - 1, king.pos_y + 1]]
        board_size = B[0]

        for index in range(0, len(all_King_moves_options) - 1):
            king_moves = all_King_moves_options[index][0], all_King_moves_options[index][1]
            if king_moves[0] > board_size or king_moves[0] < 1 or king_moves[1] > board_size or king_moves[1] < 1:
                continue
            else:
                can_walk = king.can_reach(king_moves[0], king_moves[1], B)
                if can_walk:
                    new_board = king.move_to(king_moves[0], king_moves[1], B)
                    if (is_check(king.side, new_board)):
                        continue
                    else:
                        print("is not checkmate")
                        return False, king, king_moves

        for piece in board:
            if Helper.is_not_type(piece, King) and piece.side == side:
                rook = None
                bishop = None

                if Helper.is_type(piece, Rook):
                    rook = Rook(piece.pos_x, piece.pos_y, piece.side)
                elif Helper.is_type(piece, Bishop):
                    bishop = Bishop(piece.pos_x, piece.pos_y, piece.side)

                # More than one piece targeting the King can't avoid the check without moving the King
                if (len(checkmate_pieces_options) == 1):
                    type_of = type(checkmate_pieces_options[0])
                    path_to_king = list()

                    opp_piece = checkmate_pieces_options[0]
                    x = king.pos_x
                    y = king.pos_y
                    x2 = checkmate_pieces_options[0].pos_x
                    y2 = checkmate_pieces_options[0].pos_y

                    if rook is not None and rook.can_reach(x2, y2, B):
                        return False, rook, (x2, y2)
                    if bishop is not None and bishop.can_reach(x2, y2, B):
                        return False, bishop, (x2, y2)

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
                        elif y2 == y:
                            while x2 != x:
                                path_to_king.append([x2, y2])
                                if x2 < x:
                                    x2 += 1
                                else:
                                    x2 -= 1

                    elif Helper.is_type(opp_piece, Bishop):
                        for item in zip(range_list(x2, x), range_list(y2, y)):
                            path_to_king.append([item[0], item[1]])

                    for path in path_to_king:
                        if rook is not None and rook.can_reach(path[0], path[1], B):
                            new_board = rook.move_to(path[0], path[1], B)
                            if is_check(rook.side, new_board):
                                continue
                            else:
                                return False, rook, (path[0], path[1])
                        if bishop is not None and bishop.can_reach(path[0], path[1], B):
                            new_board = bishop.move_to(path[0], path[1], B)
                            if is_check(bishop.side, new_board):
                                continue
                            else:
                                return False, bishop, (path[0], path[1])

                else:
                    return True, None, (0, 0)
        return True, None, (0, 0)

    @staticmethod
    def copy_board(B: Board) -> Board:
        pieces = list()
        for piece in B[1]:
            if Helper.is_type(piece, King):
                pieces.append(King(piece.pos_x, piece.pos_y, piece.side))
            elif Helper.is_type(piece, Bishop):
                pieces.append(Bishop(piece.pos_x, piece.pos_y, piece.side))
            elif Helper.is_type(piece, Rook):
                pieces.append(Rook(piece.pos_x, piece.pos_y, piece.side))
        return B[0], pieces


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


def is_check(side: bool, B: Board) -> bool:

    board = B[1]
    for piece in board:

        if Helper.is_type(piece, King) and piece.side == side:
            king_in_check = King(piece.pos_x, piece.pos_y, piece.side)

            for piece2 in board:
                if piece2.side != side:
                    if Helper.is_type(piece2, Rook):
                        rook = Rook(piece2.pos_x, piece2.pos_y, piece2.side)
                        if (rook.can_reach(king_in_check.pos_x, king_in_check.pos_y, B)):
                            return True

                    elif Helper.is_type(piece2, Bishop):
                        bishop = Bishop(piece2.pos_x, piece2.pos_y, piece2.side)
                        if (bishop.can_reach(piece.pos_x, piece.pos_y, B)):
                            return True

                    elif Helper.is_type(piece2, King):
                        king = King(piece2.pos_x, piece2.pos_y, piece2.side)
                        if (king.can_reach(piece.pos_x, piece.pos_y, B)):
                            return True
    return False


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_reach 
    '''

    info = Helper.checkmate_info(side, B)
    print(info)
    print(info[0])
    return info[0]


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
    check_risk = is_check(False, B)

    if check_risk:

        check_info = Helper.checkmate_info(False, B)
        piece_to_move_to_avoid_checkmate = check_info[1]
        move_to_save_from_checkmate = check_info[2]

        #  to update move_to_save_from_checkmate and piece_to_move_to_avoid_checkmate
        if piece_to_move_to_avoid_checkmate is not None:
            return piece_to_move_to_avoid_checkmate, move_to_save_from_checkmate[0], move_to_save_from_checkmate[1]

    else:

        for piece in piece_list:
            if piece.side is False:
                black_elem_list.append(piece)
            else:
                white_elem_list.append(piece)

        for piece in black_elem_list:
            for piece2 in white_elem_list:
                if piece.can_reach(piece2.pos_x, piece2.pos_y, B):
                    can_reach_enemy.append([piece, piece2])

        if len(can_reach_enemy) == 1:

            return can_reach_enemy[0][0], can_reach_enemy[0][1].pos_x, can_reach_enemy[0][1].pos_y

        elif len(can_reach_enemy) > 1:
            index = random.randrange(0, len(can_reach_enemy)-1)

            return can_reach_enemy[index][0], can_reach_enemy[index][1].pos_x, can_reach_enemy[index][1].pos_y
        else:

            while True:

                pos_x = random.randrange(1, size)
                pos_y = random.randrange(1, size)

                for piece in black_elem_list:
                    if piece.can_reach(pos_x, pos_y, B):
                        return piece, pos_x, pos_y

                    else:
                        continue


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

    # filename = input("File name for initial configuration: ")
    filename = "board_examp2.txt"
    is_working = execute(filename)

    if not is_working:
        while not is_working:
            filename = input("This is not a valid file. File name for initial configuration: ")
            if filename == "QUIT":
                return
            is_working = execute(filename)
    else:
        print("The initial configuration is:")
        execute(filename)
        board = read_board(filename)

        not_chekmate = True
        while not_chekmate:

            white_move = input("Next move of white: ")

            if white_move == "QUIT":
                filename_to_save = input("File name to store the configuration: ")
                try:
                    save_board(filename_to_save, board)
                    print("The game configuration saved.")
                    return
                except IOError:
                    print("error on saving")
            else:
                initial_pos: str = None
                final_pos: str = None

                index_initial_pos: tuple[int, int] = None
                index_final_pos: tuple[int, int] = None

                if len(white_move) == 4:

                    initial_pos = white_move[0:2]
                    final_pos = white_move[2:]

                elif len(white_move) == 6:
                    initial_pos = white_move[0:3]
                    final_pos = white_move[3:]

                elif len(white_move) == 5:

                    if white_move[2].isdigit():
                        initial_pos = white_move[0:3]
                        final_pos = white_move[3:]
                    else:
                        initial_pos = white_move[0:2]
                        final_pos = white_move[2:]

                else:
                    white_move = input("This is not a valid move. Next move of White: ")

                index_initial_pos = location2index(initial_pos)
                index_final_pos = location2index(final_pos)
                temp_board = board

                if is_piece_at(index_initial_pos[0], index_initial_pos[1], board):
                    piece_to_move = piece_at(index_initial_pos[0], index_initial_pos[1], board)

                    if piece_to_move.can_reach(index_final_pos[0], index_final_pos[1], board):

                        temp_board = piece_to_move.move_to(index_final_pos[0], index_final_pos[1], temp_board)
                        if is_check(True, temp_board):
                            print("it's check, can't make this move")
                        else:
                            board = temp_board
                            save_board(filename, board)
                            print("The configuration after White's move is: \n")
                            print(execute(filename))
                            if is_checkmate(False, board):
                                print("Game over. White wins.")
                                return
                            else:
                                black_move = find_black_move(board)
                                black_piece = black_move[0]
                                # black_move_initial_pos = black_piece.pos_x, black_piece.pos_y
                                # black_move_final_pos = black_move[1], black_move[2]

                                loc_initial_pos = index2location(black_piece.pos_x, black_piece.pos_y)
                                loc_final_pos = index2location(black_move[1], black_move[2])

                                board = black_piece.move_to(black_move[1], black_move[2], board)

                                save_board(filename, board)
                                print("Next move of Black is " + loc_initial_pos + loc_final_pos + ". The configuration after Black's move is: \n")
                                print(execute(filename))

                                if is_checkmate(True, board):
                                    print("Game over. Black wins.")
                                    return
                                continue
                    else:
                        print("not possible to reach")

                else:
                    print("wrong move")



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
