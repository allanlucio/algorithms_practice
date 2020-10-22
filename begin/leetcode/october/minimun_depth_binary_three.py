# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        self.m=50000
        depth=1
        def st(root,depth):
            if(root.left == None and root.right == None):
                if(depth<self.m):
                    self.m=depth
                
                return
            depth+=1
            
            if(depth<self.m):
                if(root.left):
                    st(root.left,depth)
                if(root.right):
                    st(root.right,depth)
            
        if(root):    
            st(root,depth)
            return self.m
        else:
            return 0
