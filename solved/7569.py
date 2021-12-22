from collections import deque
def naming(i1,i2,i3):
    return str(i1)+' '+str(i2)+' '+str(i3)
def bfs(currentq, nextq, board, visited,h,r,c):
    global tomato
    global flag
    while currentq:
        node=currentq.popleft()
        i1,i2,i3=node[0],node[1],node[2]
        dh=[1,0,0,0,0,-1]
        dr=[0,1,-1,0,0,0]
        dc=[0,0,0,1,-1,0]
        for i in range(6):
            newh=i1+dh[i]
            newr=i2+dr[i]
            newc=i3+dc[i]
            if newh>=0 and newh<h and newr>=0 and newr<r and newc>=0 and newc<c and naming(newh,newr,newc) not in visited.keys() and board[newh][newr][newc]==0:
                flag=True
                board[newh][newr][newc]=1
                tomato-=1
                nextq.append([newh,newr,newc])
                visited[naming(newh,newr,newc)]=True
col,row,height=map(int, input().split())
board=[]
for __ in range(height):
    tmp=[list(map(int,input().split())) for _ in range(row)]
    board.append(tmp)#board[층][행][열]로 저장함
flag=False
q1=deque()
q2=deque()
tomato=0#익어야 하는 도마도
visited={}
for i1,h in enumerate(board):
    for i2,r in enumerate(h):
        for i3,value in enumerate(r):
            if value==1:
                q1.append([i1,i2,i3])
                visited[naming(i1,i2,i3)]=True
            elif value==0:
                tomato+=1
day=0
while q1 or q2:
    flag=False
    if q1:#q1에 담겨있음 nextq가 q2가 됨
        bfs(q1,q2,board,visited,height,row,col)
    else:
        bfs(q2,q1,board,visited,height,row,col)
    if flag is False:
        if tomato!=0:#변화가 일어나지 않음. 도마도가 남음
            break
    else:
        flag=False
        day+=1
print(day) if tomato==0 else print(-1)