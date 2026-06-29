# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.string=[]
        if root:
            self.string.append(str(root.val))
        else:
            return "N"
        def dfs(node):
            if not node:
                return
            if node.left:
                self.string.append(str(node.left.val))
            else:
                self.string.append("N")
            if node.right:
                self.string.append(str(node.right.val))
            else:
                self.string.append("N")
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        i=len(self.string)-1
        while self.string[i]=="N":
            self.string.pop()
            i-=1
        return ",".join(self.string)
        
    # Decodes your encoded data to tree.
    def deserialize(self, dat: str) -> Optional[TreeNode]:
        data = dat.split(",")
        
        self.root = TreeNode(int(data[0]))if data[0]!="N"else None
        self.i=1
        def dfs(node):
            if not node:
                return
            if self.i<len(data):
                if data[self.i]!="N":
                    node.left=TreeNode()
                    node.left.val = int(data[self.i])
                self.i +=1
            else:
                return
            if self.i<len(data):
                if data[self.i]!="N":
                    node.right =TreeNode()
                    node.right.val = int(data[self.i]) 
                self.i +=1
            else:
                return
            
            dfs(node.left)
            
            dfs(node.right)
        dfs(self.root)
        return self.root

