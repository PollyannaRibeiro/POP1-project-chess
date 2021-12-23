def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''

    unicode_char = ord(loc[0].lower()) - ord("a") + 1
    y = int(loc[1:])
    print(unicode_char)
    return tuple([unicode_char, y])


def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    unicode = chr(x + ord("a") - 1);
    print(unicode)

    return f"{unicode}{y}"


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
    return False
	
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
    def __init__(self, pos_X: int, pos_Y: int, side_: bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
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
        if is_equal(current_x, pos_X) and not is_equal(current_y, pos_Y) or not is_equal(current_x, pos_X) and is_equal(
                current_y, pos_Y):
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
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''

        current_x = self.pos_x
        current_y = self.pos_y
        current_side = self.side

        # check if there is a piece of the same side on the new position
        if is_piece_at(pos_X, pos_Y, B):
            piece_on_there = piece_at(pos_X, pos_Y, B)
            if current_side == piece_on_there.side:
                return False

        # check if the movement is possible
        if abs(current_x - pos_X) == abs(current_y-pos_Y) and abs(current_x - pos_X)>0:
            return True
        else:
            return False

    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        if self.can_reach(pos_X, pos_Y, B):
            current_x = self.pos_x
            current_y = self.pos_y

            # find out the moves
            x_move = pos_X - current_x
            y_move = pos_Y - self.pos_y
            find_moves = x_move + y_move

            x_counter : int
            y_counter : int

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
                    pass
                else:
                    x_counter = -1
                    y_counter = 1

            while current_x != pos_X and current_y != pos_Y:
                current_x += x_counter
                current_y += y_counter
                if is_piece_at(current_x, current_y, B):
                    return False
            return True

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B 
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

            print(f"board - bishop --- {new_board}")
            return new_board

class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''

        current_x = self.pos_x
        current_y = self.pos_y
        current_side = self.side

        # check if there is a piece of the same side on the new position
        if is_piece_at(pos_X, pos_Y, B):
            piece_on_there = piece_at(pos_X, pos_Y, B)
            if current_side == piece_on_there.side:
                return False

        # check if the movement is possible
        if is_equal(current_x, pos_X) and abs(current_y - pos_Y) == 1 or abs(current_x - pos_X) == 1 and is_equal(
            current_y, pos_Y):
            return True
        elif abs(current_x - pos_X) == abs(current_y - pos_Y) == 1:
            return True
        else:
            return False


    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

        if self.can_reach(pos_X, pos_Y, B):
            #  check if it is not overleaping any other piece
            if piece_at(pos_X, pos_Y, B):
                piece = piece_at(pos_X, pos_Y, B)
                if piece.side == self.side:
                    return False
                else:
                    return True
            else:
                return True
        return False

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
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

            print(f"board - king --- {new_board}")
            return new_board

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
