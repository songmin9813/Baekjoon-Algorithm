import sys
def floyd(board, n):
    for middle in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if board[start][end]>board[start][middle]+board[middle][end]:
                    board[start][end]=board[start][middle]+board[middle][end]
                    if start==end and board[start][end]<0:
                        return True
    return False
tc=int(sys.stdin.readline())
for _ in range(tc):
    n,m,w=map(int, sys.stdin.readline().split())
    board=[[2<<30 for _ in range(n+1)]for _ in range(n+1)]
    for __ in range(m):
        x,y,d=map(int,sys.stdin.readline().split())
        board[x][y]=min(board[x][y],d)
        board[y][x]=min(board[y][x],d)
    for __ in range(w):
        x,y,d=map(int,sys.stdin.readline().split())
        board[x][y]=min(board[x][y],-d)
    floyd(board,n)
    flag=False
    print('YES') if floyd(board, n) else print('NO')