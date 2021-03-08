import unittest
from model import SudokuBoard


class TestBoard1(unittest.TestCase):
    def test_board_1(self):
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        solution = [
             [1, 2, 3, 4, 5, 6, 7, 8, 9],
             [4, 5, 6, 7, 8, 9, 1, 2, 3],
             [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [2, 1, 4, 3, 6, 5, 8, 9, 7],
             [3, 6, 5, 8, 9, 7, 2, 1, 4],
             [8, 9, 7, 2, 1, 4, 3, 6, 5],
             [5, 3, 1, 6, 4, 2, 9, 7, 8],
             [6, 4, 2, 9, 7, 8, 5, 3, 1],
             [9, 7, 8, 5, 3, 1, 6, 4, 2]
        ]
        solver = SudokuBoard(board)
        self.assertTrue(solver.solve())
        self.assertEqual(solver.board, solution)
        print(solver)


class TestBoard2(unittest.TestCase):
    def test_board_2(self):
        board = [
            [7, 0, 0, 0, 0, 9, 0, 0, 3],
            [0, 9, 0, 1, 0, 0, 8, 0, 0],
            [0, 1, 0, 0, 0, 7, 0, 0, 0],
            [0, 3, 0, 4, 0, 0, 0, 8, 0],
            [6, 0, 0, 0, 8, 0, 0, 0, 1],
            [0, 7, 0, 0, 0, 2, 0, 3, 0],
            [0, 0, 0, 5, 0, 0, 0, 1, 0],
            [0, 0, 4, 0, 0, 3, 0, 9, 0],
            [5, 0, 0, 7, 0, 0, 0, 0, 2]
        ]
        solution = [
            [7, 5, 8, 2, 4, 9, 1, 6, 3],
            [4, 9, 3, 1, 5, 6, 8, 2, 7],
            [2, 1, 6, 8, 3, 7, 4, 5, 9],
            [9, 3, 5, 4, 7, 1, 2, 8, 6],
            [6, 4, 2, 3, 8, 5, 9, 7, 1],
            [8, 7, 1, 9, 6, 2, 5, 3, 4],
            [3, 2, 7, 5, 9, 4, 6, 1, 8],
            [1, 8, 4, 6, 2, 3, 7, 9, 5],
            [5, 6, 9, 7, 1, 8, 3, 4, 2]
        ]
        solver = SudokuBoard(board)
        self.assertTrue(solver.solve())
        self.assertEqual(solver.board, solution)
        print(solver)


class TestBoard3(unittest.TestCase):
    def test_board_3(self):
        board = [
               [7,8,0,4,0,0,1,2,0],
               [6,0,0,0,7,5,0,0,9],
               [0,0,0,6,0,1,0,7,8],
               [0,0,7,0,4,0,2,6,0],
               [0,0,1,0,5,0,9,3,0],
               [9,0,4,0,6,0,0,0,5],
               [0,7,0,3,0,0,0,1,2],
               [1,2,0,0,0,7,4,0,0],
               [0,4,9,2,0,6,0,0,7]
        ]
        solution = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
        solver = SudokuBoard(board)
        self.assertTrue(solver.solve())
        self.assertEqual(solver.board, solution)
        print(solver)


# class TestBoard4(unittest.TestCase):
#     def test_board_4(self):
#         board = [
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 3, 0, 8, 5],
#             [0, 0, 1, 0, 2, 0, 0, 0, 0],
#             [0, 0, 0, 5, 0, 7, 0, 0, 0],
#             [0, 0, 4, 0, 0, 0, 1, 0, 0],
#             [0, 9, 0, 0, 0, 0, 0, 0, 0],
#             [5, 0, 0, 0, 0, 0, 0, 7, 3],
#             [0, 0, 2, 0, 1, 0, 0, 0, 0],
#             [0, 0, 0, 0, 4, 0, 0, 0, 9]
#         ]
#         solution = [[]]
#         solver = SudokuBoard(board)
#         self.assertTrue(solver.solve())
#         # self.assertEqual(solver.board, solution)
#         print(solver)


if __name__ == '__main__':
    unittest.main()
