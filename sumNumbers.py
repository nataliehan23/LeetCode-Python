# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        sum = self.dfs(root, 0)
        return sum
        
    def dfs(self, root, sum):
        if root == None:
            return 0
        sum = root.val + sum * 10
        if not root.left and not root.right:
            return sum
        return self.dfs(root.left, sum) + self.dfs(root.right, sum)
       
            
            