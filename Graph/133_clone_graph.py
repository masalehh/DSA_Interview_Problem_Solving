from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:

        def dfs(current_node: Optional[Node]) -> Optional[Node]:
            if current_node is None:
                return None
            if current_node in visited_to_cloned:
                return visited_to_cloned[current_node]

            # Creating clone node
            cloned_node = Node(current_node.val)
            visited_to_cloned[current_node] = cloned_node

            for neighbor in current_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))

            return cloned_node

        visited_to_cloned: dict[Node, Node] = {}
        return dfs(node)


# 1 ---- 2
# |      |
# |      |
# 4 ---- 3
