import sys
def backtracking(result,index,fours):
    global maxValue,minValue,n
    if index==n:
        maxValue=max(maxValue,result)
        minValue=min(minValue,result)
        return
    for i,value in enumerate(fours):
        if value==0:
            continue
        else:
            fours[i]-=1
            if i==0:
                backtracking(result+nums[index],index+1,fours)
            elif i==1:
                backtracking(result-nums[index],index+1,fours)
            elif i==2:
                backtracking(result*nums[index],index+1,fours)
            else:
                if result<0 and nums[index]>0:
                    backtracking(-(-result//nums[index]),index+1,fours)
                else:
                    backtracking(result//nums[index],index+1,fours)
            fours[i]+=1
minValue=10**8
maxValue=-minValue
n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
fours=list(map(int,sys.stdin.readline().split()))
backtracking(nums[0],1,fours)
print(maxValue,minValue)