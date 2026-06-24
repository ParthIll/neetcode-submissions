# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.equivalent = True
        def checktree(p,q):
            if not p and not q:
                return
            if not q:
                self.equivalent =False
                return
            if not p:
                self.equivalent = False
                return
            if p.val != q.val:
                self.equivalent=False
            checktree(p.left,q.left)
            checktree(p.right,q.right)
            return
        checktree(p,q)
        return self.equivalent