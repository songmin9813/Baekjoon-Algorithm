import sys
def backtracking(length,save,visited):
    if length==m:
        for i,v in enumerate(save):
            string='\n' if i==len(save)-1 else ' '
            print(v,end=string)
        return
    for i1 in range(len(board)):
        if not visited[i1]:
            visited[i1]=True
            save.append(board[i1])
            backtracking(length+1,save,visited)
            save.pop()
            visited[i1]=False
n,m=map(int,sys.stdin.readline().split())
board=list(map(int,sys.stdin.readline().split()))
board.sort()
visited=[False for _ in range(n+2)]
backtracking(0,[],visited)