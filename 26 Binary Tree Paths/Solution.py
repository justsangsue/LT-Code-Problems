"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        result = []
        if not root:
            return result
            
        if not (root.left or root.right):
            result.append(str(root.val))
            return result
        
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        
        for path in left:
            result.append(str(root.val) + '->' + path)
        for path in right:
            result.append(str(root.val) + '->' + path)
        return result;