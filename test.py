from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 1
        if len(t) > len(s):
            return ""

        count_t = Counter(t)
        res = s
        for i in range(len(s)):
            while right < len(s) and s[right] not in t:
                right += 1
            while left <= right and s[left] not in t:
                left += 1
            count_s = Counter(s[left:right + 1])
            if not (count_t - count_s):
                res = min(res, s[left:right + 1], key=len)
                right += 1
                left += 1
            else:
                right += 1

        return res


s = "ADOBECODEBANC"
t = "ABC"

sol = Solution()
print(sol.minWindow(s, t))


