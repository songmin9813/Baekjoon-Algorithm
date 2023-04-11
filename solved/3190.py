import sys
from collections import deque
def moving():
    second,rot_index=0,0
    snake=deque()
    snake.append([1,1])
    origin=[[0,1],[1,0],[0,-1],[-1,0]] # 우 하 좌 상
    D=[[1,0],[0,-1],[-1,0],[0,1]]
    L=[[-1,0],[0,1],[1,0],[0,-1]]
    while True:
        second+=1
        newX,newY=snake[-1][0]+origin[rot_index][0],snake[-1][1]+origin[rot_index][1]
        if not(0<newX<=n) or not(0<newY<=n):
            return second
        for sx,sy in snake:
            if newX==sx and newY==sy:
                return second
        snake.append([newX,newY])

        ate_apple=False
        for i,values in enumerate(apples):
            ax,ay=values
            if newX==ax and newY==ay and not applevisited[i]:
                ate_apple=True
                applevisited[i]=True
                break
        
        if not ate_apple:
            snake.popleft()
                
        if infos and int(infos[0][0])==second:
            if infos[0][1]=='D':
                rot_index = origin.index(D[rot_index])
            else:
                rot_index = origin.index(L[rot_index])
            infos.popleft()

n=int(sys.stdin.readline())
board=[[0 for _ in range(n+1)]for _ in range(n+1)]
k=int(sys.stdin.readline())
apples=[list(map(int,sys.stdin.readline().split()))for _ in range(k)]
applevisited=[False for _ in range(k)]
l=int(sys.stdin.readline())
infos=deque(list(map(str,sys.stdin.readline().split())) for _ in range(l))
print(moving())