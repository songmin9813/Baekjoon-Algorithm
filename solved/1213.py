import sys
from collections import Counter
string=sys.stdin.readline().rstrip()
result=["" for _ in range(len(string))]
counter=list(Counter(string).items())
counter.sort()
oddindex=-1
for i,values in enumerate(counter):
    al,nums=values
    if nums%2==1:
        if oddindex!=-1:
            print("I'm Sorry Hansoo")
            exit(0)
        result[len(string)//2]=al
        oddindex=i
i1,i2=0,-1
for values in counter:
    al,nums=values
    for _ in range(nums//2):
        result[i1]=al
        i1+=1
    for _ in range(nums//2):
        result[i2]=al
        i2-=1
print("".join(result))
