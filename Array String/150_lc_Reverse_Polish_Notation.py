# I could do it by own, without taking any help from existed solution or AI

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp_stack: List[int] = []
        for i, item in enumerate(tokens):
            if item == '+':
                n2 = temp_stack.pop()
                n1 = temp_stack.pop()
                temp_stack.append(n1 + n2)
            elif item == '-':
                n2 = temp_stack.pop()
                n1 = temp_stack.pop()
                temp_stack.append(n1 - n2)
            elif item == '*':
                n2 = temp_stack.pop()
                n1 = temp_stack.pop()
                temp_stack.append(n1 * n2)
            elif item == '/':
                n2 = temp_stack.pop()
                n1 = temp_stack.pop()
                temp_stack.append(int(n1 / n2))
            else:
                temp_stack.append(int(item))
        return temp_stack[0]


case1 = ["2", "1", "+", "3", "*"]
case2 = ["4", "13", "5", "/", "+"]
case3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
sol = Solution()
r = sol.evalRPN(case1)
print(r)
