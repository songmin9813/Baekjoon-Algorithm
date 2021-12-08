numdict={}
n=int(input())
list_=list(map(str,input().split()))
for value in list_:
    if value in numdict.keys():
        numdict[value]+=1
    else:
        numdict[value]=1
n=int(input())
findlist_=list(map(str,input().split()))
result=''
for value in findlist_:
    if value in numdict.keys():
        result+=str(numdict[value])+' '
    else:
        result+='0 '
print(result)