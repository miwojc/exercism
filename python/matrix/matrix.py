from typing import List


class Matrix(object):
    def __init__(self, matrix_string: str) -> None:
        self.lst_int = [
            [int(num) for num in row.split()] for row in matrix_string.split("\n")
        ]

    def row(self, index: int) -> List[int]:
        """Returns row at given index"""
        return self.lst_int[index - 1].copy()

    def column(self, index: int) -> List[int]:
        """Returns column at given index"""
        return [row[index - 1] for row in self.lst_int]
