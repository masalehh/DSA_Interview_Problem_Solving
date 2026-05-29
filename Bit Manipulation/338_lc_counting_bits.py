class Solution:
    def countBits(self, n: int) -> List[int]:
        count_set = []
        for i in range(n+1):
            count = 0
            while i:
                i &= (i-1)
                count += 1
            count_set.append(count)
        return count_set


"""Solved by myself"""
