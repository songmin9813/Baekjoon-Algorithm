import sys
n,m=map(int, sys.stdin.readline().split())
dict_={}
for _ in range(n):
    key,value=map(str, sys.stdin.readline().split())
    dict_[key]=value
for _ in range(m):
    print(dict_[sys.stdin.readline().strip()])