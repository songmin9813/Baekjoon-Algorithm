import sys
tc=int(sys.stdin.readline())
for _ in range(tc):
    m=int(sys.stdin.readline())
    board=[list(map(int,sys.stdin.readline().split()))for _ in range(2)]
    for i2 in range(1,m):
        for i1 in range(2):
            if i2==1:
                if i1==0:
                    board[i1][i2]+=board[i1+1][i2-1]
                else:
                    board[i1][i2]+=board[i1-1][i2-1]
            else:
                if i1==0:
                    board[i1][i2]+=max(board[i1+1][i2-1],board[i1+1][i2-2])
                else:
                    board[i1][i2]+=max(board[i1-1][i2-1],board[i1-1][i2-2])
    print(max(board[0][m-1],board[1][m-1]))