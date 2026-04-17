from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            result[sorted_word].append(word)
        return list(result.values()) 

