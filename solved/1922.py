import sys
def find(x):
    if root[x]!=x:#find를 재귀적으로 구현하면서 수시로 저장해주어 추후의 연산 속도를 줄일 수 있다.
        root[x]=find(root[x])
    return root[x]
def union(x,y,d):
    x=find(x)
    y=find(y)
    if x!=y:
        global result, count
        root[y]=x
        result+=d
        count-=1
    return
n=int(sys.stdin.readline())
result,count=0,n-1
root=[i for i in range(n+1)]
m=int(sys.stdin.readline())
edges=[list(map(int,sys.stdin.readline().split()))for _ in range(m)]
edges.sort(key=lambda x:x[2])
for x,y,d in edges:
    union(x,y,d)
    if count==0:
        break
print(result)