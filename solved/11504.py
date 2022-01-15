import sys
result=1
n=int(sys.stdin.readline())
board=list(map(int,sys.stdin.readline().split()))
dp=[]
for i1,v1 in enumerate(board):
    if i1==0:
        dp.append([1,1])
        continue
    up,down=-1,-1
    for i2 in range(0,i1):
        if board[i2]<board[i1]:
            up=max(up,dp[i2][0])
        elif board[i2]>board[i1]:
            down=max(down,max(dp[i2][0],dp[i2][1]))
        else:
            pass
    if up==-1:
        up=0
    if down==-1:
        down=0
    result=max(result,max(up+1,down+1))
    dp.append([up+1,down+1])
print(result)