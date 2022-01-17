import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
queue=deque()
depth,flag=1,False
queue.append(n)
while queue:
    l=len(queue)
    for _ in range(l):
        cnode=queue.popleft()
        if cnode==m:
            flag=True
            break
        numone=cnode*2
        numtwo=int(str(cnode)+'1')
        if numone<=m:
            queue.append(numone)
        if numtwo<=m:
            queue.append(numtwo)
    if flag:
        break
    depth+=1
print(depth) if flag else print(-1)