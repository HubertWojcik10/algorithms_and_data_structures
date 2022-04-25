from itu.algs4.graphs import edge_weighted_graph
from itu.algs4.graphs import edge
from itu.algs4.fundamentals.queue import Queue

'''
This is my solution to the Kattis Harmony and Conflict problem (week 8). 
The problem is to check whether a graph G is harmonic. 

In week 7/8, we learned about dfs, bfs, shortest paths, etc. I used knowledge acquired during these lessons to solve this problem.
'''

def bfs(G, s):
    marked = [False for _ in range(G.V())]
    colored = [False for _ in range(G.V())]
    marked[s] = True
    colored[s] = True

    node_queue = Queue()
    node_queue.enqueue(s)

    while not node_queue.is_empty():
        curr = node_queue.dequeue() #current node

        for x in G.adj(curr):
            neigh = x.other(curr) #neighbor of current node
            weight = x.weight() #weight of edge between current and neighbor

            if not marked[neigh]:
                if weight == 1: colored[neigh] = not colored[curr]
                else: colored[neigh] = colored[curr]

                marked[neigh] = True
                node_queue.enqueue(neigh)
            else:
                #if neighbor is marked then we just need to verify
                if weight == 1 and colored[neigh] == colored[curr]: 
                    return 0
                if weight == 0 and colored[neigh] != colored[curr]: 
                    return 0

    return 1




n, m = input().split(' ')
n, m = int(n), int(m)

G = edge_weighted_graph.EdgeWeightedGraph(n)

for _ in range(m):
    u, v, c = [int(i) for i in input().split(' ')]
    E = edge.Edge(u, v, c)
    G.add_edge(E)

#the main function
print(bfs(G, 0))



