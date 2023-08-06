from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result: bool = False

        # check rows and columns validity
        rows: list[set] = [
            set(), set(), set(),
            set(), set(), set(),
            set(), set(), set()
        ]
        columns: list[set] = [
            set(), set(), set(),
            set(), set(), set(),
            set(), set(), set()
        ]
        squares: list[list[set]] = [
            [set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()]
        ]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                if (num in rows[i] or
                    num in columns[j] or
                    num in squares[i // 3][j // 3]):
                    return False

                rows[i].add(num)
                columns[j].add(num)
                squares[i // 3][j // 3].add(num)

        return True



def test_is_valid_sudoku_valid():
    input: list[list[str]] = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    expected: bool = True
    assert Solution().isValidSudoku(board=input) is expected


def test_is_valid_sudoku_invalid_2():
    input: list[list[str]] = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    expected: bool = False
    assert Solution().isValidSudoku(board=input) is expected


def test_is_valid_sudoku_invalid2():
    input: list[list[str]] = [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]
    ]
    expected = False
    assert Solution().isValidSudoku(board=input) is expected