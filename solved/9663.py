import sys
#대각선을 일일이 검색하는 것이 아니라 대각선또한 2*n-1개의 크기를 가지는 1차원 위치 배열로 사용이 가능하다
#이런 생각하는 사람은 천재가 아닐까...
def backtracking(i1):
    if i1==n:
        global result
        result+=1
        return
    for i2 in range(n):
        if col[i2] and dia1[i1+i2] and dia2[i1-i2+n-1]:
            col[i2],dia1[i1+i2],dia2[i1-i2+n-1]=False,False,False
            backtracking(i1+1)
            col[i2],dia1[i1+i2],dia2[i1-i2+n-1]=True,True,True
    return
n=int(sys.stdin.readline())
col=[True for _ in range(n)]
dia1=[True for _ in range(2*n-1)]
dia2=[True for _ in range(2*n-1)]
result=0
for i2 in range(n//2):
    col[i2],dia1[i2],dia2[-i2+n-1]=False,False,False
    backtracking(1)
    col[i2],dia1[i2],dia2[-i2+n-1]=True,True,True
result*=2
if n%2==1:
    i2=n//2
    col[i2],dia1[i2],dia2[-i2+n-1]=False,False,False
    backtracking(1)
    col[i2],dia1[i2],dia2[-i2+n-1]=True,True,True
print(result)