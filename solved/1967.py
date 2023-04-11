import sys
def dfs(node):
    result=[0,0] # node, weight
    visited=[False for _ in range(n+1)]
    visited[node]=True
    stack=[[node,0]]
    while stack:
        cnode,cw=stack.pop()
        if result[1]<=cw:
            result=[cnode, cw]
        for values in trees[cnode]:
            nnode, nw = values
            if not visited[nnode]:
                visited[nnode]=True
                stack.append([nnode, cw+nw])
    return result

n=int(sys.stdin.readline())
trees=[[] for _ in range(n+1)]
for _ in range(n-1):
    x,y,w=map(int,sys.stdin.readline().split())
    trees[x].append([y,w])
    trees[y].append([x,w])

first=dfs(1)
second=dfs(first[0])
print(second[1])