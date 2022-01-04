import sys
def preorder(root):
    global result
    if root != '.':
        print(root,end=' ')
        preorder(tree[root][0])
        preorder(tree[root][1])

def sort(inorder,postorder):
    cindex=inorder.index(postorder[-1])
    left,right=inorder[:cindex],inorder[cindex+1:]
    if len(left)==1:
        tree[inorder[cindex]][0]=left[0]
    elif len(left)>=2:
        tree[inorder[cindex]][0]=postorder[:cindex][-1]
        sort(inorder[:cindex],postorder[:cindex])
    if len(right)==1:
        tree[inorder[cindex]][1]=right[0]
    elif len(right)>=2:
        tree[inorder[cindex]][1]=postorder[cindex+1:][-2]
        sort(inorder[cindex+1:],postorder[cindex+1:-1])
    #for i in range(-2, -len(right)-2, -1):
        #if cindex<inorder.index(postorder[i]):
            #tree[inorder[cindex]][1]=postorder[i]
        #else:
            #tree[inorder[(inorder.index(postorder[i]))+1]][0]=postorder[i]
        #cindex=inorder.index(postorder[i])
    return

n=int(sys.stdin.readline())
inorder=list(map(int, sys.stdin.readline().split()))
postorder=list(map(int,sys.stdin.readline().split()))
tree=[['.','.']for _ in range(n+2)]
sort(inorder,postorder)
preorder(postorder[-1])