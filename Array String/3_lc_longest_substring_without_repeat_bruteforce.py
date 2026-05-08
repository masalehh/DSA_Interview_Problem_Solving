class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        longest_sub = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] not in seen:
                    seen.add(s[j])
                    longest_sub = max(longest_sub, len(seen))
                else:
                    break

        return longest_sub
