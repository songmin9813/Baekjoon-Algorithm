def dfs(list_,stack,visited):
    while len(stack)!=0:
        node=stack.pop()
        for value in list_[node]:
            if not visited[value]:
                visited[value]=True
                stack.append(value)
import sys
n,m=map(int, sys.stdin.readline().split())
list_=[[]for _ in range(n+1)]
visited=[False for _ in range(n+1)]
for _ in range(m):
    x,y=map(int, sys.stdin.readline().split())
    list_[x].append(y)
    list_[y].append(x)
stack=[]
result=0
for index in range(1,n+1):
    if not visited[index]:
        visited[index]=True
        result+=1
        stack.append(index)
        dfs(list_, stack, visited)
print(result)