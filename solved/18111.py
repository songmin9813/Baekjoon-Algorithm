n,m,b=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
minnum=min(map(min,board))
maxnum=max(map(max,board))
result=[]
for land in range(maxnum,minnum-1,-1):
    time=0
    cblock=b#사용가능 블럭
    tmpresult=land*n*m
    for row in board:
        for v in row:
            if v>land:#파야됨
                cblock+=(v-land)
                time+=2*(v-land)
            elif v<land:#추가해야됨
                cblock-=(land-v)
                time+=(land-v)
    if cblock>=0:#가용 인벤개수=만들 수 있음
        if len(result)==0:
            result.append(time)
            result.append(land)
        elif result[0]>time:
            result[0]=time
            result[1]=land
print(result[0],result[1])