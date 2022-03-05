import sys
import heapq
def dijk():
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  dist=[[2<<30 for _ in range(m)]for _ in range(n)]
  dist[0][0]=int(board[0][0])
  queue=[]
  heapq.heappush(queue,[dist[0][0],0,0])
  while queue:
    cdist,x,y=heapq.heappop(queue)
    if cdist>dist[x][y]:
      continue
    for i in range(4):
      newX=dx[i]+x
      newY=dy[i]+y
      if 0<=newX<n and 0<=newY<m:
        tmpdist=cdist+board[newX][newY]
        if tmpdist<dist[newX][newY]:
          dist[newX][newY]=tmpdist
          heapq.heappush(queue,[tmpdist,newX,newY])
  return dist
m,n=map(int,sys.stdin.readline().split())
board=[list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
result=dijk()
print(result[n-1][m-1])