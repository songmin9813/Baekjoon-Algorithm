import sys
n,m=map(int, sys.stdin.readline().split())
resultup,resultdown,result=1,1,1
if n!=m:
    for num in range(n-m+1,n+1):
        resultup*=num
    for num in range(1,m+1):
        resultdown*=num
    result=resultup//resultdown
else:
    result=1
print(result)