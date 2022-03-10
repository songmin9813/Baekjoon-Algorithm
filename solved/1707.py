import sys
from collections import deque
def bfs():
    visited={i:0 for i in range(1,v+1)}
    queue=deque()
    for i in range(1,v+1):#비연결 그래프인 경우 모든 노드에 대해서 검사하여야 함
        #연결 그래프임이 보장된다면 위의 for문은 스킵 가능
        queue.append(i)
        while queue:
            cv=queue.popleft()
            if visited[cv]==0:
                visited[cv]=1
            for nv in nodes[cv]:
                if visited[nv]==0:
                    if visited[cv]==1:
                        visited[nv]=-1
                    else:
                        visited[nv]=1
                    queue.append(nv)
                else:
                    if (visited[cv]==1 and visited[nv]==1) or (visited[nv]==-1 and visited[cv]==-1):
                        return "NO"
    return "YES"
tc=int(sys.stdin.readline())
for _ in range(tc):
    v,e=map(int,sys.stdin.readline().split())
    nodes=[[]for _ in range(v+1)]
    for _ in range(e):
        x,y=map(int,sys.stdin.readline().split())
        nodes[x].append(y)
        nodes[y].append(x)
    print(bfs())