import sys
def checking(board,x,y):
    global result,n,m
    listX=[[x,x,x,x],[x,x+1,x+2,x+3],[x,x,x+1,x+1],[x,x,x-1,x-2],[x,x-1,x-1,x-1],[x,x,x+1,x+2],[x,x+1,x+1,x+1],[x,x,x-1,x-2],[x,x+1,x+1,x+1],[x,x,x+1,x+2],[x,x-1,x-1,x-1],
    [x,x+1,x+1,x+2],[x,x,x-1,x-1],[x,x+1,x+1,x+2],[x,x,x-1,x-1],[x,x,x,x+1],[x,x+1,x+1,x+2],[x,x,x-1,x],[x,x+1,x+1,x+2]]
    listY=[[y,y+1,y+2,y+3],[y,y,y,y],[y,y+1,y,y+1],[y,y-1,y-1,y-1],[y,y,y+1,y+2],[y,y+1,y+1,y+1],[y,y,y-1,y-2],[y,y+1,y+1,y+1],[y,y,y+1,y+2],[y,y-1,y-1,y-1],[y,y,y-1,y-2],
    [y,y,y+1,y+1],[y,y+1,y+1,y+2],[y,y,y-1,y-1],[y,y-1,y-1,y-2],[y,y+1,y+2,y+1],[y,y,y-1,y],[y,y+1,y+1,y+2],[y,y,y+1,y]]
    for i in range(19):
        newX=listX[i]
        newY=listY[i]
        flag=True
        tmpresult=0
        for i1 in range(4):
            if not(0<=newX[i1]<n) or not(0<=newY[i1]<m):
                flag=False
                break#하나라도 밖으로 나오면 아웃
            tmpresult+=board[newX[i1]][newY[i1]]
        if flag:#전부 확인과정 거침
            result=max(result, tmpresult)
n,m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result=0
for i1 in range(n):
    for i2 in range(m):
        checking(board,i1,i2)
print(result)