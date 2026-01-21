from typing import List, Set, Tuple


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited: Set[Tuple[int, int]] = set()

        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image

        def flood_fill_helper(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                image[r][c] != original_color
            ):
                return

            visited.add((r, c))
            image[r][c] = color

            flood_fill_helper(r+1, c)
            flood_fill_helper(r-1, c)
            flood_fill_helper(r, c+1)
            flood_fill_helper(r, c-1)

        flood_fill_helper(sr, sc)
        return image


images = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
r = 1
c = 1
colors = 2
image2 = [[0,0,0],[0,0,0]]
image3 = [[0,0,0],[0,0,0]]
sol = Solution()
print(sol.floodFill(image3, 0, 0, 2))

"""image = [[1, 1, 1], 
         [1, 1, 0], 
         [1, 0, 1]]
=== Accepted in leetcode ===
"""