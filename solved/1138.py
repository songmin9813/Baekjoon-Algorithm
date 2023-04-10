import sys
n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
result=[0 for _ in range(n)]
result[nums[0]]=1
for i1 in range(1,n):
    count=0
    for i2 in range(n):
        if result[i2]==0:
            if count==nums[i1]:
                result[i2]=i1+1
                break
            else:
                count+=1
print(*result)