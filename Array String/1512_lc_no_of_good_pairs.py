# I wrote the solution by myself within 9 minutes and accepted in leetcode at first try
from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Counts the number of good pairs in the array.

        A pair (i, j) is considered good if:
        - nums[i] == nums[j]
        - i < j

        Approach:
        - Count the frequency of each number using a hashmap (Counter).
        - For each number with frequency `n`, the number of ways to pick 2 identical elements is:
              nC2 = n * (n - 1) // 2
        - Sum this value for all unique numbers.

        Time Complexity:
            O(n) — single pass to build frequency map + iteration over unique elements

        Space Complexity:
            O(n) — for storing frequency map

        Args:
            nums (List[int]): List of integers

        Returns:
            int: Total number of good pairs
        """

        # Step 1: Build frequency map of elements
        freq_nums = Counter(nums)

        # Step 2: Initialize total count of good pairs
        total_good_pair = 0

        # Step 3: For each unique value, calculate number of valid pairs
        for val in freq_nums.values():
            # Number of ways to choose 2 items from 'val' occurrences
            current_pair = (val * (val - 1)) // 2

            # Accumulate result
            total_good_pair += current_pair

        # Step 4: Return total number of good pairs
        return total_good_pair