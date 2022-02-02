import sys
def find(x):
    if x!=root[x]:
        root[x]=find(root[x])
    return root[x]
def union(x,y,d):
    x=find(x)
    y=find(y)
    if x!=y:
        global count,result
        root[y]=x
        count-=1
        result+=d
n=int(sys.stdin.readline())
board=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
root=[i for i in range(n)]
count=n
result=0
edge=[]
for i1,row in enumerate(board):
    for i2,v in enumerate(row):
        if i1==i2:
            continue
        edge.append([v,i1,i2])
edge.sort(key=lambda x:x[0])
for d,x,y in edge:
    union(x,y,d)
    if count==0:
        break
print(result)