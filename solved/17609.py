def oddoreven(string, flag, oddeven):#flag가 true라면 이미 하나가 삭제된거임
    str1=string[:int(len(string)/2)]
    if oddeven=='even':
        str2=string[len(string):int(len(string)/2-1):-1]
    else:
        str2=string[len(string):int(len(string)/2):-1]
    if str1==str2:#회문만족함
        if flag is True:
            return 1#하나만 제거되어 나오는 유사회문
        else:
            return 0#제거하지 않아도 회문임
    else:#회문을 만족하지 않음
        if flag is True:#이미 기회를 한 번 줌
            return 2
        else:#기회 한 번 줘야됨
            l_str1=list(str1)
            l_str2=list(str2)
            for i,v in enumerate(l_str1):
                if l_str1[i] != l_str2[i]:
                    tmplist=l_str1.copy()
                    del l_str1[i]
                    if oddeven == 'even':
                        new_list1=l_str1+l_str2[::-1]
                    else:
                        new_list1=l_str1+list(string[int(len(string)/2)])+l_str2[::-1]
                    del l_str2[i]
                    if oddeven == 'even':
                        new_list2=tmplist+l_str2[::-1]
                    else:
                        new_list2=tmplist+list(string[int(len(string)/2)])+l_str2[::-1]
                    new_string1=''.join(new_list1)
                    new_string2=''.join(new_list2)
                    if oddeven == 'even':
                        oddeven = 'odd'
                    else:
                        oddeven = 'even'
                    if (oddoreven(new_string1,True,oddeven)==1) or (oddoreven(new_string2,True,oddeven)==1):
                        return 1
                    else:
                        return 2

n=int(input())
for i in range(n):
    string=input()
    if len(string)%2==1:
        print(oddoreven(string,False,'odd'))
    else:
        print(oddoreven(string,False,'even'))