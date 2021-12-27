import sys
dict_={}
n=int(sys.stdin.readline())
for _ in range(n):
    string=list(map(str,sys.stdin.readline().split()))
    if len(string)==2:#숫자가 존재하는 연산
        op,num=string[0],int(string[1])
        if op=='add' and num not in dict_.keys():
            dict_[num]=True
        elif op=='remove' and num in dict_.keys():
            del dict_[num]
        elif op=='check':
            if num not in dict_.keys():
                print(0)
            else:
                print(1)
        else:
            if num not in dict_.keys():
                dict_[num]=True
            else:
                del dict_[num]
    elif string[0]=='all':
        for i in range(1,21):
            dict_[i]=True
    else:
        dict_.clear()