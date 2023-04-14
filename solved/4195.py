import sys
def find(x):
    if trees[x]!=x:
        trees[x]=find(trees[x])
    return trees[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        trees[y]=x
        lengths[x]+=lengths[y]
        lengths[y]=lengths[x]
    return lengths[y]

tc=int(sys.stdin.readline())
for _ in range(tc):
    f=int(sys.stdin.readline())
    dict_,trees,lengths={},[],[]
    index=0
    for _ in range(f):
        a,b=map(str,sys.stdin.readline().split())
        if a not in dict_.keys():
            dict_[a]=index
            trees.append(index)
            lengths.append(1)
            index+=1
        if b not in dict_.keys():
            dict_[b]=index
            trees.append(index)
            lengths.append(1)
            index+=1
        print(union(dict_[a],dict_[b]))

        
