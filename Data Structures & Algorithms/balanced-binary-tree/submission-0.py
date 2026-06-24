# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True
        def get_height(root):
            if not root:
                return 0
            height = max(get_height(root.left),get_height(root.right))+1
            if abs(get_height(root.left)-get_height(root.right))>1:
                self.balanced=False
            return height
        get_height(root)
        return self.balanced