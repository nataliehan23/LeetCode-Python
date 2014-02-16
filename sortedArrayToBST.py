# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
        if len(num) == 1:
            return TreeNode(num[0])
        left = 0
        right = len(num)
        mid = (right - left)//2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        if (mid + 1) < len(num):
            root.right = self.sortedArrayToBST(num[mid+1:])
        return root
            