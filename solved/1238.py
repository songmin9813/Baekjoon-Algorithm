import sys
def findkey(dict_,dist):
    result=0
    for i in dict_.keys():
        if dist[result]>dist[i]:
            result=i
    return result

def dijk(board,n,start):
    dist=[2<<30 for _ in range(n+1)]
    dist[start]=0
    for value in board[start]:
        dist[value[1]]=value[0]
    visited={i:False for i in range(1,n+1)}
    del visited[start]
    for _ in range(n-1):
        cnode=findkey(visited,dist)
        del visited[cnode]
        for value in board[cnode]:
            cost=dist[cnode]+value[0]
            if cost<dist[value[1]]:
                dist[value[1]]=cost
    return dist

n,m,x=map(int,sys.stdin.readline().split())
board=[[]for _ in range(n+1)]
dist=[[]for _ in range(n+1)]
for _ in range(m):
    start,end,d=map(int,sys.stdin.readline().split())
    board[start].append([d,end])#거리, 인접노드
resultboard=[[2<<30 for _ in range(n+1)]]
for i in range(1,n+1):
    resultboard.append(dijk(board,n,i))
result=resultboard[1][x]+resultboard[x][1]
for i in range(2,n+1):
    if result<resultboard[i][x]+resultboard[x][i]:
        result=resultboard[i][x]+resultboard[x][i]
print(result)