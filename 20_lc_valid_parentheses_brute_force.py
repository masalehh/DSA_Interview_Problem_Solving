class Solution:
    def is_valid(self, s: str) -> bool:
        # Time Complexity: O(n^2)
        # - Each 'in' check and 'replace' operation takes O(n) time.
        # - In the worst case, the loop runs O(n) times (removing one pair per iteration).
        #   → Overall = O(n) * O(n) = O(n^2)
        #
        # Space Complexity: O(n)
        # - Each 'replace()' creates a new string copy (since Python strings are immutable).
        # - Therefore, at most O(n) additional space is used.

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


sol = Solution()
print(sol.is_valid('([])'))     # return True
print(sol.is_valid('([)]'))     # return False
print(sol.is_valid('()[]{}'))   # return True
print(sol.is_valid('(]'))       # return False
