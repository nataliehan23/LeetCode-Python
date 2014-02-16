# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root == None:
            return -1000
        mm = [-1000]
        _,maxm = self.dfs(root, mm)
        return maxm[0]
    def dfs(self, root, mm):
        if root == None:
            return 0, mm
        ll, mm = self.dfs(root.left, mm)
        rr, mm = self.dfs(root.right, mm)
        rval = root.val
        if ll > 0:
            rval += ll
        if rr > 0:
            rval += rr
        mm[0] = max(mm[0], rval)
        if max(ll,rr)>0:
            return max(ll,rr) + root.val, mm
        else:
            return root.val, mm
       