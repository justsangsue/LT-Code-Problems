"""
Cannot pass, have duplicate in output
https://www.lintcode.com/problem/clone-graph/description
"""


from collections import deque
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node == None:
            return node;
            
        # get all connected nodes
        nodes = self.getNodes(node)
        # copy nodes
        old_new_map = dict()
        for nd in nodes:
            old_new_map[nd] = UndirectedGraphNode(nd.label)
            old_new_map[nd].neighbors = nd.neighbors
        return old_new_map[node]
    
    def getNodes(self, node):
        nodes = [node]
        q = deque()
        visited = dict()
        
        q.append(node)
        visited[node] = True
        while len(q) != 0:
            cur_node = q.popleft()
            for child in cur_node.neighbors:
                if child not in visited:
                    q.append(child)
                    visited[child] = True
                    nodes.append(child)
        return nodes           
                    
                    
                    
        