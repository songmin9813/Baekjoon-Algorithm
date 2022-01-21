import sys
def bellman():
    dist=[2<<30 for _ in range(n+1)]
    dist[1]=0
    for _ in range(n):
        updated=False
        for i in range(m):
            x,y,cdist=edges[i]
            if dist[x]==2<<30:
                continue
            if dist[y]>dist[x]+cdist:
                updated=True
                dist[y]=dist[x]+cdist
    return updated, dist
n,m=map(int,sys.stdin.readline().split())
edges=[list(map(int,sys.stdin.readline().split()))for _ in range(m)]
flag, dist=bellman()
if not flag:
    for i in range(2,n+1):
        print(dist[i]) if dist[i]!=2<<30 else print(-1)
else:
    print(-1)