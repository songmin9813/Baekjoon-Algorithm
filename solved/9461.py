tc=int(input())
for _ in range(tc):
    list_=[1,1,1]
    n=int(input())-1
    if n>2:
        for i in range(3,n+1):
            list_.append(list_[i-3]+list_[i-2])
    print(list_[n])