import sys
n=int(sys.stdin.readline())
list_=[1,2]
for i in range(2,n):
    list_.append((list_[i-1]+list_[i-2])%10007)
print(list_[n-1])