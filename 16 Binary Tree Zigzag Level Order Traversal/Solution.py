from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        result = []
        if root == None:
            return result
        
        q = deque()
        q.append(root)
        leftToRight = True
        
        while len(q) != 0:
            level = []
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if leftToRight:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            result.append(level)
            leftToRight = not leftToRight
        return result

"""
Input:{1,2,3}
Output:[[1],[3,2]]
"""