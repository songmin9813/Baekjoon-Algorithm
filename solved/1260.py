from queue import Queue
def dfs(graph, start_node):
    visited={}
    stack=[]
    
    stack.append(start_node)
    while len(stack)!=0:
        node=stack.pop()
        if node not in visited:
            visited[node]=True
            stack.extend(reversed(graph[node]))
    return visited

def bfs(graph, start_node):
    visited={}
    queue=Queue()
    
    queue.put(start_node)
    while queue.qsize()!=0:
        node=queue.get()
        if node not in visited:
            visited[node]=True
            for nextNode in graph[node]:
                queue.put(nextNode)
    
    return visited

graph={}
n,m,v=map(int, input().split())
for n in range(1, n+1):
    graph[n]=[]#그래프 기반
for _ in range(m):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
for key in graph.keys():
    graph[key].sort()

dfsresult=list(dfs(graph,v).keys())
bfsresult=list(bfs(graph,v).keys())
re1=''
re2=''
for v1 in dfsresult:
    re1+=str(v1)+' '
for v2 in bfsresult:
    re2+=str(v2)+' '
print(re1)
print(re2)