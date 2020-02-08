# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        
        curVal = max(nums)
        curInd = nums.index(curVal)
        node = TreeNode(curVal)
        node.left = self.constructMaximumBinaryTree(nums[:curInd])
        node.right = self.constructMaximumBinaryTree(nums[(curInd + 1):])
        
        return node