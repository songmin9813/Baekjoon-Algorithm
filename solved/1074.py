def divide(r,c,number,result):
    if number==0:
        print(result)
        return
    if r<=pow(2,number-1):
        if c<=pow(2,number-1):#1사분면
            divide(r,c,number-1,result)
        else:
            result+=pow(2,number-1)**2
            divide(r,c-pow(2,number-1),number-1,result)
    elif c<=pow(2,number-1):#3사분면
        result+=(pow(2,number-1)**2)*2
        divide(r-pow(2,number-1),c,number-1,result)
    else:#4분면
        result+=(pow(2,number-1)**2)*3
        divide(r-pow(2,number-1),c-pow(2,number-1),number-1,result)
    return result
n,r,c=map(int,input().split())#r+1,c+1로 고정시킬 예정임. 0 생각하기 귀찮음
divide(r+1,c+1,n,0)