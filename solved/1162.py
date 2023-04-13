import sys
import heapq
def dijk():
    dist=[[sys.maxsize for _ in range(k+1)]for _ in range(n+1)]
    dist[1][0]=0
    queue=[[0,1,0]] # 거리 도시 포장수
    while queue:
        cd,cy,ksum=heapq.heappop(queue)
        if dist[cy][ksum]<cd:
            continue
        for n_node,n_dist in nodes[cy]:
            new_dist=cd+n_dist
            if new_dist<dist[n_node][ksum]:
                dist[n_node][ksum]=new_dist
                heapq.heappush(queue,[new_dist, n_node, ksum])
            if ksum<k and cd<dist[n_node][ksum+1]:
                dist[n_node][ksum+1]=cd
                heapq.heappush(queue,[cd, n_node, ksum+1])
    return min(dist[n])

n,m,k=map(int,sys.stdin.readline().split())
nodes=[[]for _ in range(n+1)]
for _ in range(m):
    x,y,d=map(int,sys.stdin.readline().split())
    nodes[x].append([y,d])
    nodes[y].append([x,d])
print(dijk())