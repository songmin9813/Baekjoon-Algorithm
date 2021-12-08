n,k=map(int,input().split())
up=1
downone=1
downtwo=1
for v in range(1,n+1):
    up*=v
    if v==k:
        downone=up
    if v==(n-k):
        downtwo=up
print(int(up/(downone*downtwo)))