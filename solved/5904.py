import sys
def tracking(start,end,i,n):
    if i==0:
        if n==start:
            print('m')
        else:
            print('o')
        return
    midlength=3+i
    otherlength=(end-start-midlength+1)//2
    leftend=start+otherlength-1
    rightstart=leftend+midlength
    if start<=n<=leftend:
        tracking(start,leftend,i-1,n)
    elif n<=rightstart:
        if leftend+1==n:
            print('m')
        else:
            print('o')
        return
    else:
        tracking(rightstart+1,end,i-1,n)
n,i,length=int(sys.stdin.readline()),0,3
while True:
    if n<=length:
        break
    i+=1
    length=length*2+(3+i)
tracking(1,length,i,n)