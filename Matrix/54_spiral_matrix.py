from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0

        bottom = len(matrix)
        right = len(matrix[0])

        result: List[int] = []

        while top < bottom and left < right:
            left_to_right = left
            while left_to_right < right:
                result.append(matrix[left][left_to_right])
                left_to_right += 1

            top += 1
            top_to_bottom = top
            while top_to_bottom < bottom:
                result.append(matrix[top_to_bottom][right-1])
                top_to_bottom += 1
            right -= 1
            if not (top < bottom and left < right):
                break

            right_to_bottom = right - 1
            while right_to_bottom >= left:
                result.append(matrix[bottom-1][right_to_bottom])
                right_to_bottom -= 1
            bottom -= 1

            bottom_to_top = bottom - 1
            while bottom_to_top >= top:
                result.append(matrix[bottom_to_top][left])
                bottom_to_top -= 1
            left += 1

        return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
s = Solution()
print("Result: ", s.spiralOrder(matrix))
s.spiralOrder(matrix)
