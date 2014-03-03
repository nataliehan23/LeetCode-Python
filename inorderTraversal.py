# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res = []
        self.inorder(root, res)
        return res
        
    def inorder(self, root, path):
        if root is None:
            return
        self.inorder(root.left, path)
        path.append(root.val)
        self.inorder(root.right, path)
        return path
        