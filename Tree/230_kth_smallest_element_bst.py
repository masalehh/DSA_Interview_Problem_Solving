from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        cnt = k

        def inorder_dfs(node):
            nonlocal res, cnt
            if not node or cnt == 0:
                return
            inorder_dfs(node.left)
            if cnt == 0:
                return

            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            inorder_dfs(node.right)

        inorder_dfs(root)
        return res


"""
    Time & Space Complexity

    Time complexity: O(h+k)O(h+k) in terms of nodes visited, worst-case O(n)O(n)
    Space complexity: O(h)O(h) for the recursion stack, worst-case O(n)O(n)

"""