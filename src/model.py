class SudokuBoard:
    def __init__(self, board=None):
        if board is None:
            self.board = [[0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0]]
        else:
            self.board = board

    def set_board(self, board):
        self.board = board

    def solve(self):
        empty_square = self.find_empty()
        if not empty_square:
            return True
        else:
            x, y = empty_square[1], empty_square[0]

        for val in range(1, len(self.board) + 1):
            if self._valid(val, x, y):
                self.board[y][x] = val
                if self.solve():
                    return True
                self.board[y][x] = 0

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def _valid(self, num, x, y):
        for i in range(len(self.board[0])):
            if self.board[y][i] == num:
                return False

        for i in range(len(self.board)):
            if self.board[i][x] == num:
                return False

        box_x = x // 3
        box_y = y // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def __str__(self):
        board_str = ""
        for y in range(len(self.board)):
            if y % 3 == 0:
                board_str += "---------------------\n"
            for x in range(len(self.board[0])):
                if x == 8:
                    board_str += str(self.board[y][x]) + "\n"
                else:
                    if (x + 1) % 3 == 0:
                        board_str += str(self.board[y][x]) + " | "
                    else:
                        board_str += str(self.board[y][x]) + " "
            if y == 8:
                board_str += "---------------------\n"
        return board_str