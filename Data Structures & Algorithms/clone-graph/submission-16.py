"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        seen = {node: Node(node.val)}
        while queue:
            temp = queue.popleft()
            for i in temp.neighbors:
                if i not in seen:
                    queue.append(i)
                    seen[i] = Node(i.val)
                seen[temp].neighbors.append(seen[i])
        return seen[node]

