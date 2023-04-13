import sys
import heapq
def dijk():
    dist=[2<<30 for _ in range(n+1)]
    dist[x]=0
    queue=[[0,x]]
    while queue:
        cd,cy=heapq.heappop(queue)
        if dist[cy]<cd:
            continue
        for next_node in city[cy]:
            new_dist=cd+1
            if dist[next_node]>new_dist:
                dist[next_node]=new_dist
                heapq.heappush(queue,[new_dist,next_node])
    return dist
    
n,m,k,x=map(int, sys.stdin.readline().split())
city=[[]for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    city[a].append(b)
dist_infos=dijk()
count=0
for i,value in enumerate(dist_infos):
    if value==k:
        count+=1
        print(i)
if count==0:
    print(-1)