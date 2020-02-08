# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxDiff = -1
    stack = []
    
    def dfsAllNodeCheck(self, node):
        self.stack.append(node.val)
        
        if node.left:
            self.dfsAllNodeCheck(node.left)
        
        
        if node.right:
            self.dfsAllNodeCheck(node.right)
            
        if not node.left and not node.right:    
            self.maxDiff = max(self.maxDiff, abs(max(self.stack)-min(self.stack)))
        self.stack.pop()
        
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfsAllNodeCheck(root)
        
        return self.maxDiff
        