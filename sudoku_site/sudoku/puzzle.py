import random


def is_valid(puzzle: list[list[int]]) -> bool:
    def is_valid_unit(unit):
        return len(set(unit)) == 9 and all(1 <= num <= 9 for num in unit)

    def is_valid_row(puzzle):
        return all(is_valid_unit(row) for row in puzzle)

    def is_valid_column(puzzle):
        return all(is_valid_unit(col) for col in zip(*puzzle))

    def is_valid_box(puzzle):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [puzzle[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_unit(box):
                    return False
        return True

    return is_valid_row(puzzle) and is_valid_column(puzzle) and is_valid_box(puzzle)


def _is_element_present(puzzle: list[list[int]], element: int, i: int, j: int) -> bool:
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


def try_make_new_puzzle() -> list[list[int]] | None:
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

                        if not _is_element_present(puzzle, x, mi, mj):
                            puzzle[mi][mj] = x
                            is_element_placed = True
                            break

                    if is_element_placed:
                        break

                if not is_element_placed:
                    return None

    return puzzle


def _show_puzzle(puzzle: list[list[int]]):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=" ")
        print()


def make_new_puzzle() -> tuple[int, list[list[int]]]:
    n_attempts = 0

    while True:
        sudoku_puzzle = try_make_new_puzzle()
        if sudoku_puzzle is None:
            n_attempts += 1
        else:
            break

    return n_attempts, sudoku_puzzle


def remove_numbers_from_puzzle(puzzle: list[list[int]], level: str) -> list[list[int]]:
    level_to_holes = {
        "easy": 40,
        "medium": 50,
        "hard": 60,
    }
    
    holes = level_to_holes.get(level)
    
    puzzle_with_holes = [row[:] for row in puzzle] 
    
    for _ in range(holes):
        while True:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if puzzle_with_holes[row][col] != 0:
                puzzle_with_holes[row][col] = 0
                break

    return puzzle_with_holes

