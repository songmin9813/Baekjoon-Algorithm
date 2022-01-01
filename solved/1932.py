import sys
n=int(sys.stdin.readline())
dp=[]
for i1 in range(n):
    list_=list(map(int,sys.stdin.readline().split()))
    if i1!=0:
        for index,value in enumerate(list_):
            if index==0:
                list_[index]+=dp[i1-1][0]
            elif index==len(list_)-1:
                list_[index]+=dp[i1-1][-1]
            else:
                list_[index]=max(dp[i1-1][index-1]+list_[index],dp[i1-1][index]+list_[index])
    dp.append(list_)
print(max(dp[n-1]))