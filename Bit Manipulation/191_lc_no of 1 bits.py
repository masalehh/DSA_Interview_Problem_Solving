class Solution:
    def hammingWeight(self, n: int) -> int:
        count_bit = 0
        while n:
            count_bit += n & 1
            n >>= 1
        return count_bit 