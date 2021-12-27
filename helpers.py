from piece import Piece
# from rook import Rook
# from bishop import Bishop
# from king import King
from board import Board

def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''

    unicode_char = ord(loc[0].lower()) - ord("a") + 1
    y = int(loc[1:])
    return tuple([unicode_char, y])


def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    unicode = chr(x + ord("a") - 1);
    return f"{unicode}{y}"

def is_piece_at(pos_X: int, pos_Y: int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B'''
    for piece in B[1]:
        if piece.pos_x == pos_X and piece.pos_y == pos_Y:
            return True
    return False


def piece_at(pos_X: int, pos_Y: int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    for piece in B[1]:
        if piece.pos_x == pos_X and piece.pos_y == pos_Y:
            return piece


def is_equal(num, new_num):
    return new_num == num


def range_list(a: int, b: int) -> [int]:
    if a > b:
        step = -1
    else:
        step = 1
    return list(range(a, b, step))





