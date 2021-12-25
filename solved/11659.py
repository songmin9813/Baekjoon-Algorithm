import sys
n,m=map(int,sys.stdin.readline().split())
list_=list(map(int,sys.stdin.readline().split()))
sumlist=[0]
for i in range(n):#누적합리스트
    sumlist.append(sumlist[i]+list_[i])
result=''
for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    print(str(sumlist[j]-sumlist[i-1])