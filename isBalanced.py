# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        LH = self.balanceHeight(root.left)
        RH = self.balanceHeight(root.right)
        if LH == -1:
            return False
        if RH == -1:
            return False
        if LH - RH > 1 or RH - LH > 1:
            return False
        else:
            return True
    def balanceHeight(self, root):
        if root == None:
            return 0
        LBH = self.balanceHeight(root.left)
        RBH = self.balanceHeight(root.right)
        if LBH == -1:
            return -1
        if RBH == -1:
            return -1
        if LBH - RBH > 1 or RBH - LBH >1:
            return -1
        else:
            return max(LBH, RBH) + 1
        
        