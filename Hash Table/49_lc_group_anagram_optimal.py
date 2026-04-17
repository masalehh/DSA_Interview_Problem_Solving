from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to group words by their character frequency signature
        # Key   -> tuple of 26 counts (for 'a' to 'z')
        # Value -> list of words that share the same signature (anagrams)
        result = defaultdict(list)

        # Iterate through each word in input
        for word in strs:
            # Initialize frequency count for 26 lowercase letters
            # Index 0 -> 'a', 1 -> 'b', ..., 25 -> 'z'
            count = [0] * 26

            # Count occurrences of each character in the word
            for char in word:
                # Convert character to index:
                # ord('a') = 97 → index 0
                # ord('b') = 98 → index 1
                # ...
                index = ord(char) - ord('a')
                count[index] += 1

            # Convert list to tuple so it can be used as a dictionary key (hashable)
            key = tuple(count)

            # Append the word to the corresponding anagram group
            result[key].append(word)

        # Return only the grouped anagrams (ignore keys)
        return list(result.values())
