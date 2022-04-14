import sys

def nums_to_korean(n):
    nums_dict=["","일","이","삼","사","오","육","칠","팔","구"]
    nums_unit=[["","만","억"],"십","백","천"]
    #사전 정보 생성
    stack_one=list(n)
    stack_two,count=[],0
    unit_nums=[]
    while stack_one:
        stack_two.append(stack_one.pop())
        count+=1
        if count==4:
            stack_two.reverse()
            unit_nums.append(stack_two.copy())
            stack_two.clear()
            count=0
    if stack_two:
        stack_two.reverse()
        unit_nums.append(stack_two.copy())
    unit_nums.reverse()
    for i1,list_unit in enumerate(unit_nums):
        for i2,number in enumerate(list_unit):
            x=nums_dict[int(number)]
            unit_index=len(list_unit)-1-i2
            if unit_index==0:
                if int("".join(list_unit))!=0:
                    y=nums_unit[0][len(unit_nums)-1-i1]
                else:
                    y=""
            else:
                if x!="":
                    y=nums_unit[unit_index]
                else:
                    y=""
            print("{}: {}{}".format(number,x,y))
    #여기까지 분할 구현부
    stack_one=list(n)
    stack_two,count=[],0
    while stack_one:
        stack_two.append(stack_one.pop())
        count+=1
        if count==3:
            stack_two.append(',')
            count=0
    if stack_two[-1]==",":
        stack_two.pop()
    stack_two.reverse()
    result="".join(stack_two)
    #여기까지 삼분할 result 구현문
    return result
print("금액을 숫자로 입력: ",end="")
n=sys.stdin.readline().rstrip()
print(nums_to_korean(n))