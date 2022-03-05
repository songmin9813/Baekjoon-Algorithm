import sys
n=int(sys.stdin.readline())
dp=[[0 for _ in range(n+1)]for _ in range(2)]
for i2 in range(1,n+1):
    if i2==1:
        dp[0][i2]=0
        dp[1][i2]=1
    else:
        dp[0][i2]=dp[0][i2-1]+dp[1][i2-1]
        dp[1][i2]=dp[0][i2-1]
print(dp[0][n]+dp[1][n])