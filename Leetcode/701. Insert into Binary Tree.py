# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def dfs(root, val):
            if not root:
                return []
            
            if val < root.val:
                # print("left")
                if root.left:
                    
                    dfs(root.left, val)
                else:
                    root.left = TreeNode(val)
                    return []
            if val > root.val:
                # print("right")
                if root.right:
                    
                    dfs(root.right, val)
                else:
                    root.right = TreeNode(val)
                    return []
        dfs(root,val)     
        return root