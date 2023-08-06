from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result: bool = False

        # check rows and columns validity
        row_set: set[int] = set()
        col_set: set[int] = set()

        for row_num in range(len(board)):
            for col_num in range(len(board[row_num])):
                num = board[row_num][col_num]
                if num.isdigit() and num in row_set:
                    return False
                row_set.add(num)

                num = board[col_num][row_num]
                if num.isdigit() and num in col_set:
                    return False
                col_set.add(num)
            row_set.clear()
            col_set.clear()

        square_set: set[int] = set()
        for i in range(3):
            for j in range(3):

                for row_num in range(i * 3, i*3 + 3):
                    for col_num in range(j * 3, j * 3 + 3):
                        num = board[row_num][col_num]
                        if num.isdigit() and num in square_set:
                            return False
                        square_set.add(num)
                square_set.clear()

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
