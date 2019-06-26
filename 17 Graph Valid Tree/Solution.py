"""
If an undirected graph is a tree:
    1. number of edges = number of nodes - 1
    2. all nodes are connected
"""
from collections import deque
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def initializeGraph(self, n, edges):
        graph = dict()
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
        
        
    def validTree(self, n, edges):
        # write your code here
        if n == 0 or len(edges) != n - 1:
            return False 
        
        if n == 1:
            return True
        
        graph = self.initializeGraph(n, edges)
        q = deque()
        visited = dict()
        
        q.append(0)
        visited[0] = True
        visited_num = 1
        
        
        while len(q) != 0:
            node = q.popleft()
            for child in graph[node]:
                if visited.get(child) != True:
                    q.append(child)
                    visited[child] = True
                    visited_num += 1
        return visited_num == n        
        
        