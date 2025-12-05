from typing import List, Any
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        curr_stack: List[int] = []
        len_temp = len(temperatures)
        result: List[int] = [0] * len_temp

        for i in range(len_temp-1, -1, -1):
            while curr_stack and temperatures[curr_stack[-1]] <= temperatures[i]:
                curr_stack.pop()

            if curr_stack:
                result[i] = curr_stack[-1] - i
            curr_stack.append(i)
        return result

