class Solution:
    def reverseBits(self, n: int) -> int:
        rev_num = 0
        for _ in range(32):
            rev_num <<= 1
            lsb = n & 1
            rev_num |= lsb
            n >>= 1
        return rev_num 