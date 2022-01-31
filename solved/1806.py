import sys
n,m=map(int, sys.stdin.readline().split())
board=list(map(int,sys.stdin.readline().split()))
result=100001
tmp=0
for i,v in enumerate(board):
    tmp+=v
    board[i]=tmp
board=[0]+board
i,j=0,0
while i!=len(board) or j!=len(board)-1:
    tmp=board[j]-board[i]
    if tmp>=m:
        result=min(result,j-i)
        i+=1
    else:
        if j!=len(board)-1:
            j+=1
        else:
            i+=1
print(result) if result!=100001 else print(0)