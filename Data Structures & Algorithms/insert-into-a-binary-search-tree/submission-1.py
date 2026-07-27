# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        s=root
        while s.left or s.right:
            if s.left and val<s.val:
                s=s.left
            elif s.right and val>s.val:
                s=s.right
            else:
                break
        if val<s.val:
            s.left=TreeNode(val)
        else:
            s.right=TreeNode(val)
            
        
        return root