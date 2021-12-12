def backtracking(index, length, visited, string,temp,result,channel):
    if index==length:
        result.append(abs(int(string)-int(channel))+length)
        return
    for i1,two in enumerate(temp[index]):
        if visited[index][i1] is not True:
            visited[index][i1]=True
            string+=str(temp[index][i1])
            backtracking(index+1,length,visited,string,temp,result,channel)
            string=string[:-1]
            visited[index][i1]=False
            
channel=input()
n=int(input())
remote=list(range(0,10))
if n!=0:
    minus_remote=map(int,input().split())
    for v in minus_remote:#망가진 리모컨 생성
        remote.remove(v)
length=len(channel)
result=abs(int(channel)-100)#단순 +- 값 저장
if len(remote)!=0:
    if len(channel)==1:
        rangelist_=[length,length+1]
    elif len(channel)==6:
        rangelist_=[length-1,length]
    else:
        rangelist_=[length-1,length,length+1]
    for leng in rangelist_:
        manipulate=[]
        visited=[]
        tmpresult=[]
        for _ in range(leng):
            manipulate.append(remote)
        for one in manipulate:
            list_=[]
            for two in one:
                list_.append(False)
            visited.append(list_)
        backtracking(0,leng,visited,'',manipulate,tmpresult,channel)
        result=min(result,min(tmpresult))
print(result)