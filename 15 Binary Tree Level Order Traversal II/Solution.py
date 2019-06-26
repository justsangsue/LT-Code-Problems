from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        result = []
        if root == None:
            return result
            
        q = deque()
        q.append(root)

        while len(q) != 0:
            level = []
            l = len(q)
            for i in range(l):
                node = q.popleft()
                level.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            result.insert(0, level)
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    sol = Solution()
    print(sol.levelOrderBottom(root))