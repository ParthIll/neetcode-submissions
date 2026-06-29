# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.hasPathSumbool = False
        def dfs(node,add):
            if not node:
                return
            add+=node.val
            if add==targetSum and not node.left and not node.right:
                self.hasPathSumbool = True
            dfs(node.left,add)
            dfs(node.right,add)
        dfs(root,0)
        return self.hasPathSumbool