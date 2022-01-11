import sys
n,m=map(int,sys.stdin.readline().split())
board=[[0 for _ in range(n+1)]]
for _ in range(n):
    board.append([0]+list(map(int,sys.stdin.readline().split())))
for i1 in range(n+1):
    for i2 in range(n+1):
        if i2==0:
            continue
        board[i1][i2]+=board[i1][i2-1]
for _ in range(m):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    result=0
    for i1 in range(x1,x2+1):
        result+=board[i1][y2]-board[i1][y1-1]
    print(result)