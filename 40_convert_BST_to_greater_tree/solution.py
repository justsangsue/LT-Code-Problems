# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
        
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        return self.helper(root)
    
    def helper(self, root):
        if root == None:
            return root
        self.helper(root.right)
        root.val += self.sum
        self.sum = root.val
        self.helper(root.left)
        return root

