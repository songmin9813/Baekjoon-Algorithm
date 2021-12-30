import sys
a,b,c=map(int,sys.stdin.readline().split())
modsum=1
while b!=1:
    if b%2==1:
        modsum=(modsum*a)%c
    a=a*a%c
    b//=2
print((a*modsum)%c)