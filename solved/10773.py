n=int(input())
stack=[]
result=0
for value in range(n):
    temp=int(input())
    if temp==0:
        result-=stack.pop()
    else:
        stack.append(temp)
        result+=temp
print(result)
        