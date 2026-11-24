class Graph:
    def create(self):
        self.n = int(input("Enter number of intersections: "))

        if not 1 <= self.n <= 20:
            print("Invalid number of vertices.")
            self.n = 0
            return

        self.a = [[0]*self.n for i in range(self.n)]
        e = int(input("Enter number of roads: "))
        print("\nEnter roads (source destination):")

        for i in range(e):
            u, v = map(int, input(f"Road {i+1}: ").split())
            if 0 <= u < self.n and 0 <= v < self.n:
                self.a[u][v] = self.a[v][u] = 1
            else:
                print("Invalid intersection number.")
                return

        print("\nRoad network created successfully.")

    def display(self):
        if self.n == 0:
            print("\nGraph is not created.")
            return

        print("\nAdjacency Matrix:\n")
        print("  ", *range(self.n))
        for i in range(self.n):
            print(i, *self.a[i])

    def dfs(self, start):
        if self.n == 0:
            print("\nGraph is not created.")
            return
        if not 0 <= start < self.n:
            print("\nInvalid starting vertex.")
            return

        s = [start]
        visited = [0]*self.n
        print("\nDFS Traversal:", end=" ")

        while s:
            u = s.pop()
            if not visited[u]:
                print(u, end=" ")
                visited[u] = 1
                for v in range(self.n-1, -1, -1):
                    if self.a[u][v] and not visited[v]:
                        s.append(v)
        print()

g = Graph()
g.create()
g.display()
start = int(input("\nEnter starting intersection for DFS: "))
g.dfs(start)