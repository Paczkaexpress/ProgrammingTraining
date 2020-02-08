# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    arr = []
    
    def dfs(self, root, currentLevel):
        if len(self.arr) == 0:
            return
        newNode = self.arr[0]
        currentLevel += 1
        # print("{} {}".format(currentLevel, newNode))
        if currentLevel <= newNode[1]:
            self.arr.pop(0)
            if root.left == None:
                # print("left {} {}".format(currentLevel, newNode))
                root.left = TreeNode(newNode[0])
                self.dfs(root.left, currentLevel)
            else:
                # print("right {} {}".format(currentLevel, newNode))
                root.right = TreeNode(newNode[0])
                self.dfs(root.right, currentLevel)
                
        # print("{} {}".format(currentLevel, newNode))
        if len(self.arr) == 0:
            return
        newNode = self.arr[0]
        if currentLevel <= newNode[1]:
            self.arr.pop(0)
            # print("right {} {}".format(currentLevel, newNode))
            root.right = TreeNode(newNode[0])
            self.dfs(root.right, currentLevel)
            
            
    def recoverFromPreorder(self, S: str) -> TreeNode:
        c = 0
        levelFlag = False
        val = 0
        for i in range(len(S)):
            if i == len(S)-1:
                c = c*10 + int(S[i])
                self.arr.append([c,val])
            elif S[i] != '-':
                levelFlag = True
                c = c*10 + int(S[i])
            else:
                if levelFlag == True:
                    levelFlag = False
                    self.arr.append([c,val])
                    c = 0
                    val = 0
                val += 1
                
        # print(self.arr)
        root = TreeNode(self.arr.pop(0)[0])
        # print(root)
        self.currentLevel = 0
        self.dfs(root, self.currentLevel)
        # print(root)
        return root