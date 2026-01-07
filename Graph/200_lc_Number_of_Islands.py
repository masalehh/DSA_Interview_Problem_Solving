class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs_helper(r, c):
            if (
                    r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    (r, c) in visited or
                    grid[r][c] == '0'
            ):
                return

            visited.add((r, c))

            dfs_helper(r + 1, c)
            dfs_helper(r - 1, c)
            dfs_helper(r, c + 1)
            dfs_helper(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs_helper(r, c)
                    count += 1
        return count


"""
solved by myself and accepted at first attempt 
"""