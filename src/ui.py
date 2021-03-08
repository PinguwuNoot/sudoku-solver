from model import SudokuBoard


class CUI:
    BOARD_1 = [
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

    def __init__(self):
        self.solver = SudokuBoard(CUI.BOARD_1)
        self.run()

    def run(self):
        print("Puzzle:\n{}".format(self.solver))
        self.solver.solve()
        print("Solution:\n{}".format(self.solver))


class GUI:
    pass


def main():
    CUI()
    # GUI()


if __name__ == "__main__":
    main()