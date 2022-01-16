import sys
def backtracking(length,save,start):
    if length==m:
        for i,v in enumerate(save):
            string='\n' if i==len(save)-1 else ' '
            print(v,end=string)
        return
    for i1 in range(start,len(board)):
        save.append(board[i1])
        backtracking(length+1,save,i1)
        save.pop()
n,m=map(int,sys.stdin.readline().split())
board=list(range(1,n+1))
visited=[False for _ in range(n+2)]
backtracking(0,[],0)