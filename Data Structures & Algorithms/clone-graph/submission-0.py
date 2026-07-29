"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(curr):
            if not curr:
                return None
            if curr in old_to_new:
                return old_to_new[curr]

            # Create a clone for the current node
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # Recursively clone all neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)