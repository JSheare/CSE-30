# author: Jacob Shearer
# date:
# file:
# input:
# output:

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.value = 0  # :(

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        new_vert = Vertex(key)
        self.vertList.update({key: new_vert})
        self.numVertices += 1

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList.values()

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addVertex(f)

        if t not in self.vertList:
            self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def breadth_first_search(self, s):
        queue = [self.getVertex(s)]
        keys = []
        while len(queue) > 0:
            vertex = queue.pop()
            if vertex.id not in keys:
                keys.append(vertex.id)

            for connection in list(vertex.getConnections()):
                if connection.id in keys:
                    continue

                queue.insert(0, connection)

        return keys
    
    def depth_first_search(self):
        start = self.vertList[list(self.getVertices())[0]]
        keys = [start.id]

        def explore(vertex):
            if vertex.id not in keys:
                keys.append(vertex.id)

            for connection in list(vertex.getConnections()):
                if connection.id in keys:
                    continue

                explore(connection)

        for connection in list(start.getConnections()):
            explore(connection)

        return keys
    
    def DFS(self, vid, path):  # What is this supposed to do?
        pass


if __name__ == '__main__':

    g = Graph()
    for i in range(6):
        g.addVertex(i)
        
    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)

    for v in g:
        print(v)

    assert (g.getVertex(0) in g) is True
    assert (g.getVertex(6) in g) is False
        
    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]


