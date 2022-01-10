import sys
dict_={0:0,1:1}
def fibo(num):
    if num not in dict_.keys():
        if num%2==0:#짝수
            F1=fibo(num//2)
            F2=fibo(num//2-1)
            dict_[num]=(F1*(F1+2*F2))%1000000007
        else:
            F1=fibo(num//2)
            F2=fibo(num//2+1)
            dict_[num]=(F1**2+F2**2)%1000000007
    return dict_[num]
print(fibo(int(sys.stdin.readline())))