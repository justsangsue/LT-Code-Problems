from collections import deque
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        
        result = []
        if graph == None or len(graph) == 0:
            return result
        
        # 1. get indegree
        indegree = self.getIndegree(graph)
        
        # 2. put indegree 0
        q = deque()
        for node in graph:
            if indegree[node] == 0:
                q.append(node)
        
        # 3. bfs
        while len(q) != 0:
            node = q.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return result
        
    def getIndegree(self, graph):
        indegree = dict()
        for node in graph:
            indegree[node] = 0
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
        return indegree
    