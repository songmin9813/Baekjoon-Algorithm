import sys
def floyd(dist, n):
    for middle in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if dist[start][end]>dist[start][middle]+dist[middle][end]:
                    dist[start][end]=dist[start][middle]+dist[middle][end]
                    if start==end and dist[start][end]<0:
                        return True
    return False
tc=int(sys.stdin.readline())
for _ in range(tc):
    n,m,w=map(int, sys.stdin.readline().split())
    dist=[[2<<30 for _ in range(n+1)]for _ in range(n+1)]
    for __ in range(m):
        x,y,d=map(int,sys.stdin.readline().split())
        dist[x][y]=min(dist[x][y],d)
        dist[y][x]=min(dist[y][x],d)
    for __ in range(w):
        x,y,d=map(int,sys.stdin.readline().split())
        dist[x][y]=min(dist[x][y],-d)
    floyd(dist,n)
    flag=False
    print('YES') if floyd(dist, n) else print('NO')