# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        mmin = -100000
        mmax = 100000
        return self.isValidBSTRange(root, mmin, mmax)
        
    def isValidBSTRange(self, root, mmin, mmax):
        if root == None:
            return True
        if root.val < mmax and root.val > mmin:
            LL = self.isValidBSTRange(root.left, mmin, root.val)
            RR = self.isValidBSTRange(root.right, root.val, mmax)
            return  LL and RR
        else:
            return False
            
        
        