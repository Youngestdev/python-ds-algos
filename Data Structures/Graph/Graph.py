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
        print("Graph value: ", self.graph)
        visited[v] = True
        print(v, end='\t')
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i, visited)
        print(visited)

    def BFS(self, root):
        visited, queue = set(), collections.deque([root])
        visited.add(queue)

        while queue:
            # Dequeue a vertex from Queue
            vertex = queue.popleft()
            print(str(vertex) + " ", end="")

        # If not visited, mark it as visited and enqueue it.
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

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

    def printGraph(self):
        for i in self.graph:
            print("Node {} :-> {}".format(i, self.graph[i]))


class GraphAdjMatrix:
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges into the graph
    def addEdges(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
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


class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class GraphAdjList:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Add edges
    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Print the graph
    def printGraph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


class WeightedGraph:
    def __init__(self, size):
        self.graph = defaultdict(list)
        self.size = size

    def addEdge(self, u, v, w):
        self.graph[u].append([v, [w]])

    def printGraph(self):
        for row in range(self.size):
            print("{}\t\t{}".format(row, self.graph[row]))

    def DFS(self, v, visited):
        print("Graph value: ", self.graph)
        visited[v] = True
        print(v, end="\n")
        for i in self.graph[v][:-1]:
            if not visited[i]:
                self.DFS(i, visited)
        print(visited)


graph = WeightedGraph(4)
graph.addEdge(0, 1, 4)
graph.addEdge(2, 2, 6)
graph.addEdge(1, 3, -1)
graph.addEdge(1, 2, 0)

_visited = [False] * graph.size

# graph.printGraph()
graph.DFS(2, _visited)
print("\n")

graph2 = Graph(4)
graph2.addEdge(0, 1)
graph2.addEdge(2, 2)
graph2.addEdge(1, 3)
graph2.addEdge(1, 2)
graph2.DFS(2, [False] * graph2.V)
print("\n")