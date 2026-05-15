class Solution:
    def is_valid(self, s: str) -> bool:
        # Time Complexity: O(n)
        # - Each character in the string is processed exactly once.
        # - Stack operations (append, pop) are O(1).
        #   → Overall: O(n)

        # Space Complexity: O(n)
        # - In the worst case (e.g., all opening brackets), the stack stores all characters.
        #   → Overall: O(n)

        stack = []                         # Stack to store opening brackets
        valid_pairs = ['()', '{}', '[]']   # List of valid bracket pairs

        for ch in s:
            if ch in '({[':
                stack.append(ch)           # Push opening bracket to stack
            elif not stack or stack.pop() + ch not in valid_pairs:
                # If stack is empty (no matching open) OR
                # the popped bracket + current char is not a valid pair → invalid
                return False

        # If stack is empty, all brackets matched properly
        return not stack


# --- Example usage ---
sol = Solution()
print(sol.is_valid('([])'))     # True: properly nested brackets
print(sol.is_valid('([)]'))     # False: wrong order of brackets
print(sol.is_valid('()[]{}'))   # True: multiple valid pairs
print(sol.is_valid('(]'))       # False: mismatched pair
