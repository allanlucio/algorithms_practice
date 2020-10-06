class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if(root == None):
            return TreeNode(val=val)
        
        def insertion(root):
            
            
            
            if(val >= root.val):
                if(root.right == None):
                    root.right = TreeNode(val=val)
                else:
                    insertion(root.right)
            elif(val< root.val):
                if(root.left == None):
                    root.left = TreeNode(val=val)
                else:
                    insertion(root.left)
        
        insertion(root)
        
        return root
