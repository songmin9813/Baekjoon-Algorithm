from collections import deque
def bfs(graph, current_queue, next_queue, visited, depths, depth):
    while current_queue:
        current_node=current_queue.popleft()
        if current_node not in visited:
            visited[current_node]=True
            depths[current_node]=depth
            for nextNode in graph[current_node]:
                next_queue.append(nextNode)
graph={}
n,m=map(int, input().split())

for num in range(1,n+1):
    graph[num]=[]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
result={}
for node in graph.keys():
    queue1=deque([node])
    queue2=deque()
    visited={}
    depths={}
    depth=0
    while queue1 or queue2:
        if len(queue1)==0:
            bfs(graph, queue2, queue1, visited, depths, depth)
        elif len(queue2)==0:
            bfs(graph, queue1, queue2, visited, depths, depth)
        depth+=1
    result[node]=sum(depths.values())
minnum=min(result,key=lambda x:result[x])
print(minnum)