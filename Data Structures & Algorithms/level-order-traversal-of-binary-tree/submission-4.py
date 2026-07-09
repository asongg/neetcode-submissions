# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root,0)])
        seen = set()
        out = []
        while queue:
            node, depth = queue.popleft()
            if node:
                if depth in seen:
                    out[depth].append(node.val)
                else:
                    out.append([node.val])
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth+1))
                seen.add(depth)
        return out