# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## I got  Output Limit Exceeded ERROR :-(
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        paths = []
        if root == None:
            return paths
        path = []
        self.dfs(root, paths, path, sum)
        return paths
    
    def dfs(self, root, paths, path, sum):
        if root.val == sum and not root.left and not root.right:
            path.append(root.val)
            paths.append(path)
            return paths
        path.append(root.val)
        if root.left:
            paths = self.dfs(root.left, paths, path, sum-root.val)
        if root.right:
            paths = self.dfs(root.right,paths, path, sum-root.val)
        path.pop()
        return paths