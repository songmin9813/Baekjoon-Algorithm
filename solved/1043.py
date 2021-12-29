import sys
n,m=map(int,sys.stdin.readline().split())
truth=list(map(int,sys.stdin.readline().split()))
truthdict={}
for i in range(1,len(truth)):
    truthdict[truth[i]]=True
party=[list(map(int,sys.stdin.readline().split()))[1:] for _ in range(m)]
visited=[False for _ in range(m)]
result,tmpresult=0,m
while result!=tmpresult:
    result=tmpresult
    dictsize=list(truthdict.keys())
    for key in dictsize:
        for i1 in range(m):
            if not visited[i1] and key in party[i1]:
                visited[i1]=True
                for value in party[i1]:
                    truthdict[value]=True
                tmpresult-=1
print(result)