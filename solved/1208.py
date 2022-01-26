import sys
import itertools
def combi(T):
    arr=[0]
    for i in range(1,len(T)+1):
        tmplist=list(itertools.combinations(T,i))
        for v in tmplist:
            arr.append(sum(v))
    return arr
n,s=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
T1,T2=combi(nums[:len(nums)//2]),combi(nums[len(nums)//2:])
T1.sort()
T2.sort(reverse=True)
result,i1,i2=0,0,0#i1이 늘면 총 수가 늘어남. i2가 늘면 총 수가 줄어듦
while i1<len(T1) and i2<len(T2):
    tmps=T1[i1]+T2[i2]
    if tmps==s:
        lsame,rsame=1,1
        lv,rv=T1[i1],T2[i2]
        while True:
            if i1+1<len(T1) and T1[i1+1]==lv:
                lsame+=1
                i1+=1
            else:
                break
        while True:
            if i2+1<len(T2) and T2[i2+1]==rv:
                rsame+=1
                i2+=1
            else:
                break
        result+=(lsame*rsame)
        i1+=1
        i2+=1
    elif tmps>s:
        i2+=1
    else:
        i1+=1
print(result) if s!=0 else print(result-1)