from typing import List, Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if node is None:
                return True

            if not inorder(node.left):
                return False

            nonlocal prev
            if prev >= node.val:
                return False
            prev = node.val

            return inorder(node.right)

        prev = -inf

        return inorder(root)


"""
Time Complexity: O(n)
Space Complexity: O(n)
          5
        /   \
       3     8
      / \   / \
     1   4 7   9

        5
       / \
      3   6
     / \
    1   4
    
        5
       / \
      3   4
     / \ / \
    1  4 3  6
"""