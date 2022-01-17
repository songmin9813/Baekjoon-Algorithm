import sys
def backtracking(length, visited, list_):
    if length==m:
        string=''
        for i,v in enumerate(list_):
            end=' 'if i!=len(list_)-1 else '\n'
            string=string+str(v)+end
        dict_[string]=True
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            list_.append(board[i])
            backtracking(length+1, visited, list_)
            list_.pop()
            visited[i]=False
    return
n,m=map(int, sys.stdin.readline().split())
board=list(map(int, sys.stdin.readline().split()))
board.sort()
visited=[False for _ in range(n)]
dict_={}
backtracking(0,visited,[])
for v in dict_.keys():
    print(v,end='')