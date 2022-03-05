import sys
n=int(sys.stdin.readline())
board=[[[0]*4 for _ in range(10)]for _ in range(n)]
#[n][10][4]#계단수/자릿수/
for i in range(1,10):#0은 존재X
    if i==9:
        board[0][i][2]=1#9를만남
    else:
        board[0][i][0]=1
for i1 in range(1,n):
    for i2 in range(10):
        if i2==0:
            board[i1][i2][1]=(board[i1-1][i2+1][0]+board[i1-1][i2+1][1])%1000000000
            board[i1][i2][3]=(board[i1-1][i2+1][2]+board[i1-1][i2+1][3])%1000000000
        elif i2==9:
            board[i1][i2][2]=(board[i1-1][i2-1][0]+board[i1-1][i2-1][2])%1000000000
            board[i1][i2][3]=(board[i1-1][i2-1][1]+board[i1-1][i2-1][3])%1000000000
        else:
            for i3 in range(4):
                board[i1][i2][i3]=(board[i1-1][i2-1][i3]+board[i1-1][i2+1][i3])%1000000000
result=0
for i2 in range(10):
    result=(result+board[n-1][i2][3])%1000000000
print(result)