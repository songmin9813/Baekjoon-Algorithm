import sys
tc=int(sys.stdin.readline())
list_=[]
for _ in range(tc):
    list_.append(int(sys.stdin.readline()))
dp=list_.copy()
for i in range(1,len(list_)):
    if i==1:
        dp[i]+=dp[i-1]
    elif i==2:
        dp[i]=max(list_[i-1]+list_[i],list_[i-2]+list_[i],dp[i-1])
    else:
        dp[i]=max(dp[i-3]+list_[i-1]+list_[i],dp[i-2]+list_[i],dp[i-1])
print(dp[tc-1])