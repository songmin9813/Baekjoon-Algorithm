import sys
n=int(sys.stdin.readline())
dp=list(map(int,sys.stdin.readline().split()))
for i in range(1,len(dp)):
    dp[i]=max(dp[i-1]+dp[i],dp[i])
print(max(dp))