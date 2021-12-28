import sys
dict_={}
n=int(sys.stdin.readline())
binary=0b0
for _ in range(n):
    string=list(map(str,sys.stdin.readline().split()))
    if len(string)==2:#숫자가 존재하는 연산
        op,num=string[0],int(string[1])
        if op=='add':
            binary=binary|1<<num-1
        elif op=='remove':
            binary=binary&~(1<<num-1)
        elif op=='check':
            print(1) if binary&1<<num-1 else print(0)
        else:#toggle
            binary=binary^(1<<num-1)
    elif string[0]=='all':
        binary=0b11111111111111111111
    else:
        binary=0b0