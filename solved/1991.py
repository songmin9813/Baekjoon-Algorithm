import sys
def preorder(root):
    global results
    if root != '.':
        results[0].append(root)
        preorder(tree[root][0])
        preorder(tree[root][1])
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        results[1].append(root)
        inorder(tree[root][1])
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        results[2].append(root)

n = int(sys.stdin.readline().strip())
tree = {}
for n in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
results=[[],[],[]]
preorder('A')
inorder('A')
postorder('A')
print(''.join(results[0])+'\n'+''.join(results[1])+'\n'+''.join(results[2]))