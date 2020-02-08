class Solution(object):
    preorder = []
    inorder = []
    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        return self.dfs(0, len(self.preorder), 0, len(self.inorder))
        
    def dfs(self, pre_start, pre_end, in_start, in_end): # [start, end)
        if pre_end - pre_start <= 0:
            return None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start : in_end+1].index(self.preorder[pre_start])
        root.left = self.dfs(pre_start+1, pre_start+1+offset, in_start, in_start+offset)
        root.right = self.dfs(pre_start+1+offset, pre_end, in_start+1+offset, in_end)
        return root
