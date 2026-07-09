# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            small = min(p.val, q.val)
            big = max(p.val, q.val)
            print(curr.val)
            if small < curr.val and curr.val < big:
                return curr
            elif curr.val == small or curr.val == big:
                return curr
            elif curr.val > small:
                queue.append(curr.left)
            elif curr.val < big:
                queue.append(curr.right)
            