import sys
from collections import deque
def finedust(board,dusts):
    queue=deque()
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    iter=dusts.keys()
    for i1,i2 in iter:
        count=0
        for i in range(4):
            newX=i1+dx[i]
            newY=i2+dy[i]
            if 0<=newX<r and 0<=newY<c and board[newX][newY]!=-1:
                count+=1
                queue.append([newX,newY,board[i1][i2]//5])
        board[i1][i2]-=(board[i1][i2]//5*count)
        dusts[(i1,i2)]=board[i1][i2]
    while queue:
        x,y,dust=queue.popleft()
        board[x][y]+=dust
        if board[x][y]!=0:
            dusts[(x,y)]=board[x][y]
    return
def air(board,dusts,puri):
    dx=[0,-1,0,1]#위 기준 0123
    dy=[1,0,-1,0]#아래 기준 0321
    queue=deque()
    queue.append([0,[puri[0][0],puri[0][1]+1],0,0])#tmp,위치정보,up/down,방향정보
    queue.append([0,[puri[1][0],puri[1][1]+1],1,0])
    while queue:
        tmp,points,updown,location=queue.popleft()
        newX=points[0]+dx[location]
        newY=points[1]+dy[location]
        if not (0<=newX<r and 0<=newY<c):
            if updown==0:
                location+=1
            else:
                location=location-1 if location!=0 else 3
            newX=points[0]+dx[location]
            newY=points[1]+dy[location]
        swap(board,dusts,puri,tmp,points,updown,location,[newX,newY],queue)
    return
def swap(board,dusts,puri,tmp,points,updown,location,newpoints,queue):
    if newpoints in puri:
        global result
        result-=board[points[0]][points[1]]
        board[points[0]][points[1]]=tmp
    else:
        queue.append([board[points[0]][points[1]],newpoints,updown,location])
        board[points[0]][points[1]]=tmp
    if board[points[0]][points[1]]!=0 and tmp==0:
        del dusts[(points[0],points[1])]
    elif tmp!=0:
        dusts[(points[0],points[1])]=tmp
r,c,t=map(int, sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split()))for _ in range(r)]
result,puri=0,[]
dusts={}
for i1,row in enumerate(board):
    for i2,value in enumerate(row):
        if value>0:
            dusts[(i1,i2)]=value
            result+=value
        elif value==-1:
            puri.append([i1,i2])
for _ in range(t):
    finedust(board,dusts)
    air(board,dusts,puri)
print(result)