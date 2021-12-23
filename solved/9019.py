from collections import deque
def d(numstr,result):
    return [format(int(numstr)*2%10000,'04'),result+'D']
def s(numstr,result):
    return [format(int(numstr)-1,'04'),result+'S'] if int(numstr)!=0 else ['9999',result+'S']
def l(numstr,result):
    return [numstr[1]+numstr[2]+numstr[3]+numstr[0],result+'L']
def r(numstr,result):
    return [numstr[3]+numstr[0]+numstr[1]+numstr[2],result+'R']
def bfs(numstr,result,b):
    queue.append([numstr,result])
    visited[int(numstr)]=True
    while queue:
        string,tmpresult=queue.popleft()
        if string==b:
            break
        i1=int(string)*2%10000
        i2=int(string)-1 if int(string)!=0 else 9999
        i3=int(string[1]+string[2]+string[3]+string[0])
        i4=int(string[3]+string[0]+string[1]+string[2])
        if visited[i1] is not True:
            visited[i1]=True
            queue.append(d(string,tmpresult))
        if visited[i2] is not True:
            visited[i2]=True
            queue.append(s(string,tmpresult))
        if visited[i3] is not True:
            visited[i3]=True
            queue.append(l(string,tmpresult))
        if visited[i4] is not True:
            visited[i4]=True
            queue.append(r(string,tmpresult))
    return tmpresult
n=int(input())
queue=deque()
for _ in range(n):
    visited=[False for _ in range(10000)]
    a,b=map(str,input().split())
    a=a.zfill(4)
    b=b.zfill(4)
    print(bfs(a,'',b))
    queue.clear()