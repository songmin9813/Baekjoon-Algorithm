n=int(input())
twocount=0
fivecount=0
for num in range(1, n+1):
    if num%10==0:
        while num%2==0:
            num//=2
            twocount+=1
        while num%5==0:
            num//=5
            fivecount+=1
    elif num%2==0:
        while num%2==0:
            num//=2
            twocount+=1
    elif num%5==0:
        while num%5==0:
            num//=5
            fivecount+=1
print(min(twocount, fivecount))