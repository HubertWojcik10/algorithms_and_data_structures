from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, s):
		visited = [False] * (max(self.graph) + 1)

		queue = [] #the main queue used for bfs
		queue.append(s) #appending the root node
		visited[s] = True

		while queue:
			s = queue.pop(0) #dequeuing
			print(s)

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS(2) #2 as the root node

# Huge thank you to by Neelam Yadav, who created the code for bfs in Python
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
