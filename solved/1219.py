import sys
def bellman():
    dist=[-2<<30 for _ in range(n)]
    dist[start]=values[start]
    for iter in range(n+100):
        #기존 사이클 감지가 아닌 충분한 relaxation과정을 통해 사이클 판별을 dist내에서 다룬다
        for x,y,cdist in edges:
            if dist[x]==-2<<30:
                continue
            elif dist[y]<dist[x]-cdist+values[y]:
                dist[y]=dist[x]-cdist+values[y]
                if iter>=n-1:#한번이라도 사이클 내에 도달한다면 무조건 무한의 값
                    dist[y]=2<<30
            elif dist[x]==2<<30:
                dist[y]=2<<30
    return dist
n,start,end,m=map(int,sys.stdin.readline().split())
edges=[list(map(int,sys.stdin.readline().split()))for _ in range(m)]
values=list(map(int,sys.stdin.readline().split()))
dist=bellman()
if dist[end]==2<<30:
    print('Gee')
elif dist[end]==-2<<30:
    print('gg')
else:
    print(dist[end])