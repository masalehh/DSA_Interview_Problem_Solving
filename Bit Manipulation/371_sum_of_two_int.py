class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            a_lsb = (a >> i) & 1
            b_lsb = (b >> i) & 1
            curr_bit = a_lsb ^ b_lsb ^ carry
            carry = (a_lsb + b_lsb + carry) >= 2
            if curr_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res