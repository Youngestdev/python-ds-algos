# Kosaraju's Algorithm to find strongly connected components in Python

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    # Add edge into the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Depth First Search
    def DFS(self, v, visited):
        visited[v] = True
        print(v, end='')
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i, visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    # Transpose the Graph
    def Transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # Print strongly connected components
    def printSCC(self):
        stack = []
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.fillOrder(i, visited, stack)

        gr = self.Transpose()

        visited = [False] * self.V

        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.DFS(i, visited)
                print("")

class GraphAdjMatrix:
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges into the graph
    def addEdges(self, v1, v2):
        if v1 == v2:
            print("Same vertext %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    # Return length.
    def __len__(self):
        return self.size

    # Print the matrix
    def toString(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val)),
            print

graph = GraphAdjMatrix(4)
graph.addEdges(0, 1)
graph.addEdges(0, 2)
graph.addEdges(1, 2)
graph.addEdges(2, 0)

graph.toString()

# graph.Transpose()
# graph.printValues()
