import sys
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ResultType:
    def __init__(self, size, nodeSum):
        self.size = size
        self.nodeSum = nodeSum
        
    
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def __init__(self):
        self.subtree = None
        self.subtreeResult = None  
        
    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.subtree
    
    def helper(self, root):
        if not root:
            return ResultType(0, 0)
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        result = ResultType(left.size + right.size + 1, 
                            left.nodeSum + right.nodeSum + root.val)
        if (not self.subtree) or \
           (result.nodeSum * self.subtreeResult.size > self.subtreeResult.nodeSum * result.size):
            self.subtreeResult = result
            self.subtree = root
        return result