def dfs(graph, depths, depth, visited, node):
    if node in visited:
        return
    visited[node]=True
    depths[node]=depth
    for node in graph[node]:
        if node not in visited:
            dfs(graph, depths, depth+1, visited, node)
    return
graph={}
n,m=map(int, input().split())

for num in range(1,n+1):
    graph[num]=[]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph.keys():
    visited={}
    depths={}
    dfs(graph, depths, 0, visited, node)
    print(depths)