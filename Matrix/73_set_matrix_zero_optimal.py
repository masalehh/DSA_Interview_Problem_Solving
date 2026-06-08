from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        rows_len = len(matrix)
        cols_len = len(matrix[0])
        rows_to_zero = [False] * rows_len
        cols_to_zero = [False] * cols_len

        for rows_index in range(rows_len):
            for cols_index in range(cols_len):
                if matrix[rows_index][cols_index] == 0:
                    rows_to_zero[rows_index] = True
                    cols_to_zero[cols_index] = True

        for rows_index in range(rows_len):
            for cols_index in range(cols_len):
                if rows_to_zero[rows_index] or cols_to_zero[cols_index]:
                    matrix[rows_index][cols_index] = 0

