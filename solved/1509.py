import sys
def check(i,j,dp):
    dp[i][i]=True
    if i!=j:
        if string[i]==string[j]:
            dp[i][j]=True
        else:
            return
    i,j=i-1,j+1
    while 0<=i and j<len(dp):
        if string[i]==string[j]:
            dp[i][j]=True
            i,j=i-1,j+1
        else:
            break
    return
string=sys.stdin.readline().rstrip()
dp=[[False for _ in range(len(string))]for _ in range(len(string))]
for i1 in range(len(string)-1):
    check(i1,i1,dp)
    check(i1,i1+1,dp)
check(len(string)-1,len(string)-1,dp)
dp2=[0]+[2<<30 for _ in range(len(string))]
for i2 in range(len(string)):
    for i1 in range(i2+1):
        if dp[i1][i2]:
            dp2[i2+1]=min(dp2[i1]+1,dp2[i2+1])
print(dp2[-1])