from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        temp_list = []
        for col in range(col_len):
            for row in range(row_len-1, -1, -1):
                temp_list.append(matrix[row][col])
        i = 0
        for row in range(row_len):
            for col in range(col_len):
                matrix[row][col] = temp_list[i]
                i += 1