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

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''

def save_board(filename: str) -> None:
    '''saves board configuration into file in current directory in plain format'''


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
