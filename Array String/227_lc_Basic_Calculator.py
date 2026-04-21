class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        s = s.replace(' ', '')
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in '+-*/' or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))
                op = ch
                num = 0
        return sum(stack)


sol = Solution()
r = sol.calculate(" -3+5 / 2 ")
print(r)

"""
Time and Space Complexity
Time Complexity: O(n)

The algorithm iterates through the string s exactly once using a single for loop. For each character, 
it performs constant time operations:

Checking if a character is a digit: O(1)
Updating the value v: O(1)
Performing stack operations (append/pop): O(1)
Arithmetic operations (+, -, *, /): O(1)
After the loop, the sum() function iterates through the stack once, which contains at most n elements, 
adding another O(n) operation. Therefore, the overall time complexity is O(n) + O(n) = O(n).

Space Complexity: O(n)

The main space consumption comes from the stack stk. In the worst case, when the expression contains only 
addition and subtraction operations (e.g., "1+2+3+4+5"), every number will be pushed onto the stack. 
Since there can be at most n/2 numbers in a string of length n (considering operators and digits), 
the stack can grow up to O(n) size. The other variables (v, n, sign, i, c) use constant space O(1). 
Therefore, the overall space complexity is O(n).
"""