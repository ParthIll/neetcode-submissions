# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -2000
        def dfs(node):
            if not node:
                return 0
            leftPath = dfs(node.left)
            rightPath = dfs(node.right)
            maxWithSplitting = max(node.val,node.val+leftPath + rightPath,node.val+leftPath,node.val+rightPath)
            maxWithoutSplitting = max(node.val,node.val+max(leftPath,rightPath))
            if max(maxWithSplitting,maxWithoutSplitting)>self.res:
                self.res = max(maxWithSplitting,maxWithoutSplitting)
            
            return maxWithoutSplitting
        dfs(root)
        return self.res