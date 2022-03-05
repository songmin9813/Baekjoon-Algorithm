import sys
def findprime(n):
    dict_=[True for i in range(n+1)]
    dict_[0],dict_[1]=False,False
    iter=int(n**0.5)
    for i in range(2,iter+1):
        if not dict_[i]:
            continue
        for i2 in range(i+i,n+1,i):
            dict_[i2]=False
    result=[]
    for i in range(len(dict_)):
        if dict_[i]:
            result.append(i)
    return result
n=int(sys.stdin.readline())
prime=[0]+findprime(n)
tmpsum=0
for i in range(1,len(prime)):
    tmpsum+=prime[i]
    prime[i]=tmpsum
i,j,result=0,0,0
while i!=len(prime) or j!=len(prime)-1:
    tmp=prime[j]-prime[i]
    if j<len(prime)-1 and tmp<n:
        j+=1
    else:
        if tmp==n:
            result+=1
        i+=1
print(result)