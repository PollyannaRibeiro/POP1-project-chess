from abc import ABCMeta, abstractmethod

Piece = None
Board = tuple[int, list[Piece]]


class Piece(metaclass=ABCMeta):
    pos_x: int
    pos_y: int
    side: bool  # True for White and False for Black

    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.side = side_

    @abstractmethod
    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        pass

    @abstractmethod
    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        pass

    @abstractmethod
    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        pass

