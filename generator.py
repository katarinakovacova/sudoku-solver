import random

def generate_and_show_sudoku():

    def is_element_present(puzzle: list[list[int]], element: int, i: int, j: int) -> bool:
        """Check, if given element is already present in a given row and column.

        Args:
            puzzle: matrix of integers
            element: integer that is being checked
            i: index of the row
            j: index of the column
        """
        for m in range(9):
            if puzzle[i][m] == element or puzzle[m][j] == element:
                return True
        return False

    def make_new_puzzle() -> list[list[int]] | None:
        puzzle = [[0 for _ in range(9)] for _ in range(9)]

        indices = [0, 1, 2]

        for x in range(1, 10):
            for i in range(3):
                for j in range(3):
                    si = 3 * i
                    sj = 3 * j

                    random.shuffle(indices)
                    rowi = indices.copy()
                    random.shuffle(indices)
                    coli = indices.copy()

                    is_element_placed = False

                    for k in range(3):
                        for l in range(3):
                            mi = si + rowi[k]
                            mj = sj + coli[l]

                            if puzzle[mi][mj] != 0:
                                continue

                            if not is_element_present(puzzle, x, mi, mj):
                                puzzle[mi][mj] = x
                                is_element_placed = True
                                break

                        if is_element_placed:
                            break

                    if not is_element_placed:
                        return None

        return puzzle

    def show_puzzle(puzzle: list[list[int]]):
        for i in range(9):
            for j in range(9):
                print(puzzle[i][j], end=" ")
            print()

    count = 0

    while True:
        sudoku_puzzle = make_new_puzzle()
        if sudoku_puzzle is None:
            count += 1
        else:
            break

    print("Number of failed attempts:", count)
    show_puzzle(sudoku_puzzle)

generate_and_show_sudoku()
