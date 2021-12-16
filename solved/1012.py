tc=int(input())
for _ in range(tc):
    n,m,k=map(int,input().split())
    visited=[[False for col in range(m)]for row in range(n)]
    cabbages=[]
    for __ in range(k):
        a,b=map(int,input().split())
        cabbages.append([a,b])
    count=0
    for i,value in enumerate(cabbages):
        stack=[]
        if visited[value[0]][value[1]] is not True:
            stack.append(value)
            count+=1
            visited[value[0]][value[1]]=True
            while stack:
                node=stack.pop()
                dx=[-1,0,1,0]
                dy=[0,1,0,-1]
                for i in range(4):
                    newX=node[0]+dx[i]
                    newY=node[1]+dy[i]
                    if newX>=0 and newX<n and newY>=0 and newY<m and visited[newX][newY] is not True and [newX,newY] in cabbages:
                        visited[newX][newY]=True
                        stack.append([newX,newY])
    print(count)