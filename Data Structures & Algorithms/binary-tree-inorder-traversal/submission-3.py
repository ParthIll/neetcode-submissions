class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret=[]
        ret+=self.inorderTraversal(root.left)
        ret.append(root.val)
        ret+=self.inorderTraversal(root.right)
        return ret