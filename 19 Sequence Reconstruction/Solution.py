from collections import deque
class GraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        
        
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        if len(seqs) == 1 and seqs[0] == org: # corner case
            return True
        if org == None or seqs == None or seqs == []: # corner case
            return False
        if len(seqs) > 1 and [] in seqs: # corner case
            return False
   
        # 1. convert seqs to a directed graph
        graph = self.getGraph(seqs)
        for node in graph:
            print(node.label, [neighbor.label for neighbor in node.neighbors])
        # 2. get topological order
        # 2.1 get indegree
        indegree = self.getIndegree(graph)
        if indegree == {}: # corner case
            return False
        for nd, val in indegree.items():
            print(nd.label, val)
        # 2.2 bfs
        order = []
        q = deque()
        for node in graph:
            if indegree[node] == 0:
                q.append(node)
                order.append(node.label)
        
        while len(q) != 0:
            node = q.popleft()
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    order.append(neighbor.label)
            if len(q) > 1:
                return False
        print(order, org)
        return order == org
    
    def getGraph(self, seqs):
        graph = dict()
        graph_list = []
        for edge in seqs:
            if len(edge) == 1:
                graph[edge[0]] = GraphNode(edge[0])
                continue
            for i in range(len(edge) - 1):
                if edge[i] not in graph:
                    graph[edge[i]] = GraphNode(edge[i])
                if edge[i + 1] not in graph:
                    graph[edge[i + 1]] = GraphNode(edge[i + 1])
                if graph[edge[i + 1]] not in graph[edge[i]].neighbors:
                    graph[edge[i]].neighbors.append(graph[edge[i + 1]])
        for label, node in graph.items():
            graph_list.append(node)
        return graph_list
    
    def getIndegree(self, graph):
        indegree = dict()
        for node in graph:
            indegree[node] = 0
        for node in graph:
            for neighbor in node.neighbors:
                try:
                    indegree[neighbor] += 1
                except KeyError:
                    return {}
        return indegree

if __name__ == '__main__':
    org = [5,3,2,4,1]
    seqs = [[5,3,2,4],[4,1],[1],[3],[2,4],[1000000000]]
    sol = Solution()
    print(sol.sequenceReconstruction(org, seqs))