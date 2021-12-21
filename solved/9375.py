tc=int(input())
for _ in range(tc):
    n=int(input())
    dict_={}
    for __ in range(n):
        category=list(map(str,input().split()))[1]
        if category in dict_.keys():
            dict_[category]+=1
        else:
            dict_[category]=1
    result=1
    for value in dict_.values():
        result*=(value+1)
    print(result-1)