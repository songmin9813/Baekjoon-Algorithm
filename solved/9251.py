import sys
#부분수열이기 때문에 앞의 값들을 계속 뒤까지 끌어줘야 한다는 것에 유의한 dp문제
string1=sys.stdin.readline().rstrip()
string2=sys.stdin.readline().rstrip()
dp=[[0 for _ in range(len(string2)+1)]for _ in range(len(string1)+1)]
result=0
for i1,value1 in enumerate(string1):
    for i2,value2 in enumerate(string2):
        if value1==value2:#같은경우 단순 합 증가
            dp[i1+1][i2+1]=dp[i1][i2]+1
        else:#각 문자열별 최댓값을 끌어주어야 함
            dp[i1+1][i2+1]=max(dp[i1][i2+1],dp[i1+1][i2])
        result=max(result,dp[i1+1][i2+1])
print(result)