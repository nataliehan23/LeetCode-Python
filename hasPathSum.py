# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        if root.left:
            LP = self.hasPathSum(root.left, sum-root.val)
        else:
            LP = False
        if root.right:
            RP = self.hasPathSum(root.right, sum-root.val)
        else:
            RP = False
        if LP or RP:
            return True
        else:
            return False
        