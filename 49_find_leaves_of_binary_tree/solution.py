"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Record the height of each node

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        if root == None:
            return []
        hashmap = collections.defaultdict(list)
        self.helper(root, hashmap)
        return [hashmap.get(key) for key in hashmap]
    
    def helper(self, root, hashmap):
        if root.left == None and root.right == None:
            hashmap[1].append(root.val)
            return 1
        if root.left == None:
            h = self.helper(root.right, hashmap) + 1
        elif root.right == None:
            h = self.helper(root.left, hashmap) + 1
        else:
            h = max(self.helper(root.right, hashmap), self.helper(root.left, hashmap)) + 1
        hashmap[h].append(root.val)
        return h


#
#
# More elegant version
#
#

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        if root == None:
            return []
        hashmap = collections.defaultdict(list)
        self.helper(root, hashmap)
        return [hashmap.get(key) for key in hashmap]
    
    def helper(self, root, hashmap): # start from 0, not 1
        if root == None:
            return 0
        h = max(self.helper(root.right, hashmap), self.helper(root.left, hashmap)) + 1
        hashmap[h].append(root.val)
        return h

        
        
