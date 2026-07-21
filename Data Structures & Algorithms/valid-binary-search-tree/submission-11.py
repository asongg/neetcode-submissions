# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float("-inf"), float("inf"))])
        while queue:
            node, leftBound, rightBound = queue.popleft()
            if not (leftBound < node.val < rightBound):
                return False
            if node.left:
                if node.val > node.left.val:
                    queue.append((node.left, leftBound, node.val))
                else:
                    return False
            if node.right:
                if node.val < node.right.val:
                    queue.append((node.right, node.val, rightBound))
                else:
                    return False
        return True

