import sys
def floyd():
    global dist
    for mid in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if dist[start][end]>dist[start][mid]+dist[mid][end]:
                    dist[start][end]=dist[start][mid]+dist[mid][end]
n,v=map(int,sys.stdin.readline().split())
dist=[[2<<30 for _ in range(n+1)]for _ in range(n+1)]
for _ in range(v):
    x,y=map(int,sys.stdin.readline().split())
    dist[x][y]=1
floyd()
result=0
for i1 in range(1,n+1):
    flag=True
    for i2 in range(1,n+1):
        if i1==i2:
            continue
        if dist[i1][i2]==2<<30 and dist[i2][i1]==2<<30:
            flag=False
            break
    if flag:
        result+=1
print(result)