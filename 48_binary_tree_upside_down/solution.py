"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        if root == None:
            return root
        return self.helper(root)
    
    def helper(self, cur):
        if cur.left == None:
            return cur
        newRoot = self.helper(cur.left)
        cur.left.right = cur
        cur.left.left = cur.right
        cur.left = None
        cur.right = None
        return newRoot
        
        
        
        