import sys
n,m=map(int,sys.stdin.readline().split())
board=list(map(int,sys.stdin.readline().split()))
board.sort(reverse=True)
stack,result=[[board[i]]for i in range(n)],{}
while stack:
    node=stack.pop()
    if len(node)==m:
        string=''
        for i,v in enumerate(node):
            end=' 'if i!=len(node)-1 else '\n'
            string=string+str(v)+end
        result[string]=True
        continue
    for v in board:
        if node[-1]<=v:
            repli=node.copy()
            repli.append(v)
            stack.append(repli)
for v in result.keys():
    print(v, end='')