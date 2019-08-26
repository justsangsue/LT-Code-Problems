# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
# Time complexity: O(n)
# Space complexity: O(n)
# n is the number of nodes

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return root
        res = []
        self.bfs(root, res)
        return res
    
    def bfs(self, root, res):
        q = collections.deque()
        q.append(root)
        while q:
            res.append(q[-1].val)
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
        
                
    
