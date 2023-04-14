import sys
n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
tc=int(sys.stdin.readline())
for _ in range(tc):
    i,j,x,y=map(int,sys.stdin.readline().split())
    print(sum([sum(board[i1][j-1:y])for i1 in range(i-1,x)]))