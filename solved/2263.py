import sys
sys.setrecursionlimit(10**5)
def sort(inS,inE,postS,postE):
    global inorder,postorder
    if postS<=postE:
        print(postorder[postE],end=' ')
        for i in range(n):
            if inorder[i]==postorder[postE]:
                rootindex=i
                break
        sort(inS,rootindex,postS,postS+(rootindex-1-inS))
        sort(rootindex+1,inE,postS+(rootindex-inS),postE-1)
    return

n=int(sys.stdin.readline())
inorder=list(map(int, sys.stdin.readline().split()))
postorder=list(map(int,sys.stdin.readline().split()))
sort(0,n-1,0,n-1)