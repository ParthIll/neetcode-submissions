class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Returns a tuple: (rob_this_node, skip_this_node)
        def dfs(node):
            if not node:
                return (0, 0)
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            
            # If we rob this node, we cannot rob its immediate children
            rob_current = node.val + left_skip + right_skip
            
            # If we skip this node, we are free to choose whether to rob or skip its children (take the max of both for each child)
            skip_current = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_current, skip_current)
        
        return max(dfs(root))