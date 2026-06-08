from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        zero_cordinates = []
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    zero_cordinates.append((i, j))

        for row, col in zero_cordinates:
            print(row, col)
            matrix[row] = [0] * col_len
            for r in matrix:
                # print(col)
                r[col] = 0

