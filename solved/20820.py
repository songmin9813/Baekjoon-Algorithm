import sys
n,m=map(int,sys.stdin.readline().split())
dict_list={}
result=""
for _ in range(n):
    value = sys.stdin.readline().rstrip()
    if len(value) < m:
        continue
    if value in dict_list:
        dict_list[value]+=1
    else:
        dict_list[value]=1
sort_result=sorted(dict_list.keys(),key=lambda x:(-dict_list[x],-len(x),x))
for value in sort_result:
    print(value)