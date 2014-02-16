# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        levels = []
        if root==None:
            return levels
        preLevel = []
        preNodes = []
        curLevel = []
        curNodes = []
        preNodes.append(root)
        preLevel.append(root.val)
        levels.append(preLevel)
        while True:
            while len(preNodes)>0:
                parent = preNodes.pop(0)
                if parent.left:
                    curNodes.append(parent.left)
                    curLevel.append(parent.left.val)
                if parent.right:
                    curNodes.append(parent.right)
                    curLevel.append(parent.right.val)
                if not parent.left and not parent.right:
                    continue
            if curNodes:
                levels.insert(0,curLevel)
                preNodes = curNodes
                curLevel = []
                curNodes = []
            else:
                break
        
        return levels
            