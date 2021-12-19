n=int(input())
m=int(input())
string=input()
pattern=False
oflag=False
count=0
result=0
for i,value in enumerate(string):
    if value=='I':
        if pattern is False:#새로운 패턴 등장
            pattern=True
            count=1
            oflag=True
        else:
            if oflag is True:#패턴 깨지자마자 새로운 패턴 가능성
                if count>n:
                    result+=(count-n)
                count=1
                oflag=True
            else:#패턴 유지
                count+=1
                oflag=True
    else:#o가 나오는 경우
        if pattern is True:
            if oflag is True:#옳게된 패턴
                oflag=False
            else:#패턴 깨짐. 새로운 패턴 찾아야됨
                if count>n:
                    result+=(count-n)
                count=0
                pattern=False
if count>n:
    result+=(count-n)
print(result)