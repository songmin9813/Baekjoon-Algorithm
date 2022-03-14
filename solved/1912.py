import sys
n=int(sys.stdin.readline())
list_=list(map(int,sys.stdin.readline().split()))
dp=list_.copy()
for i in range(1,len(dp)):
    dp[i]=max(dp[i-1]+dp[i],dp[i])
print(max(dp))