# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        ll =[]
        self.preOrder(root, ll)
        return ll
   
    def preOrder(self, root, ll):
        if not root:
            return ll
        ll.append(root.val)
        self.preOrder(root.left,ll)
        self.preOrder(root.right,ll)
        return ll
    
        
        
        