string=input()
list_=[]
resultstack=[]
a=''
for v in string:
    if v=='-' or v=='+':
        list_.append(int(a))
        list_.append(v)
        a=''
    else:
        a+=v
list_.append(a)
i=0
while i<len(list_):
    if list_[i]=='-':
        pass
    elif list_[i]=='+':
        resultstack[-1]=resultstack[-1]+int(list_[i+1])
        i+=1
    else:
        resultstack.append(int(list_[i]))
    i+=1
result=resultstack[0]
for i in range(1,len(resultstack)):
    result-=resultstack[i]
print(result)