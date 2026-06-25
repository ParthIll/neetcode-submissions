# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        ret =[]
        def dfs(node, level):
            if not node:
                return
            
            # If we are visiting this level for the first time, 
            # create a new sublist for it
            if len(result) == level:
                result.append([])
            
            # Append the current node's value to its respective level
            result[level].append(node.val)
            
            # Move to the next level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        for res in result:
            ret.append(res[-1])
        return ret