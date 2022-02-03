import sys
import bisect
def binary():
    start,end=1,points[-1]
    while start<=end:
        mid=(start+end)//2
        ci,count=points[0],1
        while True:
            ci=bisect.bisect_left(points,ci+mid)
            if ci==len(points):
                break
            ci=points[ci]
            count+=1
        if count>=m:
            global result
            start=mid+1
            result=mid
        else:
            end=mid-1
result=0
n,m=map(int,sys.stdin.readline().split())
points=[int(sys.stdin.readline())for _ in range(n)]
points.sort()
binary()
print(result)