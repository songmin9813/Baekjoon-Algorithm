import sys
def find(x):
    if x!=root[x]:
        root[x]=find(root[x])
    return root[x]

def union(a,x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        if a==0:
            root[y]=x
        else:
            print("NO")
    elif a==1:
        print("YES")

n,m=map(int,sys.stdin.readline().split())
root=[i for i in range(n+1)]
for _ in range(m):
    a,x,y=map(int,sys.stdin.readline().split())
    union(a,x,y)