import re
while True:
    string=input()
    if string == '.':break
    stack=[]
    cstr=re.findall('[\[\]\(\)\{\}]', string)
    for v in cstr:
        if v=='(' or v=='[' or v=='{':
            stack.append(v)
        elif v==')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(v)
                break
        elif v==']':
            if len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(v)
                break
        else:
            if len(stack)!=0 and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(v)
                break
    if len(stack)==0:
        print('yes')
    else:
        print('no')