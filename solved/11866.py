n,k=map(int,input().split())
list_=list(range(1,n+1))
index=0
output='<'
while len(list_)!=0:
    index=(index+k-1)%len(list_)
    output+=str(list_[index])+', '
    del list_[index]
output=output[:-2]+'>'
print(output)