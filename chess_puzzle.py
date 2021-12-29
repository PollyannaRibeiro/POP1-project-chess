import random
from typing import Optional
from piece import Piece
from helpers import *


class Rook(Piece):

    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule2] and [Rule4]
        '''
        if self.pos_x == pos_X or self.pos_y == pos_Y:
            squares_to_check: list[([int, int])] = list()
            if self.pos_x == pos_X:
                listY = range_list(pos_Y, self.pos_y)
                for y in listY:
                    squares_to_check.append((self.pos_x, y))
            else:
                listX: [int] = range_list(pos_X, self.pos_x)
                for x in listX:
                    squares_to_check.append((x, self.pos_y))

            for pos in squares_to_check:
                if pos[0] == pos_X and pos[1] == pos_Y:
                    if is_piece_at(pos[0], pos[1], B):
                        piece: Piece = piece_at(pos[0], pos[1], B)
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
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))
                # checking if there is an opposite piece on there and removes it

            # placing piece's new position
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
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))
                # If there is an opposite side piece on there, remove it
            new_piece = piece_at(self.pos_x, self.pos_y, new_board)
            # move piece for this position
            new_piece.pos_x = pos_X
            new_piece.pos_y = pos_Y
            return new_board
        return B
        # return the previous board if no piece is moved

    def possible_moves(self, B: Board) -> list[tuple[int, int]]:
        size = B[0]
        moves: list[tuple[int, int]] = list()
        for x in list(range(1, size+1)):
            if x != self.pos_x and self.can_move_to(x, self.pos_y, B):
                moves.append((x, self.pos_y))

        for y in list(range(1, size+1)):
            if y != self.pos_y and self.can_move_to(self.pos_x, y, B):
                moves.append((self.pos_x, y))
        return moves

    def __repr__(self):
        side = "W" if self.side else "B"
        return "Rook {} x:{} y:{}".format(side, self.pos_x, self.pos_y)
        # improving readability for testing purpose

    def __eq__(self, other: any):
        if Helper.is_type(other, Rook) and self.pos_x == other.pos_x \
                and self.pos_y == other.pos_y and self.side == other.side:
            return True
        else:
            return False


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
        # checking if the movement is possible
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
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))
                # If there is an opposite side piece on there, remove it

            # placing piece's new position
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
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))
                # If there is an opposite side piece on there, remove it
            new_piece = piece_at(self.pos_x, self.pos_y, new_board)
            # move piece for this position
            new_piece.pos_x = pos_X
            new_piece.pos_y = pos_Y
            return new_board
        return B
        # return the previous board if no piece is moved

    def possible_moves(self, B: Board) -> list[tuple[int, int]]:
        size = B[0]

        options = [(self.pos_x, self.pos_y + 1),
                   (self.pos_x, self.pos_y - 1),
                   (self.pos_x + 1, self.pos_y),
                   (self.pos_x - 1, self.pos_y),
                   (self.pos_x + 1, self.pos_y + 1),
                   (self.pos_x - 1, self.pos_y - 1),
                   (self.pos_x + 1, self.pos_y - 1),
                   (self.pos_x - 1, self.pos_y + 1)]

        moves: list[tuple[int, int]] = list()
        for x, y in options:
            if 0 < x <= size and 0 < y <= size and self.can_move_to(x, y, B):
                moves.append((x, y))
        return moves

    def __repr__(self):
        side = "W" if self.side else "B"
        return "King {} x:{} y:{}".format(side, self.pos_x, self.pos_y)
        # improving readability for testing purpose

    def __eq__(self, other):
        if Helper.is_type(other, King) and self.pos_x == other.pos_x \
                and self.pos_y == other.pos_y and self.side == other.side:
            return True
        else:
            return False


class Bishop(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''

        current_x = self.pos_x
        current_y = self.pos_y
        current_side = self.side

        # checking if the movement is possible
        if abs(current_x - pos_X) == abs(current_y - pos_Y) and abs(current_x - pos_X) > 0:

            # check if there is a piece of the same side on the new position
            if is_piece_at(pos_X, pos_Y, B):
                piece_on_there = piece_at(pos_X, pos_Y, B)
                if current_side == piece_on_there.side:
                    return False

            # checking overlapping possibility
            x_move = pos_X - current_x
            y_move = pos_Y - current_y
            find_moves = x_move + y_move

            x_counter: int
            y_counter: int

            #  all the possible bishop moves
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

            if is_piece_at(pos_X, pos_Y, B):
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))
                # If there is an opposite side piece on there, remove it

            # placing piece's new position
            piece_to_be_altered = piece_at(self.pos_x, self.pos_y, new_board)
            piece_to_be_altered.pos_x = pos_X
            piece_to_be_altered.pos_y = pos_Y
            return True
        else:
            return False

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''

        if self.can_move_to(pos_X, pos_Y, B):
            new_board = Helper.copy_board(B)
            if is_piece_at(pos_X, pos_Y, new_board):
                new_board[1].remove(piece_at(pos_X, pos_Y, new_board))
                # If there is an opposite side piece on there, remove it
            new_piece = piece_at(self.pos_x, self.pos_y, new_board)
            # move piece for this position
            new_piece.pos_x = pos_X
            new_piece.pos_y = pos_Y
            return new_board
        return B
        # return the previous board if no piece is moved

    def possible_moves(self, B: Board) -> list[tuple[int, int]]:
        size = B[0]

        x = self.pos_x - 1
        y = self.pos_y - 1
        lower_left = min(x, y)
        lower_right = min(size - x - 1, y)
        upper_left = min(x, size - y)
        upper_right = min(size - x - 1, size - y)

        xa = list(range(self.pos_x - lower_left, self.pos_x + upper_right + 1))
        ya = list(range(self.pos_y - lower_left, self.pos_y + upper_right + 1))

        xb = list(range(self.pos_x - upper_left, self.pos_x + lower_right + 1))
        yb = list(range(self.pos_y + upper_left, self.pos_y - lower_right - 1, -1))

        moves: list[tuple[int, int]] = list()
        for a, b in zip(xa, ya):
            if a != self.pos_x and b != self.pos_y and self.can_move_to(a, b, B):
                moves.append((a, b))

        for a, b in zip(xb, yb):
            if a != self.pos_x and b != self.pos_y and self.can_move_to(a, b, B):
                moves.append((a, b))
        return moves

    def __repr__(self):
        side = "W" if self.side else "B"
        return "Bishop {} x:{} y:{}".format(side, self.pos_x, self.pos_y)
        # improving readability for testing purpose

    def __eq__(self, other):
        if Helper.is_type(other, Bishop)  and self.pos_x == other.pos_x \
                and self.pos_y == other.pos_y and self.side == other.side:
            return True
        else:
            return False


class Helper:
    @staticmethod
    def is_type(piece: Piece, type_of) -> bool:
        return type(piece) == type_of

    @staticmethod
    def is_not_type(piece: Piece, type_of) -> bool:
        return type(piece) != type_of

    @staticmethod
    def checkmate_info(side: bool, B: Board) -> tuple[bool, Optional[Piece], tuple[int, int]]:
        # It returns if it's a checkmate:
        #   if true, returns no piece and an empty tuple -> True, None, (0, 0)
        #   else if is Not even a check, returns -> False, None, (0, 0)
        #   otherwise: return False, the piece that can be used to save the check and the movement that needs to be done

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

        # the king can run away from check by itself?
        king_moves = king_in_check.possible_moves(B)
        if len(king_moves) > 0:
            return False, king_in_check, random.choice(king_moves)

        for piece in board:
            if Helper.is_not_type(piece, King) and piece.side == side:

                # If more than one piece is targeting the King, it's impossible to avoid the checkmate without
                # moving itself

                if len(checkmate_pieces_options) == 1:

                    path_to_king = list()
                    opp_piece = checkmate_pieces_options[0]
                    x = king_in_check.pos_x
                    y = king_in_check.pos_y
                    x2 = checkmate_pieces_options[0].pos_x
                    y2 = checkmate_pieces_options[0].pos_y

                    # Firstly, check if it's possible to remove the piece that is threatening the king
                    if piece.can_reach(x2, y2, B):
                        return False, piece, (x2, y2)

                    # Otherwise, find it is possible to move some piece to stop it from reaching the king
                    # Getting the enemy rook route (x, y) to king

                    if Helper.is_type(opp_piece, Rook):
                        if x2 == x:
                            while y2 != y:
                                path_to_king.append([x2, y2])
                                if y2 < y:
                                    y2 += 1
                                else:
                                    y2 -= 1

                        elif y2 == y:
                            while x2 != x:
                                path_to_king.append([x2, y2])
                                if x2 < x:
                                    x2 += 1
                                else:
                                    x2 -= 1

                    # Getting the enemy bishop route (x, y) to the king
                    elif Helper.is_type(opp_piece, Bishop):
                        for item in zip(range_list(x2, x), range_list(y2, y)):
                            path_to_king.append([item[0], item[1]])

                    # checking who can save the king and defining it new position to it
                    for path in path_to_king:
                        if piece.can_reach(path[0], path[1], B):
                            new_board = piece.move_to(path[0], path[1], B)
                            if is_check(piece.side, new_board):
                                continue
                            else:
                                return False, piece, (path[0], path[1])

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

    @staticmethod
    def type_of_piece(piece: Piece, option_rook: str, option_bishop: str, option_king: str):
        if type(piece) == Rook:
            return option_rook
        elif type(piece) == Bishop:
            return option_bishop
        elif type(piece) == King:
            return option_king
        else:
            raise Exception("Unknown piece type")


def is_check(side: bool, B: Board) -> bool:

    board = B[1]
    for piece in board:

        if Helper.is_type(piece, King) and piece.side == side:
            king_in_check = King(piece.pos_x, piece.pos_y, piece.side)

            for piece2 in board:
                if piece2.side != side:
                    if piece2.can_reach(king_in_check.pos_x, king_in_check.pos_y, B):
                        return True
                    if piece2.can_move_to(king_in_check.pos_x, king_in_check.pos_y, B):
                        return True
    return False


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side
    '''

    info = Helper.checkmate_info(side, B)
    return info[0]


