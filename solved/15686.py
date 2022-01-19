import sys
def finding(start):
    stack=[[start]]
    while stack:
        cnode=stack.pop()
        if len(cnode)==m:
            global result
            result=min(result,cal(cnode))
            continue
        for i in range(cnode[-1]+1,len(chicken)):
            tmp=cnode.copy()
            tmp.append(i)
            stack.append(tmp)
def cal(chicken_):
    count=0
    for x1,y1 in house:
        result=2<<30
        for i in chicken_:
            x2,y2=chicken[i]
            result=min(result, abs(x1-x2)+abs(y1-y2))
        count+=result
    return count
n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
chicken,house=[],[]
result=2<<30
for i1,row in enumerate(board):
    for i2,value in enumerate(row):
        if value==1:
            house.append([i1,i2])
        elif value==2:
            chicken.append([i1,i2])
for start in range(len(chicken)):
    finding(start)
print(result)