import sys
dp,n=[0,1],int(sys.stdin.readline())
for _ in range(2,n+1):
    dp.append(dp[-1]+dp[-2])
print(dp[n])