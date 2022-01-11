import sys
from collections import deque
def bfs(start):
    visited=[False for _ in range(n+1)]
    result=[0 for _ in range(n+1)]
    result[start]=start
    queue=deque()
    queue.append(start)
    visited[start]=True
    while queue:
        cnode=queue.popleft()
        for next in trees[cnode]:
            if not visited[next]:
                result[next]=cnode
                visited[next]=True
                queue.append(next)
    return result
n=int(sys.stdin.readline())
trees=[[]for _ in range(n+1)]
for _ in range(n-1):
    x,y=map(int,sys.stdin.readline().split())
    trees[x].append(y)
    trees[y].append(x)
results=bfs(1)
for i in range(2,n+1):
    print(results[i])