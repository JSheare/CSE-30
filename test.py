from graph import Graph
g = Graph()
for i in range(9):
    g.addVertex(i+1)

g.addEdge(1, 3)
g.addEdge(1, 4)

g.addEdge(2, 3)
g.addEdge(2, 5)
g.addEdge(2, 9)

g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(3, 9)

g.addEdge(4, 1)
g.addEdge(4, 5)
g.addEdge(4, 7)
g.addEdge(4, 9)

g.addEdge(5, 2)
g.addEdge(5, 4)
g.addEdge(5, 7)
g.addEdge(5, 9)

g.addEdge(6, 8)

g.addEdge(7, 4)
g.addEdge(7, 5)
g.addEdge(7, 8)

g.addEdge(8, 6)
g.addEdge(8, 7)

g.addEdge(9, 2)
g.addEdge(9, 3)
g.addEdge(9, 4)
g.addEdge(9, 5)

print(g.DFS(2, []))
print(g.breadth_first_search(2))





