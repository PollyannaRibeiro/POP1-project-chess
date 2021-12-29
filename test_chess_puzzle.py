import pytest
from chess_puzzle import *


# ---------- Boards to be used in the tests-----------------------

wb1 = Bishop(1, 1, True)
wr1 = Rook(1, 2, True)
wb2 = Bishop(5, 2, True)
bk = King(2, 3, False)
br1 = Rook(4, 3, False)
br2 = Rook(2, 4, False)
br3 = Rook(5, 4, False)
wr2 = Rook(1, 5, True)
wk = King(3, 5, True)

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
B2 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
bb1_ = Bishop(8, 8, False)


br1e = Rook(4, 4, False)
br2e = Rook(1, 5, False)
bb1e = Bishop(5, 3, False)
bke = King(2, 2, False)
wb1e = Bishop(2, 4, True)
wke = King(3, 5, True)
wr1e = Rook(4, 1, True)


# ---------- helpers.py -----------------------

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


def test_range_list():
    assert range_list(5, 10) == [5, 6, 7, 8, 9]
    assert range_list(10, 5) == [10, 9, 8, 7, 6]
    assert range_list(-1, 3) == [-1, 0, 1, 2]
    assert range_list(5, 5) == []
    assert range_list(5, 4) == [5]


def test_is_piece_at1():
    assert is_piece_at(2, 2, B1) == False
    assert is_piece_at(6, 2, B2) == True
    assert is_piece_at(7, 6, B2) == False
    assert is_piece_at(2, 6, B1) == False
    assert is_piece_at(10, 3, B2) == True


def test_piece_at1():
    assert piece_at(4, 3, B1) == br1
    assert piece_at(4, 7, B1) is None
    assert piece_at(6, 2, B2) == wr1_
    assert piece_at(6, 7, B2) == bk_
    assert piece_at(1, 1, B2) is None


# ---------- Piece methods -----------------------

def test_can_reach1():
    assert wr2.can_reach(4, 5, B1) == False
    assert bk.can_reach(1, 2, B1) == True
    assert br1.can_reach(2, 3, B1) == False
    assert wb2.can_reach(4, 3, B1) == True
    assert br3.can_reach(4, 3, B1) == False


br2a = Rook(1, 5, False)
wr2a = Rook(2, 5, True)


def test_can_move_to1():
    bk2 = King(3, 1, False)
    B2 = (5, [wb1, wr1, wb2, bk2, br1, br2a, br3, wr2a, wk])
    assert wr2a.can_move_to(2, 4, B2) == False
    B3 = (10, [wr2_, wr3_, wb1_, bk_, br1_])
    assert br1_.can_move_to(7, 6, B3) == True
    B3 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
    assert br1_.can_move_to(7, 6, B3) == False      #checkmate
    assert bk_.can_move_to(7, 7, B3) == False
    B3 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_, bb1_])
    assert bk_.can_move_to(7, 8, B3) == True        #avoid checkmate


def test_move_to():
    bk2 = King(3, 1, False)
    B = (5, [wb1, wr1, wb2, bk2, br1, br2a, br3, wr2a, wk])
    assert wr2a.move_to(2, 4, B) == B               # can't move because it's check
    B2 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
    assert br1_.move_to(7, 6, B2) == B2             # can't move because is checkmate

    br2c = Rook(1, 5, False)
    wr2c = Rook(2, 4, True)
    B3 = (5, [wb1, wr1, wb2, bk, br2c, wr2c, wk])

    assert wk.move_to(2, 4, B3) == B3           # can't move because there is another piece from the same side on there
    assert wk.move_to(4, 4, B3) != B3           # the piece moved and changed the board

    B4 = (5, [br1e, br2e, bb1e, bke, wb1e, wke, wr1e])
    assert wb1e.move_to(1, 5, B4) != B4         #the piece moved and saved from check


# ---------- Helper @static methods -----------------------

def test_is_type():
    assert Helper.is_type(bk, Bishop) == False
    assert Helper.is_type(bk, King) == True
    assert Helper.is_type(wr2, Rook) == True
    assert Helper.is_type(wr2, Bishop) == False
    assert Helper.is_type(wb1, Bishop) == True


def test_is_not_type():
    assert Helper.is_not_type(wr2, King) == True
    assert Helper.is_not_type(wr2, Rook) == False
    assert Helper.is_not_type(wb1, King) == True
    assert Helper.is_not_type(wb1, Bishop) == False
    assert Helper.is_not_type(bk, King) == False


def test_copy_board():
    B = (5, [br1e, br2e, bb1e, bke, wb1e, wke, wr1e])
    B_copy = Helper.copy_board(B)
    B_double_copy = Helper.copy_board(B_copy)
    assert B == B_copy
    assert B == B_double_copy
    assert B_copy == B_double_copy

    B_copy = wb1e.move_to(1, 5, B_copy)
    assert B != B_copy
    assert B_copy != B_double_copy
    assert B == B_double_copy


def test_type_of_piece():

    none_piece = Piece

    assert Helper.type_of_piece(wr1, "♖", "♗", "♔") == "♖"
    assert Helper.type_of_piece(wb1, "♖", "♗", "♔") == "♗"
    assert Helper.type_of_piece(wk, "♖", "♗", "♔") == "♔"
    assert Helper.type_of_piece(br1, "♜", "♝", "♚") == "♜"
    assert Helper.type_of_piece(bb1_, "♜", "♝", "♚") == "♝"
    assert Helper.type_of_piece(bk, "♜", "♝", "♚") == "♚"
    with pytest.raises(Exception):
        Helper.type_of_piece(none_piece, "♜", "♝", "♚")


