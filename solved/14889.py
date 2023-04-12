import sys
def backtracking(length, index):
    global result
    if length==n//2:
        si=[i for i,value in enumerate(visited) if value]
        li=[i for i,value in enumerate(visited) if not value]
        star,link=0,0
        for i1 in range(n//2):
            for i2 in range(i1+1,n//2):
                star+=board[si[i1]][si[i2]]+board[si[i2]][si[i1]]
                link+=board[li[i1]][li[i2]]+board[li[i2]][li[i1]]
        result=min(result, abs(star-link))
        return
    for i in range(index, n):
        if not visited[i]:
            visited[i]=True
            backtracking(length+1, i)
            visited[i]=False

n=int(sys.stdin.readline())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result=2**31
visited=[False for _ in range(n)]
visited[0]=True
backtracking(1, 0)
print(result)