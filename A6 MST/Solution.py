import functools
class Solution:
	"""
	@param graph: list of edges with weight [(node1, node2, weight)...]
	@return MST: list of edge in MST
	"""
	def kruskalMST(self, graph):
		if not graph:
			return []
		k = Kruskal(graph)
		return k.mst()


class Kruskal:
	def __init__(self, graph):
		nodes = set()
		for edge in graph:
			nodes.add(edge[0])
			nodes.add(edge[1])
		nodes = list(nodes)
		self.node_to_index = {nodes[i] : i for i in range(len(nodes))} 
		self.index_to_node = {i : nodes[i] for i in range(len(nodes))}
		self.edges = sorted(graph, key=lambda x : x[2])
		self.size = {nodes[i] : 1 for i in range(len(nodes))}

	def find(self, node):
		if self.index_to_node[self.node_to_index[node]] == node:
			return node
		node = self.index_to_node[self.node_to_index[node]]
		return self.find(node)

	def union(self, edge):
		root1 = self.find(edge[0])
		root2 = self.find(edge[1])
		if root1 == root2:
			return 
		if self.size[root1] > self.size[root2]:
			self.node_to_index[root2] = self.node_to_index[root1]
			self.size[root1] += self.size[root2]
		else:
			self.node_to_index[root1] = self.node_to_index[root2]
			self.size[root2] += self.size[root1]

	def mst(self):
		result = []
		for edge in self.edges:
			if self.find(edge[0]) != self.find(edge[1]):
				self.union(edge)
				result.append(edge)
		return result

if __name__ == '__main__':
	graph = [['A', 'E', 1],
			 ['A', 'D', 9],
			 ['A', 'B', 5],
			 ['E', 'F', 1],
			 ['E', 'D', 2],
			 ['D', 'F', 5],
			 ['D', 'G', 11],
			 ['D', 'H', 2],
			 ['D', 'B', 2],
			 ['B', 'C', 4],
			 ['F', 'G', 7],
			 ['G', 'H', 1],
			 ['G', 'I', 4],
			 ['H', 'I', 6],
			 ['H', 'C', 4],
			 ['C', 'I', 1],
			 ['C', 'J', 8],
			 ['I', 'J', 0]]
	sol = Solution()
	print(sol.kruskalMST(graph))




