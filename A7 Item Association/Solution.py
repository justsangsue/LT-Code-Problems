class Solution:
	"""
	@param items: list of item list, [[itemA, itemB], [itemB, itemC], [itemD, itemE]]
	@return merged item with maximum size
	"""
	def maxItemAssociation(self, items):
		uf = UnionFind(items)
		return uf.findLargestGroup()


class UnionFind:
	def __init__(self, items):
		item_list = []
		for l in items:
			for item in l:
				if item not in item_list:
					item_list.append(item)
		item_list = list(item_list)
		self.nodes = item_list
		self.items = items
		self.item_to_index = {item_list[i] : i for i in range(len(item_list))}
		self.index_to_item = {i : item_list[i] for i in range(len(item_list))}
		self.size = {item_list[i] : 1 for i in range(len(item_list))}

	def findLargestGroup(self):
		result = []
		for l in self.items:
			for item in l:
				if item != self.find(item):
					self.union([item, find(item)])
					break
			self.union(l)
			
		largest_node = []
		max_size = self.size[self.nodes[0]]
		for node in self.nodes:
			if max_size < self.size[node]:
				largest_node = []
				largest_node.append(node)
				max_size = self.size[node]
			elif max_size == self.size[node]:
				largest_node.append(node)

		for l_node in largest_node:
			temp = []
			for node in self.nodes:
				if self.item_to_index[node] == self.item_to_index[l_node]:
					temp.append(node)
			result.append(temp)
		return result

	def find(self, node):
		if node == self.index_to_item[self.item_to_index[node]]:
			return node
		node = self.index_to_item[self.item_to_index[node]]
		return self.find(self, node)

	def union(self, nodes):	
		largest_node = sorted(nodes, key=lambda x : self.size[x])[-1]
		for node in nodes:
			self.item_to_index[node] = self.item_to_index[largest_node]
			self.size[largest_node] += 1

if __name__ == '__main__':
	items = [['A', 'B'],
			 ['B', 'C'],
			 ['E'],
			 ['E', 'F']]	
	sol = Solution()
	print(sol.maxItemAssociation(items))

