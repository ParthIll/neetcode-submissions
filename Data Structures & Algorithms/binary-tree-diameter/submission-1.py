class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def calculate_height(node):
            if not node:
                return 0
            
            # Recursively get the height of left and right subtrees
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
            
            # The diameter at the current node is the sum of left and right heights
            current_diameter = left_height + right_height
            
            # Update the global maximum diameter found so far
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the actual height of this node to its parent
            return 1 + max(left_height, right_height)
        
        calculate_height(root)
        return self.max_diameter