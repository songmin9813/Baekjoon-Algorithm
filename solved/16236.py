import sys
from collections import deque
def bfs(shark,queue):
    global n,ate,board,visited,second
    visited[shark[0]][shark[1]]=True
    queue.append([shark[0],shark[1],0])
    iter=len(queue)
    candiate=[]
    while queue:
        for _ in range(iter):
            dx=[-1,0,0,1]
            dy=[0,-1,1,0]
            cx,cy,length=queue.popleft()
            for i in range(4):
                newX=dx[i]+cx
                newY=dy[i]+cy
                if 0<=newX<n and 0<=newY<n and shark[2]>=board[newX][newY] and not visited[newX][newY]:
                    visited[newX][newY]=True
                    if shark[2]>board[newX][newY]>0:#먹을 수 있음
                        candiate.append([newX,newY])
                        ate=True
                    else:
                        queue.append([newX,newY,length+1])
        if ate:#먹이중 가장 위+가장 왼쪽 좌표 찾아냄
            atefish=candiate[0]
            for i in range(1,len(candiate)):
                if (candiate[i][0]<atefish[0]) or (candiate[i][0]==atefish[0] and candiate[i][1]<atefish[1]):
                    atefish=candiate[i]
            board[shark[0]][shark[1]]=0
            shark[0],shark[1],shark[3],second=atefish[0],atefish[1],shark[3]+1,second+length+1
            if shark[2]==shark[3]:
                shark[2],shark[3]=shark[2]+1,0
            board[shark[0]][shark[1]]=9
            return ate
        iter=len(queue)
    return ate
n=int(sys.stdin.readline())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue=deque()
visited=[[False for _ in range(n)]for __ in range(n)]
ate=False
second=0
for i1 in range(n):
    for i2 in range(n):
        if board[i1][i2]==9:
            shark=[i1,i2,2,0]
while True:
    if not bfs(shark,queue):
        break
    else:#먹음. 초기화 진행
        queue.clear()
        visited=[[False for _ in range(n)]for __ in range(n)]
        ate=False
print(second)