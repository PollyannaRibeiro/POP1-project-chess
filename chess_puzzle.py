from piece import Piece
from rook import Rook
from bishop import Bishop
from king import King

from board import Board
from helpers import *


# ainda tentando descobrir o pq criei essa função

def is_new_bigger(num, new_num):
    if new_num > num:
        return True
    elif new_num < num:
        return False

def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''

    is_reachable = False

    board = B[1]
    for piece in board:
        if type(piece) is King and piece.side == side:
            for piece2 in board:
                if piece2.side != side:
                    if type(piece2) is Rook:
                        rook = Rook(piece2.pos_x, piece2.pos_y, piece2.side)
                        if(rook.can_reach(piece.pos_x, piece.pos_y, B)):
                            is_reachable = True

                    elif type(piece2) is Bishop:
                        bishop = Bishop(piece2.pos_x, piece2.pos_y, piece2.side)
                        if (bishop.can_reach(piece.pos_x, piece.pos_y, B)):
                            is_reachable = True

                    elif type(piece2) is King:
                        king = King(piece2.pos_x, piece2.pos_y, piece2.side)
                        if (king.can_reach(piece.pos_x, piece.pos_y, B)):
                            is_reachable = True

                    if is_reachable:
                        return True;
    return False


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_reach 
    '''

    board = B[1]
    is_check_possible: bool = is_check(side, B)

    if is_check_possible:

        for piece in board:
            if type(piece) is King and piece.side == side:
                king = King(piece.pos_x, piece.pos_y, piece.side)

                all_King_moves_options = [[king.pos_x, king.pos_y + 1], [king.pos_x, king.pos_y - 1], [king.pos_x + 1, king.pos_y],
                                         [king.pos_x - 1, king.pos_y], [king.pos_x + 1, king.pos_y + 1], [king.pos_x - 1, king.pos_y - 1],
                                         [king.pos_x + 1, king.pos_y - 1], [king.pos_x - 1, king.pos_y + 1]]

                for index in range(0, len(all_King_moves_options)-1):
                    king_moves = all_King_moves_options[index][0], all_King_moves_options[index][1]
                    can_walk = king.can_reach(king_moves[0], king_moves[1], B)
                    if can_walk:
                        new_board = king.move_to(king_moves[0], king_moves[1], B)
                        if(is_check(king.side, new_board)):
                            continue
                        else:
                            print("is not checkmate")
                            return False
                return True
    else:
        return False


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
        side = False

        for i in range(0, len(side_list)):
            for j in range(0, len(side_list[i])):
                piece = side_list[i][j]
                positions: tuple[int, int] = location2index(piece[1:])
                pos_x: int = positions[0]
                pos_y: int = positions[1]

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

        board = (line1, pieces_list)
        print(board)
        print(pieces_list)

    except IOError:
        print("Oops! It's not possible to read this file")


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

def conf2unicode(B: Board) -> str: 
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''    

if __name__ == '__main__': #keep this in
   main()
