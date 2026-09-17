# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        flipped = False
        while q:
            n = len(q)
            tempRes = []
            for i in range(n):
                temp = q.popleft()
                tempRes.append(temp.val)
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
            if flipped:
                tempRes.reverse()
                flipped = False
            else:
                flipped = True
            res.append(tempRes)
        return res