# ---------- chess_puzzle_functions -----------------------

wkb = King(3,1, True)
wr2b = Rook(2, 4, True)


def test_is_check1():
    bk2 = King(3, 1, False)
    B2 = (5, [wb1, wr1, wb2, bk2, br1, br2a, br3, wr2b, wk])
    assert is_check(True, B2) == True
    B3 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
    assert is_check(False, B3) == True
    B3 = (10, [wr1_, wr2_, wb1_, bk_, br1_])
    assert is_check(False, B3) == True

    B3 = (10, [wr1_, wr2_, wb1_, bk_, br1_, bb1_])
    assert is_check(False, B3) == True
    B3 = (10, [wr2_, wb1_, bk_, br1_, bb1_])
    assert is_check(False, B3) == True

    B4 = (5, [wb1, wr1, wb2, bk2, br1, br2a, br3, wr2b, wkb])
    assert is_check(True, B4) == False


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

def test_checkmate_info():

    # It's check and can't do anything to change it
    bk2 = King(3, 1, False)
    br2b = Rook(4, 5, False)
    B1 = (5, [wb1, wr1, wb2, bk2, br1, br2b, br3, wr2, wk])
    assert Helper.checkmate_info(True, B1) == (True, None, (0, 0))

    # it's not a check
    B2 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
    assert Helper.checkmate_info(True, B2) == (False, None, (0, 0))

    B3 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2b, wkb])
    assert Helper.checkmate_info(True, B3) == (False, None, (0, 0))

    # It's check and king moving can save it
    br2c = Rook(1, 5, False)
    wb2c = Bishop(2, 4, True)
    B4 = (5, [wb1, wr1, wb2, bk, br2c, wb2c, wk])
    assert Helper.checkmate_info(True, B4) == (False, wk, (4, 4))

    # it's check and a piece moving can save it
    B5 = (5, [br1e, br2e, bb1e, bke, wb1e, wke, wr1e])
    assert  Helper.checkmate_info(True, B5) == (False, wb1e, (1, 5))


def test_read_board1():
    def create_board(data: str):
        filename = "temp.txt"
        f = open(filename, "w")
        f.write(data)
        f.close()
        return read_board(filename)

    def get_pieces(side: bool, B: Board) -> list[Piece]:
        return [i for i in B[1] if i.side == side]

    board_1 = create_board("10\n" +
                           "Re4, Rf2, Bj3, Ka1\n" +
                           "Kf7, Rg7")
    assert board_1[0] == 10
    assert get_pieces(True, board_1) == [Rook(5, 4, True), Rook(6, 2, True),
                                         Bishop(10, 3, True), King(1, 1, True)]
    assert get_pieces(False, board_1) == [King(6, 7, False), Rook(7, 7, False)]

    board_2 = create_board("5\n" +
                           "Ka1, Be4\n" +
                           "Rc3, Ke1")
    assert board_2[0] == 5
    assert get_pieces(True, board_2) == [King(1, 1, True), Bishop(5, 4, True)]
    assert get_pieces(False, board_2) == [Rook(3, 3, False), King(5, 1, False)]

    with pytest.raises(Exception):
        create_board("invalid\n" +
                     "Ka1, Be4\n" +
                     "Rc3, Ke1")

    with pytest.raises(Exception):
        create_board("5\n" +
                     "K, Be4\n" +
                     "Rc3, Ke1")

    # test provided
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


def test_possible_moves():
    wb1 = Bishop(4, 2, True)
    wr1 = Rook(2, 3, True)
    wk = King(2, 1, True)
    bb1 = Bishop(2, 4, False)
    br1 = Rook(3, 5, False)
    bk = King(2, 5, False)

    B = (5, [wb1, wr1, wk, bb1, br1, bk])
    assert wb1.possible_moves(B) == [(3, 1), (5, 3), (2, 4), (3, 3), (5, 1)]
    assert wr1.possible_moves(B) == [(1, 3), (3, 3), (4, 3), (5, 3), (2, 2), (2, 4)]
    assert wk.possible_moves(B) == [(2, 2), (1, 1), (1, 2)]
    assert bb1.possible_moves(B) == [(1, 3), (1, 5), (3, 3), (4, 2)]
    assert br1.possible_moves(B) == [(4, 5), (5, 5), (3, 1), (3, 2), (3, 3), (3, 4)]
    assert bk.possible_moves(B) == [(1, 5), (1, 4), (3, 4)]

def test_conf2unicode1():
    assert conf2unicode(B1) == "♖ ♔  \n ♜  ♜\n ♚ ♜ \n♖   ♗\n♗    "
    B2 = (5, [wb1, wr1, wb2, bk, br1, br2a, br3, wr2a, wk])
    assert conf2unicode(B2) == "♜♖♔  \n    ♜\n ♚ ♜ \n♖   ♗\n♗    "
    B3 = (5, [wb2, bk, br1, br3, wr2a, wk])
    assert conf2unicode(B3) == " ♖♔  \n    ♜\n ♚ ♜ \n    ♗\n     "

    B4 = (10, [wr1_, wr2_, wr3_, wb1_, bk_, br1_])
    assert conf2unicode(B4) == "          \n" \
                               "          \n" \
                               "        ♖ \n" \
                               "     ♚♜   \n" \
                               "          \n" \
                               "          \n" \
                               "    ♖     \n" \
                               "         ♗\n" \
                               "     ♖    \n" \
                               "          "
    B5 = (5, [br1e, br2e, bb1e, bke, wb1e, wke, wr1e])
    assert conf2unicode(B5) == "♜ ♔  \n ♗ ♜ \n    ♝\n ♚   \n   ♖ "


