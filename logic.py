
from piece import *
from rook import Rook
from bishop import Bishop
from king import King


# class Logic:
#
#     @staticmethod
#     def is_type(piece: Piece, type_of) -> bool:
#         return type(piece) == type_of
#
#     @staticmethod
#     def is_not_type(piece: Piece, type_of) -> bool:
#         return type(piece) != type_of
#
#     @staticmethod
#     def is_check(side: bool, B: Board) -> bool:
#         '''
#         checks if configuration of B is check for side
#         Hint: use can_reach
#         '''
#
#         is_reachable = False
#
#         board = B[1]
#         for piece in board:
#
#             if Logic.is_type(piece, King) and piece.side == side:
#                 for piece2 in board:
#                     if piece2.side != side:
#                         if Logic.is_type(piece2, Rook):
#                             rook = Rook(piece2.pos_x, piece2.pos_y, piece2.side)
#                             if(rook.can_reach(piece.pos_x, piece.pos_y, B)):
#                                 is_reachable = True
#                                 print("it's check")
#
#                         elif Logic.is_type(piece2, Bishop):
#                             bishop = Bishop(piece2.pos_x, piece2.pos_y, piece2.side)
#                             if (bishop.can_reach(piece.pos_x, piece.pos_y, B)):
#                                 is_reachable = True
#                                 print("it's check")
#
#                         elif Logic.is_type(piece2, King):
#                             king = King(piece2.pos_x, piece2.pos_y, piece2.side)
#                             if (king.can_reach(piece.pos_x, piece.pos_y, B)):
#                                 is_reachable = True
#                                 print("it's check")
#
#                         if is_reachable:
#                             return True;
#         return False
#
#     @staticmethod
#     def checkmate_info(side: bool, B: Board) -> tuple[bool, list[int, int], list[type, int, int, bool]]:
#
#         move_to_save_from_checkmate = None
#         piece_to_move_to_avoid_checkmate = None
#
#         checkmate_cant_be_avoid = None
#
#         board = B[1]
#         is_check_possible: bool = Logic.is_check(side, B)
#
#         king_in_check = None
#         checkmate_pieces_options = list()
#
#         if is_check_possible:
#             # finding which pieces are putting the king in check
#             for piece in board:
#                 if Logic.is_type(piece, King) and piece.side == side:
#                     king_in_check = King(piece.pos_x, piece.pos_y, piece.side)
#                 if piece.side != side:
#                     # king = King(king_in_check.pos_x, king_in_check.pos_y, king_in_check.side)
#
#                     if Logic.is_type(piece, Rook):
#                         rook = Rook(piece.pos_x, piece.pos_y, piece.side)
#                         if rook.can_reach(king_in_check.pos_x, king_in_check.pos_y, B):
#                             checkmate_pieces_options.append(rook)
#                     elif Logic.is_type(piece, Bishop):
#                         bishop = Bishop(piece.pos_x, piece.pos_y, piece.side)
#                         if bishop.can_reach(king_in_check.pos_x, king_in_check.pos_y, B):
#                             checkmate_pieces_options.append(bishop)
#                     elif Logic.is_type(piece, King):
#                         king_opposite = King(piece.pos_x, piece.pos_y, piece.side)
#                         if king_opposite.can_reach(king_in_check.pos_x, king_in_check.pos_y, B):
#                             checkmate_pieces_options.append(king_opposite)
#
#             for piece in board:
#
#                 # king can run away?
#
#                 king = king_in_check
#
#                 all_King_moves_options = [[king.pos_x, king.pos_y + 1], [king.pos_x, king.pos_y - 1],
#                                           [king.pos_x + 1, king.pos_y],
#                                           [king.pos_x - 1, king.pos_y], [king.pos_x + 1, king.pos_y + 1],
#                                           [king.pos_x - 1, king.pos_y - 1],
#                                           [king.pos_x + 1, king.pos_y - 1], [king.pos_x - 1, king.pos_y + 1]]
#
#                 for index in range(0, len(all_King_moves_options) - 1):
#                     king_moves = all_King_moves_options[index][0], all_King_moves_options[index][1]
#                     can_walk = king.can_reach(king_moves[0], king_moves[1], B)
#                     if can_walk:
#                         new_board = king.move_to(king_moves[0], king_moves[1], B)
#                         if (Logic.is_check(king.side, new_board)):
#                             continue
#                         else:
#                             print("is not checkmate")
#                             move_to_save_from_checkmate = [King, king_moves[0], king_moves[1], king.side]
#                             checkmate_cant_be_avoid = False
#
#                 if Logic.is_not_type(piece, King) and piece.side == side:
#                     rook = None
#                     bishop = None
#
#                     if Logic.is_type(piece, Rook):
#                         rook = Rook(piece.pos_x, piece.pos_y, piece.side)
#                     elif Logic.is_type(piece, Bishop):
#                         bishop = Bishop(piece.pos_x, piece.pos_y, piece.side)
#
#                     if (len(checkmate_pieces_options) == 1):
#                         type_of = type(checkmate_pieces_options[0])
#                         path_to_king = list()
#
#                         opp_piece = checkmate_pieces_options[0]
#                         x = king.pos_x
#                         y = king.pos_y
#                         x2 = checkmate_pieces_options[0].pos_x
#                         y2 = checkmate_pieces_options[0].pos_y
#
#                         if rook is not None and rook.can_reach(x2, y2, B):
#                             move_to_save_from_checkmate = [Bishop, x2, y2, king.side]
#                             return False
#                         if bishop is not None and bishop.can_reach(x2, y2, B):
#                             move_to_save_from_checkmate = [Bishop, x2, y2, king.side]
#                             return False
#
#                         # torre com a mesma row
#                         if Logic.is_type(opp_piece, Rook):
#                             if x2 == x:
#                                 while y2 != y:
#                                     path_to_king.append([x2, y2])
#                                     if y2 < y:
#                                         y2 += 1
#                                     else:
#                                         y2 -= 1
#
#                             # torre com a mesma col
#                             if y2 == y:
#                                 while x2 != x:
#                                     path_to_king.append([x2, y2])
#                                     if x2 < x:
#                                         x2 += 1
#                                     else:
#                                         x2 -= 1
#
#                         elif Logic.is_type(opp_piece, Bishop):
#
#                             while x2 < x:
#                                 if y2 < y:
#                                     path_to_king.append([x2, y2])
#                                     x2 += 1
#                                     y2 += 1
#
#                                 if y2 > y:
#                                     path_to_king.append([x2, y2])
#                                     x2 += 1
#                                     y2 -= 1
#
#                             while x2 > x:
#                                 path_to_king.append([x2, y2])
#                                 if y2 < y:
#                                     x2 -= 1
#                                     y2 += 1
#                                 if y2 > y:
#                                     x2 -= 1
#                                     y2 -= 1
#                         elif Logic.is_type(opp_piece, King):
#                             # rook moves
#                             if x2 == x:
#                                 while y2 != y:
#                                     path_to_king.append([x2, y2])
#                                     if y2 < y:
#                                         y2 += 1
#                                     else:
#                                         y2 -= 1
#
#                             if y2 == y:
#                                 while x2 != x:
#                                     path_to_king.append([x2, y2])
#                                     if x2 < x:
#                                         x2 += 1
#                                     else:
#                                         x2 -= 1
#
#                             # bishop moves
#                             while x2 < x:
#                                 if y2 < y:
#                                     path_to_king.append([x2, y2])
#                                     x2 += 1
#                                     y2 += 1
#
#                                 if y2 > y:
#                                     path_to_king.append([x2, y2])
#                                     x2 += 1
#                                     y2 -= 1
#
#                             while x2 > x:
#                                 path_to_king.append([x2, y2])
#                                 if y2 < y:
#                                     x2 -= 1
#                                     y2 += 1
#                                 if y2 > y:
#                                     x2 -= 1
#                                     y2 -= 1
#
#                         new_board = B
#
#                         for path in path_to_king:
#
#                             if rook is not None and rook.can_reach(path[0], path[1], B):
#                                 rook.move_to(path[0], path[1], new_board)
#                                 if Logic.is_check(rook.side):
#                                     new_board = B
#                                     continue
#                                 else:
#                                     move_to_save_from_checkmate = [path[0], path[1]]
#                                     piece_to_move_to_avoid_checkmate = [Rook, rook.pos_x, rook.pos_y, rook.side]
#                                 checkmate_cant_be_avoid = False
#                             if bishop is not None and bishop.can_reach(path[0], path[1], B):
#                                 bishop.move_to(path[0], path[1], new_board)
#                                 if Logic.is_check(bishop.side):
#                                     new_board = B
#                                     continue
#                                 else:
#                                     move_to_save_from_checkmate = [path[0], path[1]]
#                                     piece_to_move_to_avoid_checkmate = [Bishop, bishop.pos_x, bishop.pos_y, bishop.side]
#                                 checkmate_cant_be_avoid = False
#
#                     elif len(checkmate_pieces_options) > 1:
#                         checkmate_cant_be_avoid = True
#             checkmate_cant_be_avoid = True
#
#         else:
#             checkmate_cant_be_avoid = False
#
#         return checkmate_cant_be_avoid, move_to_save_from_checkmate, piece_to_move_to_avoid_checkmate
