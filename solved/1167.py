import sys
#트리의 지름 공식
#1. 임의의 점에서 최대 크기인 노드 i1을 찾는다
#2. i1에서 최대 크기인 노드 i2가 트리 지름
def dfs(node, startnode):
    stack=[[startnode, 0]]
    visited={startnode:True}
    result=[0,0]#최대거리, 인덱스
    while stack:
        cnode,tmpresult=stack.pop()
        for inode in node[cnode]:
            nextnode, length=inode
            if not nextnode in visited.keys():
                visited[nextnode]=True
                stack.append([nextnode,tmpresult+length])
                if result[0]<tmpresult+length:
                    result=[tmpresult+length, nextnode]
    return result
n=int(sys.stdin.readline())
node=[[]for _ in range(n+1)]
for i1 in range(1,n+1):
    temp=list(map(int,sys.stdin.readline().split()))[:-1]
    for i2 in range(1,len(temp),2):
        node[temp[0]].append([temp[i2],temp[i2+1]])
indexone=dfs(node, 1)
result=dfs(node, indexone[1])
print(result[0])