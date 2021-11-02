def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"]
    x = list.index(loc[0])+1
    y = int(loc[1:])
    return tuple([x, y])

def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"]
    return f"{list[x-1]}{y}"

class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.side = side_

Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B'''
    for piece in B[1]:
        if piece.pos_x == pos_X and piece.pos_y == pos_Y:
            print("Is piece is working")
            return True
	
def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    for piece in B[1]:
        if piece.pos_x == pos_X and piece.pos_y == pos_Y:
            return piece

def is_new_bigger(num, new_num):
    if new_num > num:
        return True
    elif new_num <num:
        return False

def is_equal(num, new_num):
    return new_num == num

class Rook(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)
	
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
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

        # check if the movement is possible
        if is_equal(current_x, pos_X) and not is_equal(current_y, pos_Y) or not is_equal(current_x, pos_X) and is_equal(current_y, pos_Y):
            return True
        else:
            return False


    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
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
            #  check if it is not overleaping any other piece
            if is_equal(self.pos_x, pos_X):
                start = min(self.pos_y, pos_Y)+1
                end = max(self.pos_y, pos_Y)

                while start != end:
                    if is_piece_at(pos_X, start, B):
                        return False
                    start +=1
                return True
            else:
                start = min(self.pos_x, pos_X) + 1
                end = max(self.pos_x, pos_X)

                while start != end:
                    if is_piece_at(start, pos_Y, B):
                        return False
                    start += 1
                return True

        return False

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        new_board: tuple[int, list[Piece]]

        if self.can_move_to(pos_X, pos_Y, B):
            board = B
            if piece_at(pos_X, pos_Y, B):
                piece_to_remove = piece_at(pos_X, pos_Y, B)
                board[1].remove(piece_to_remove)

            self.pos_x = pos_X
            self.pos_y = pos_Y
            new_board = board

            print(f"board - rook --- {new_board}")
            return new_board

class Bishop(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''


class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''

def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''

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