def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''

    try:
        f = open(filename, "r")
        line1 = int(f.readline())   # board size

        line2 = f.readline()       # white pieces
        white_pieces_list = line2.replace("\n", "").split(", ")

        line3 = f.readline()       # black pieces
        black_pieces_list = line3.replace("\n", "").split(", ")

        f.close()

        pieces_list = list()
        side_list = [white_pieces_list, black_pieces_list]

        piece_obj = None

        for i in range(0, len(side_list)):
            for j in range(0, len(side_list[i])):
                piece = side_list[i][j]
                positions: tuple[int, int] = location2index(piece[1:])
                pos_x: int = positions[0]
                pos_y: int = positions[1]
                side: bool = False  # black

                if i == 0:
                    side = True     # white

                if piece[0] == "B":
                    piece_obj = Bishop(pos_x, pos_y, side)
                elif piece[0] == "R":
                    piece_obj = Rook(pos_x, pos_y, side)
                elif piece[0] == "K":
                    piece_obj = King(pos_x, pos_y, side)
                else:
                    raise Exception("Unknown piece type")

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

        white_pieces_str = white_pieces_str[:-2]
        black_pieces_str = black_pieces_str[:-2]
        # removing the last 2 char -> ", "

        f = open(filename, "w")

        f.write(str(size) + "\n")
        f.write(white_pieces_str + "\n")
        f.write(black_pieces_str + "\n")
        f.close()

    except IOError:
        print("Sorry, the file couldn't be saved")


