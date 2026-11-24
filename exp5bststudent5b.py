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

def inorder(r):
    s = []
    while r or s:
        while r:
            s.append(r)
            r = r.left
        r = s.pop()
        print(r.data, end=" ")
        r = r.right
    print()

def preorder(r):
    if not r:
        return
    s = [r]
    while s:
        r = s.pop()
        print(r.data, end=" ")
        if r.right:
            s.append(r.right)
        if r.left:
            s.append(r.left)
    print()

root = None
n = int(input("Enter number of students: "))
for i in range(n):
    root = insert(root, int(input("Enter student roll number: ")))

print("Student Roll Numbers (Inorder): ", end="")
inorder(root)
print("Student Records (Preorder): ", end="")
preorder(root)