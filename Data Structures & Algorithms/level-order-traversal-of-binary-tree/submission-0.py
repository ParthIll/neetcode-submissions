class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
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
        return result