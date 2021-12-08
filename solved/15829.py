r=31
m=1234567891
dpm=1
temp=input()
string=input()
result=0
for i,v in enumerate(string):
    result=(result+(ord(v)-96)*dpm)%m
    dpm=(dpm*r)%m
print(result)