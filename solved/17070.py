import sys
def solving():
    dp=[[[0,0,0]for _ in range(n+1)]for _ in range(n+1)]
    dp[1][2]=[1,0,0]
    for i1 in range(1,n+1):
        for i2 in range(3,n+1):
            if board[i1][i2]==1:
                continue
            dp[i1][i2][0]+=dp[i1][i2-1][0]+dp[i1][i2-1][1]
            if board[i1-1][i2]!=1 and board[i1][i2-1]!=1:
                dp[i1][i2][1]+=dp[i1-1][i2-1][0]+dp[i1-1][i2-1][1]+dp[i1-1][i2-1][2]
            dp[i1][i2][2]+=dp[i1-1][i2][2]+dp[i1-1][i2][1]
            #0:가로/1:대각선/2:세로
    return dp       
n=int(sys.stdin.readline())
board=[[0 for _ in range(n+1)]]
for _ in range(n):
    board.append([0]+list(map(int,sys.stdin.readline().split())))
result=solving()
print(sum(result[n][n]))