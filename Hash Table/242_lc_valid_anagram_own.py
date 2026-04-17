from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t


"""
More shorter version
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) 
        # No need to check length first, because is their length isn't same then, 
         Counter(string) will not same. 
"""
