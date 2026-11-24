from collections import deque

class Node:
    def __init__(self, x):
        self.data, self.left, self.right = x, None, None

def insert(r, x):
    if not r:
        return Node(x)
    if x < r.data:
        r.left = insert(r.left, x)
    elif x > r.data:
        r.right = insert(r.right, x)
    return r

def display(r):
    if not r:
        print("BST is empty.")
        return
    q = deque([r])
    while q:
        print("Level:", end=" ")
        for i in range(len(q)):
            n = q.popleft()
            print(n.data, end=" ")
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        print()

def copy(r):
    if not r:
        return None
    n = Node(r.data)
    n.left, n.right = copy(r.left), copy(r.right)
    return n

def height(r):
    return 0 if not r else 1 + max(height(r.left), height(r.right))

def leaves(r):
    if r:
        if not r.left and not r.right:
            print(r.data, end=" ")
        else:
            leaves(r.left)
            leaves(r.right)

root = None
n = int(input("Enter number of nodes: "))
for i in range(n):
    root = insert(root, int(input(f"Enter value {i+1}: ")))

print("\nOriginal BST\nLevel-Wise BST:")
display(root)

new = copy(root)
print("\nNew BST created successfully.")
print("\nNew BST\nLevel-Wise BST:")
display(new)

print("\nHeight of BST =", height(root))
print("\nLeaf Nodes:", end=" ")
leaves(root)
print()