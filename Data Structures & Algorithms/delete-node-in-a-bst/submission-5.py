# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val==key:
        
            rleft=root.left
            rright=root.right
            if not root.right:
                return rleft
            if not root.left:
                return rright
            root=root.right
            while root.left:
                root=root.left
            
            root.left=rleft
            return rright
            
            
        if root.left and root.left.val==key:
            if root.left.left:
                root.left.left.right=root.left.right if root.left.right else None
                root.left=root.left.left
            elif root.left.right:
                root.left=root.left.right
            else:
                root.left=None
        elif root.right and root.right.val==key:
            if root.right.right:
                root.right.right.left=root.right.left if root.right.left else None
                root.right=root.right.right
            elif root.right.left:
                root.right=root.right.left
            else:
                root.right=None
        else:
            if root.left:
                root.left=self.deleteNode(root.left,key)
            if root.right:
                root.right=self.deleteNode(root.right,key)
        return root
