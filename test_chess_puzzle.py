import pytest
from chess_puzzle import *

def test_locatio2index1():
    assert location2index("e2") == (5, 2)
    assert location2index("i4") == (9, 4)
    assert location2index("a7") == (1, 7)
    assert location2index("d5") == (4, 5)
    assert location2index("g24") == (7, 24)


def test_index2location1():
    assert index2location(5, 2) == "e2"
    assert index2location(9, 4) == "i4"
    assert index2location(1, 7) == "a7"
    assert index2location(4, 5) == "d5"
    assert index2location(7, 24) == "g24"


wb1 = Bishop(1,1,True)
wr1 = Rook(1,2,True)
wb2 = Bishop(5,2, True)
bk = King(2,3, False)
br1 = Rook(4,3,False)
br2 = Rook(2,4,False)
br3 = Rook(5,4, False)
wr2 = Rook(1,5, True)
wk = King(3,5, True)

B1 = (5, [wb1, wr1, wb2, bk, br1, br2, br3, wr2, wk])
'''
♖ ♔  
 ♜  ♜
 ♚ ♜ 
♖   ♗
♗    
'''

wr1_ = Rook(6, 2, True)
wr2_ = Rook(5, 4, True)
wr3_ = Rook(9, 8, True)
wb1_ = Bishop(10, 3, True)
bk_ = King(6, 7, False)
br1_ = Rook(7, 7, False)
B3 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])

bb1_ = Bishop(8, 8, False)


def test_is_piece_at1():
    assert is_piece_at(2, 2, B1) == False
    assert is_piece_at(6, 2, B3) == True
    assert is_piece_at(7, 6, B3) == False
    assert is_piece_at(2, 6, B1) == False
    assert is_piece_at(10, 3, B3) == True


def test_piece_at1():
    assert piece_at(4, 3, B1) == br1
    assert piece_at(4, 7, B1) == None
    assert piece_at(6, 2, B3) == wr1_
    assert piece_at(6, 7, B3) == bk_
    assert piece_at(1, 1, B3) == None


def test_can_reach1():
    assert wr2.can_reach(4, 5, B1) == False
    assert bk.can_reach(1, 2, B1) == True
    assert br1.can_reach(2, 3, B1) == False
    assert wb2.can_reach(4, 3, B1) == True
    assert br3.can_reach(4, 3, B1) == False


br2a = Rook(1,5,False)
wr2a = Rook(2,5,True)


def test_can_move_to1():
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert wr2a.can_move_to(2,4, B2) == False
    B3 = (10, [wr2_, wr3_, wb1_, bk_, br1_])
    assert br1_.can_move_to(7, 6, B3) == True
    B3 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
    assert br1_.can_move_to(7, 6, B3) == False      #checkmate
    assert bk_.can_move_to(7, 7, B3) == False
    B3 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_, bb1_])
    assert bk_.can_move_to(7, 8, B3) == True        #avoid checkmate


def test_is_check1():
    wr2b = Rook(2,4,True)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True
    B3 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
    assert is_check(False, B3) == True
    B3 = (10, [wr1_, wr2_, wb1_, bk_, br1_])
    assert is_check(False, B3) == True

    B3 = (10, [wr1_, wr2_, wb1_, bk_, br1_, bb1_])
    assert is_check(False, B3) == True
    B3 = (10, [wr2_, wb1_, bk_, br1_, bb1_])
    assert is_check(False, B3) == True




def test_is_checkmate1():

    br2b = Rook(4, 5, False)
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2b, br3, wr2, wk])
    assert is_checkmate(True, B2) == True

    B3 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
    assert is_checkmate(False, B3) == True

    B3 = (10, [wr1_, wr2_, wb1_, bk_, br1_])
    assert is_checkmate(False, B3) == False

    bb1_ = Bishop(8, 8, False)
    B3 = (10, [wr1_, wr2_, wb1_, bk_, br1_, bb1_])
    assert is_checkmate(False, B3) == False
    B3 = (10, [wr2_, wb1_, bk_, br1_, bb1_])
    assert is_checkmate(False, B3) == False

def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

def test_conf2unicode1():
    assert conf2unicode(B1) == "♖ ♔  \n ♜  ♜\n ♚ ♜ \n♖   ♗\n♗    "

def test_from_file():
    board = read_board("board_examp.txt")
    assert conf2unicode(board) == "♖ ♔  \n ♜  ♜\n ♚ ♜ \n♖   ♗\n♗    "
