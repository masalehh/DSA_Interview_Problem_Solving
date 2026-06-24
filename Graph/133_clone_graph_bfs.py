from typing import Optional
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new: dict[Node, Node] = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr_node = q.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in old_to_new:
                    q.append(neighbor)
                    old_to_new[neighbor] = Node(neighbor.val)
                curr_node.neighbors.append(neighbor)

        return old_to_new[node]


# Time & Space Complexity
#
#     Time complexity: O(V+E)O(V+E)
#     Space complexity: O(V)O(V)
