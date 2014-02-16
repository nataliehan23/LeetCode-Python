# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:
            return True
        if not root.left and not root.right:
            return True
        if root.left and not root.right:
            return False
        if not root.left and root.right:
            return False
        if root.left and root.right:
            if root.left.val != root.right.val:
                return False
            else:
                preL = []
                preLL = self.pre(root.left, preL)
                postR = []
                postRR = self.post(root.right, postR)
                return preLL == postRR
    def pre(self, root, preL):
        if root == None:
            return preL
        preL = self.pre(root.left, preL)
        preL.append(root.val)
        preL = self.pre(root.right, preL)
        return preL
    def post(self, root, postR):
        if root == None:
            return postR
        postR = self.post(root.right, postR)
        postR.append(root.val)
        postR = self.post(root.left, postR)
        return postR
        
        
        
        