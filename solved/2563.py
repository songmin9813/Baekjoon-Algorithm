import sys
board=[[False for _ in range(100)]for _ in range(100)]
n=int(sys.stdin.readline())
for _ in range(n):
    x,y=map(int,sys.stdin.readline().split())
    x-=1
    y-=1
    for i1 in range(x,x+10):
        for i2 in range(y,y+10):
            board[i1][i2]=True
result=0
for values in board:
    result+=sum(values)
print(result)