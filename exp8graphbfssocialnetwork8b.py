class Graph:
    def __init__(self, n):
        self.n = n
        self.a = [[] for i in range(n)]

    def add(self, u, v):
        self.a[u].insert(0, v)
        self.a[v].insert(0, u)

    def display(self):
        print("\nSocial Network Adjacency List:")
        for i in range(self.n):
            print(i, "->", *self.a[i])

    def bfs(self, start):
        visited = [0]*self.n
        q = [start]
        visited[start] = 1

        print("\nBFS Traversal:", end=" ")
        while q:
            u = q.pop(0)
            print(u, end=" ")
            for v in self.a[u]:
                if not visited[v]:
                    visited[v] = 1
                    q.append(v)
        print()

n = int(input("Enter number of users: "))
g = Graph(n)

e = int(input("Enter number of friendships: "))
print("Enter the friendships (user1 user2):")

for i in range(e):
    u, v = map(int, input(f"Friendship {i+1}: ").split())
    g.add(u, v)

g.display()
start = int(input("\nEnter starting user for BFS: "))
g.bfs(start)