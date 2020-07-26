from collections import defaultdict

class AdjMatrixGraph:
    def __init__(self, vertices):
        self.adj = [[False for _ in range(vertices)] for _ in range(vertices)]
        print(self.adj)

    def addEdge(self, i, j):
        self.adj[i][j] = True

    def removeEdge(i, j):
        self.adj[i][j] = False

    def hasEdge(i, j):
        return self.adj[i][j]
    

class AdjListGraph:
    def __init__(self, vertices):
        self.adj = defaultdict(list)
        self.size = vertices

    def addEdge(self, i, j):
        self.adj[i].append(j)

    def removeEdge(self, i, j):
        for k in range(len(self.adj[i])):
                if self.adj[i][k] == j:
                    del self.adj[i][k]
                    return

    def hasEdge(self, i, j):
        for k in self.adj[i]:
            if k == j:
                return True
        return False

    def outEdge(self, i):
        return self.adj[i]

    def inEdges(self, i):
        out = []
        for j in range(len(vertices)):
            if self.hasEdge(j, i):
                out.append(j)
        return out
    def __len__(self):
        return self.size

class Search:
    def BFS(self, graph, route):
        seen = [False] * (len(graph)+1)
        queue = []
        queue.append(route)
        seen[route] = True

        while len(queue) > 0:
            node = queue.pop()
            for edge in graph.outEdge(node):
                if seen[edge] == False:
                    queue.insert(0, edge)
                    seen[edge] = True
        print(seen)

    def DFS(self, graph, route):
        colour = ["white"] * (len(graph)+1)
        stack = [route]
        while len(stack) > 0:
            node = stack.pop()
            if colour[node] == "white":
                colour[node] = "grey"
                for neighbour in graph.outEdge(node):
                    stack.append(neighbour)
        print(colour)


if __name__ == '__main__':
    Graph = AdjListGraph(4)
    Graph.addEdge(1,3)
    Graph.addEdge(1,4)
    Graph.addEdge(2,1)
    Graph.addEdge(2,2)
    Graph.addEdge(0,3)
    Graph.addEdge(0,1)
    Graph.addEdge(3,2)
    search = Search()
    search.BFS(Graph, 1)
    search.DFS(Graph, 1)
