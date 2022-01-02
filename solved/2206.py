import sys
from collections import deque
def bfswall(board):
    global n,m
    queue=deque()
    queue.append([0,0,1])
    dist=[[[0]*2 for _ in range(m)] for _ in range(n)]
    dist[0][0][1]=1#1이 뚫은 상태/0이 안뚫은상태
    while queue:
        l=len(queue)
        for _ in range(l):
            cx,cy,breakable=queue.popleft()
            if cx==n-1 and cy==m-1:
                return dist[cx][cy][breakable]
            dx=[-1,0,0,1]
            dy=[0,-1,1,0]
            for i in range(4):
                newX,newY=dx[i]+cx,dy[i]+cy
                if 0<=newX<n and 0<=newY<m:
                    if board[newX][newY]==1 and breakable==1:
                        dist[newX][newY][0]=dist[cx][cy][1]+1
                        queue.append([newX,newY,0])
                    elif board[newX][newY]==0 and dist[newX][newY][breakable]==0:
                        dist[newX][newY][breakable]=dist[cx][cy][breakable]+1
                        queue.append([newX,newY,breakable])
    return -1
n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
print(bfswall(board))