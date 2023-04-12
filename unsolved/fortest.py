import sys

input=sys.stdin.readline

N=int(input())

graph=[list(map(int,input().split()))for _ in range(N)]
visitied=[False for _ in range(N)]
visitied[0]=True
result=int(1e9)

def dfs(i,depth):
    global result
    if depth==N//2:
        start_sum=0
        link_sum=0
        for i1 in range(N):
            for i2 in range(N):
                if visitied[i1] and visitied[i2]:
                    start_sum+=graph[i1][i2]
                elif not visitied[i1] and not visitied[i2]:
                    link_sum+=graph[i1][i2]
        result=min(result,abs(start_sum-link_sum))
        return

    for idx in range(i,N):
        if not visitied[idx]:
            visitied[idx]=True
            dfs(i+1,depth+1)
            visitied[idx]=False

dfs(0,1)
print(result)