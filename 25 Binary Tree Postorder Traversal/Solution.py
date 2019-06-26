"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        if not root:
            return result
        stack = [root]
        prev = None;
        curr = None;
        while stack:
            curr = stack[-1]
            if (not prev) or (prev.left == curr) or (prev.right == curr):
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:
                if curr.right:
                    stack.append(curr.right)
            else:
                result.append(curr.val)
                stack.pop()
            prev = curr
        return result
