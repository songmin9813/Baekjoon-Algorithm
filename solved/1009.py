n=int(input())
for _ in range(n):
    a,b=map(int, input().split())
    list_=[a%10]
    temp=a%10
    for _ in range(1,b):
        temp=temp*a%10
        if list_[0]==temp:#루프발생
            break
        else:
            list_.append(temp)
    result=list_[(b%len(list_))-1]
    if result==0:
        print(10)
    else:
        print(result)