def find_black_move(B: Board) -> tuple[Optional[Piece], int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''

    piece_list = B[1]
    black_elem_list = list()
    white_elem_list = list()

    can_reach_enemy = list()
    check_risk = is_check(False, B)

    if check_risk:

        check_info = Helper.checkmate_info(False, B)
        piece_to_move_to_avoid_checkmate = check_info[1]
        move_to_save_from_checkmate = check_info[2]

        if piece_to_move_to_avoid_checkmate is not None:
            return piece_to_move_to_avoid_checkmate, move_to_save_from_checkmate[0], move_to_save_from_checkmate[1]

    else:
        # checking if black pieces can reach white pieces, and if possible to reach more than one white piece,
        # choose randomly which one will be moved
        for piece in piece_list:
            if piece.side is False:
                black_elem_list.append(piece)
            else:
                white_elem_list.append(piece)

        for piece in black_elem_list:
            for piece2 in white_elem_list:
                if piece.can_move_to(piece2.pos_x, piece2.pos_y, B):
                    can_reach_enemy.append([piece, piece2])  # black and white pieces respectively

        if len(can_reach_enemy) == 1:
            return can_reach_enemy[0][0], can_reach_enemy[0][1].pos_x, can_reach_enemy[0][1].pos_y

        elif len(can_reach_enemy) > 1:
            index = random.randrange(0, len(can_reach_enemy)-1)
            return can_reach_enemy[index][0], can_reach_enemy[index][1].pos_x, can_reach_enemy[index][1].pos_y

        else:
            # If no checkmate risk, or neither possible to reach any white piece, thus get a random x,y position and
            # check if any black can move to this position and keep check until to find one possible move.
            random.shuffle(black_elem_list)
            for piece in black_elem_list:
                moves = piece.possible_moves(B)
                if len(moves) > 0:
                    move = random.choice(moves)
                    return piece, move[0], move[1]

            return None, 0, 0


def conf2unicode(B: Board) -> str:
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''

    size = B[0]
    pieces_list = B[1]

    new_list = list()

    # creating an empty matrix
    for i in range(0, size):
        mini_list = list()
        for j in range(0, size):
            mini_list.append(" ")
        new_list.append(mini_list)

    # inserting chess board Unicode
    for piece in pieces_list:

        pos_x: int = piece.pos_x-1
        pos_y: int = piece.pos_y-1
        side: bool = piece.side
        type: str = None

        if side:
            type = Helper.type_of_piece(piece, "♖", "♗", "♔")
        else:
            type = Helper.type_of_piece(piece, "♜", "♝", "♚")

        if type is not None:
            new_list[pos_x][pos_y] = type

    list_to_print = ""
    for i in reversed(range(0, size)):
        for j in range(0, size):
            list_to_print += new_list[j][i]
        list_to_print += "\n"

    return list_to_print[:-1]   # removing last "\n"


def execute(filename) -> bool:

    try:
        started = False
        if not started:
            board = read_board(filename)
            print("The initial configuration is:")
            print(conf2unicode(board))
            started = True

        temp_board = Helper.copy_board(board)
        not_chekmate = True

        while not_chekmate:
            white_move = input("Next move of white: ")
            if white_move == "QUIT":
                filename_to_save = input("File name to store the configuration: ")

                save_board(filename_to_save, temp_board)
                print("Game configuration saved.")
                return True

            else:
                initial_pos: str = None
                final_pos: str = None

                # checking if it's valid move
                white_move = white_move.strip()     # removing spaces
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
                    print("This is not a valid move.")
                    continue

                index_initial_pos = location2index(initial_pos)
                index_final_pos = location2index(final_pos)

                if is_piece_at(index_initial_pos[0], index_initial_pos[1], temp_board):
                    piece_to_move = piece_at(index_initial_pos[0], index_initial_pos[1], temp_board)

                    if piece_to_move.can_reach(index_final_pos[0], index_final_pos[1], temp_board):
                        if piece_to_move.can_move_to(index_final_pos[0], index_final_pos[1], temp_board):
                            temp_board = piece_to_move.move_to(index_final_pos[0], index_final_pos[1], temp_board)
                        else:
                            print("it's check, can't make this move")
                            continue

                        print("The configuration after White's move is: \n")
                        print(conf2unicode(temp_board))

                        if is_checkmate(False, temp_board):
                            print("Game over. White wins.")
                            return True
                        else:
                            if is_check(False, temp_board):
                                print("It's check for black")

                            black_move = find_black_move(temp_board)
                            if black_move[0] is None:
                                print("Draw. Black has no movements available.")
                                return True

                            black_piece = black_move[0]

                            loc_initial_pos = index2location(black_piece.pos_x, black_piece.pos_y)
                            loc_final_pos = index2location(black_move[1], black_move[2])

                            temp_board = black_piece.move_to(black_move[1], black_move[2], temp_board)
                            print(
                                "Next move of Black is " + loc_initial_pos + loc_final_pos + ". The configuration after Black's move is: \n")
                            print(conf2unicode(temp_board))

                            if is_checkmate(True, temp_board):
                                print("Game over. Black wins.")
                                return True

                            if is_check(True, temp_board):
                                print("It's check for white")
                            continue
                    else:
                        print("This is not a valid move.")
                        continue

                else:
                    print("This is not a valid move. Doesn't have any piece on this position.")
                    continue
    except IOError:
        filename = input("This is not a valid file. File name for initial configuration: ")
        if filename == "QUIT":
            return True

        execute(filename)


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''

    filename = input("File name for initial configuration: ")
    execute(filename)


if __name__ == '__main__':  # keep this in
    main()
