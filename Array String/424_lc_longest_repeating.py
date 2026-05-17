class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                """ Except most frequent number if rest of the characters is in 
                    my character replacement limit then we take the window size
                    because I have to replace characters other than most frequent character
                    in the current window """
                count[s[r]] -= 1
                l += 1
            res = max(res, r - l + 1)
            