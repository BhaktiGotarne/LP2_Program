class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = []
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])	
	def find(self, parent, i):
		if parent[i] != i:
			parent[i] = self.find(parent, parent[i])
		return parent[i]
	def union(self, parent, rank, x, y):
		if rank[x] < rank[y]:
			parent[x] = y
		elif rank[x] > rank[y]:
			parent[y] = x		
		else:
			parent[y] = x 
			rank[x] += 1
	def KruskalMST(self):
		result = []		
		i = 0		
		e = 0
		self.graph = sorted(self.graph,
							key=lambda item: item[2])

		parent = []
		rank = []		
		for node in range(self.V):
			parent.append(node)
			rank.append(0)		
		while e < self.V - 1:		
			u, v, w = self.graph[i] 
			
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union (parent, rank, x, y)
		minimumCost = 0
		print("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree", minimumCost)
# Driver code
if __name__ == '__main__':
	g = Graph(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)

	# Function call
	g.KruskalMST()




# The code you provided implements Kruskal's algorithm in Python for finding the minimum spanning tree of a graph. Kruskal's algorithm works by sorting the edges of the graph in ascending order of their weights and adding them to the minimum spanning tree if they do not create a cycle.

# Here's a breakdown of the code:

# - The `Graph` class is defined, which initializes the number of vertices (`V`) and an empty list to store the graph's edges (`graph`).
# - The `addEdge` method is used to add edges to the graph. Each edge is represented by a tuple containing the source vertex, destination vertex, and weight.
# - The `find` method implements the find operation of the disjoint set data structure. It recursively finds the parent of a vertex and performs path compression to optimize future find operations.
# - The `union` method performs the union operation of the disjoint set data structure. It combines two disjoint sets by their ranks, ensuring that the tree remains balanced.
# - The `KruskalMST` method is the main function that implements Kruskal's algorithm. It initializes an empty list `result` to store the edges of the minimum spanning tree.
# - The edges in `graph` are sorted in ascending order of their weights using a lambda function as the key for sorting.
# - Disjoint set arrays `parent` and `rank` are created to keep track of the subsets and their ranks.
# - The algorithm iterates through the sorted edges. For each edge, it checks if adding it to the result will create a cycle. If not, the edge is added to the result, and the disjoint sets of the endpoints are unioned.
# - The total cost of the minimum spanning tree is computed by summing the weights of the edges in `result`.
# - Finally, the minimum spanning tree's edges and total cost are printed.

# In the `if __name__ == '__main__':` block, a `Graph` object `g` is created with 4 vertices. Edges are added to `g` using the `addEdge` method.
# Then, the `KruskalMST` method is called to find the minimum spanning tree.

# If you have any specific questions or need further clarification, feel free to ask!