import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
board=[-1 for _ in range(102)]
visited=[False for _ in range(102)]
ladder,snake={},{}
for _ in range(n):
    x,y=map(int,sys.stdin.readline().split())
    ladder[x]=y
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    snake[x]=y
board[1]=0
queue=deque()
queue.append(1)
visited[1]=True
while queue:
    current=queue.popleft()
    for i in range(1,7):
        newpos=current+i
        if newpos<101 and visited[newpos] is not True:
            if newpos in ladder.keys():#무조건 올라감
                newpos=ladder[newpos]
            elif newpos in snake.keys():#무조건 내려감
                newpos=snake[newpos]
            if visited[newpos] is not True or board[newpos]>board[current]+1:
                visited[newpos]=True
                board[newpos]=board[current]+1
                queue.append(newpos)
print(board[100])