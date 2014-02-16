# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root==None:
            return 0
        LH = self.maxDepth(root.left)
        RH = self.maxDepth(root.right)
        return max(LH, RH) +1
        