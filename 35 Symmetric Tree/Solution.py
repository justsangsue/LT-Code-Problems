# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.mirror(root.left, root.right)
    
    def mirror(self, root_left, root_right) -> bool:
        if not (root_left or root_right):
            return True
        if not (root_left and root_right):
            return False
        if root_left.val == root_right.val:
            return self.mirror(root_left.left, root_right.right) and self.mirror(root_left.right, root_right.left)
        return False
        