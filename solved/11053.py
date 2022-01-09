import sys
n=int(sys.stdin.readline())
board=[0]+list(map(int,sys.stdin.readline().split()))
dp=[0 for _ in range(n+1)]
result=0
for i1 in range(1,n+1):
    if i1==1:
        dp[i1]=1
    else:
        tmpresult=-1
        for i2 in range(1,i1):
            if board[i1]>board[i2] and tmpresult<dp[i2]:
                tmpresult=dp[i2]
        dp[i1]=tmpresult+1 if tmpresult!=-1 else 1
    result=max(result, dp[i1])
print(result)