from collections import deque

class graphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        if numCourses == 1:
            return True
        if prerequisites == None:
            return False
        graph = self.initializeGraph(numCourses, prerequisites)
        indegree = self.getIndegree(graph)
        q = deque()
        order = []
        for node in graph:
            if indegree[node] == 0:
                q.append(node)
                order.append(node)
        
        while len(q) != 0:
            node = q.popleft()
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    order.append(neighbor)
        
        return len(order) == len(graph)
    
    def initializeGraph(self, numCourses, prerequisites):
        graph = []
        for i in range(numCourses):
            graph.append(graphNode(i))
        for edge in prerequisites:
            graph[edge[0]].neighbors.append(graph[edge[1]])
        return graph
    
    def getIndegree(self, graph):
        indegree = dict()
        for node in graph:
            indegree[node] = 0
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
        return indegree
        
        
        
        
        
        
        
        
        
        