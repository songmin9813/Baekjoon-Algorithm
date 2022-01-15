import sys
result=1
n=int(sys.stdin.readline())
board=list(map(int,sys.stdin.readline().split()))
dp=[]
for i1,v1 in enumerate(board):
    if i1==0:
        dp.append([1,1])#해당수로 올라가는 수인지, 내려가는 수인지 각각을 저장할 필요가 있었음
        continue
    up,down=-1,-1
    for i2 in range(0,i1):
        if board[i2]<board[i1]:
            up=max(up,dp[i2][0])#올라가는 경우 올라가는 수만 확인
        elif board[i2]>board[i1]:
            down=max(down,max(dp[i2][0],dp[i2][1]))#내려가는 경우 내려가는 경우 외에도 정점을 찍고 내려가는 경우가 생김
        else:
            pass
    if up==-1:
        up=0
    if down==-1:
        down=0
    result=max(result,max(up+1,down+1))
    dp.append([up+1,down+1])
print(result)