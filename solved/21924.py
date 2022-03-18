import sys
def find(x):
    if root[x]!=x:
        root[x]=find(root[x])
    return root[x]
def union(x,y,d):
    x=find(x)
    y=find(y)
    if x!=y:
        global count,result
        root[y]=x
        count-=1
        result+=d
n,m=map(int,sys.stdin.readline().split())
count,result,sum=n-1,0,0
edges=[]
root=[i for i in range(n+1)]
for _ in range(m):
    x,y,d=map(int,sys.stdin.readline().split())
    edges.append([x,y,d])
    sum+=d
edges.sort(key=lambda x:x[2])
for x,y,d in edges:
    union(x,y,d)
    if count==0:
        break
print(sum-result) if count==0 else print(-1)