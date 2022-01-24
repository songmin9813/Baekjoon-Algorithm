import sys
def find(x):
    tmp=root[x]#기존 find 부분을 반복문으로 바꿔준 형태
    while tmp!=root[tmp]:
        tmp=root[tmp]
    return tmp
def union(x,y,d):
    x=find(x)
    y=find(y)
    if x!=y:#이미 같은 곳을 보고 있다=사전에 이미 union됨=이거 넣으면 사이클임
        global result,count
        root[y]=x
        result+=d
        count-=1#정점의 개수를 충족한다면 더이상 안 해도 됨
v,e=map(int,sys.stdin.readline().split())
result,count=0,v-1
edges=[list(map(int,sys.stdin.readline().split()))for _ in range(e)]
root=[i for i in range(v+1)]
edges.sort(key=lambda x:x[2])
for x,y,d in edges:
    union(x,y,d)
    if count==0:#남은 정점의 수 판단(속도 향상)
        break
print(result)