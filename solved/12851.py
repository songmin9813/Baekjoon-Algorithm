import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
def bfs():
    length,count=0,0
    visited=[False for _ in range(200001)]
    queue=deque()
    queue.append([n,0])#초기/곱하기는 0, 1이면 플러스에서 옴(마이너스 금지). -1이면 마이너스에서 옴(플러스 금지)
    #현재 수를 확인한다음 방문체크를 해야하는 순서에 주의함
    l=len(queue)
    while queue:
        for _ in range(l):
            cnode, flag=queue.popleft()
            if cnode==m:
                count+=1
            visited[cnode]=True
            if cnode<m and not visited[2*cnode]:
                queue.append([2*cnode,0])
            if flag<=0:
                if flag==0 and cnode<m and not visited[cnode+1]:
                    queue.append([cnode+1,1])
                if cnode>0 and not visited[cnode-1]:
                    queue.append([cnode-1,-1])
            else:
                if cnode<m and not visited[cnode+1]:
                    queue.append([cnode+1,1])
        if count!=0:
            break
        l=len(queue)
        length+=1
    return length,count
result=bfs()
print(result[0])
print(result[1])