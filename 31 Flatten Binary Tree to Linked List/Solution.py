"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        self.helper(root);
    
    """
    @param root
    @return last TreeNode
    """
    def helper(self, root):
        if not root:
            return root
        leftLast = self.helper(root.left)
        rightLast = self.helper(root.right)
        if leftLast:
            leftLast.right = root.right
            root.right = root.left
            root.left = None
        if rightLast:
            return rightLast
        if leftLast:
            return leftLast
        return root
