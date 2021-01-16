import sys
sys.setrecursionlimit(10**6)

def preorder(node):
    if node != '.':
        print(node, end = '')
        preorder(tree[node][0])
        preorder(tree[node][1])
    if node == 'A':
        print()

def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end = '')
        inorder(tree[node][1])
    if node == 'A':
        print()         
    
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end = '')
    if node == 'A':
        print()          

n = int(sys.stdin.readline().strip())
tree = {}

for _ in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

preorder('A')
inorder('A')
postorder('A')
