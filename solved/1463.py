n=int(input())
dp=[0 for i in range(n+1)]
for i in range(1,n+1):
    if i==1:
        dp[i]=0
    elif i==2 or i==3:#초기세팅
        dp[i]=1
    elif i%2==0 and i%3==0:#6의 배수인 경우 모두 계산해주어야 함
        dp[i]=min(dp[i-1]+1,min(dp[i//2]+1,dp[i//3]+1))
    elif i%2==0:
        dp[i]=min(dp[i-1]+1,dp[i//2]+1)
    elif i%3==0:
        dp[i]=min(dp[i-1]+1,dp[i//3]+1)
    else:
        dp[i]=dp[i-1]+1
print(dp[n]) 