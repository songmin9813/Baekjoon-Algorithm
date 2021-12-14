a,b=map(int, input().split())
dict_={}
for _ in range(a):
    v=input()
    dict_[v]=True
count=0
result=[]
for _ in range(b):
    v=input()
    if v in dict_.keys():
        count+=1
        result.append(v)
result.sort()
print(count)
for v in result:
    print(v)