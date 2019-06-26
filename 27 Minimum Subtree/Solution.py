import sys
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# Traverse + Divide & Conquer
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.subtree = None
        self.min_sum = sys.maxsize
        self.helper(root)
        return self.subtree
    
    def helper(self, root):
        if not root:
            return 0
        node_sum = self.helper(root.left) + self.helper(root.right) + root.val
        if node_sum <= self.min_sum:
            self.subtree = root
            self.min_sum = node_sum
        return node_sum
