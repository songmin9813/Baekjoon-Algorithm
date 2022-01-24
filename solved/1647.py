import sys
def find(x):
    if root[x]!=x:
        root[x]=find(root[x])
    return root[x]
def union(x,y,d):
    x=find(x)
    y=find(y)
    if x!=y:
        global count,result,maxd
        count-=1
        result+=d
        maxd=max(maxd,d)
        root[y]=x
    return
n,m=map(int,sys.stdin.readline().split())
result,count,maxd=0,n-1,0
root=[i for i in range(n+1)]
edges=[list(map(int,sys.stdin.readline().split()))for _ in range(m)]
edges.sort(key=lambda x:x[2])
for x,y,d in edges:
    union(x,y,d)
    if count==0:
        break
print(result-maxd)