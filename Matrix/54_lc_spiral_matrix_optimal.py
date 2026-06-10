from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res: List[int] = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [len(matrix[0]), len(matrix) - 1]   # col and row-1

        r, c, d = 0, -1, 0
        while steps[d & 1]:     # d = directions, even = horizontal, odd=vertical
            for i in range(steps[d & 1]):
                # in every iteration take forward the direction by adding 1
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1  # increment the d to change the directions 0=right, 1=down, 2=left, 3=up
            d %= 4  # that d keep in valid range

        return res
