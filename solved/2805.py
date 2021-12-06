n,m=map(int,input().split())
trees=list(map(int,input().split()))
trees.sort(reverse=True)
result=m #점점 깎여나갈 것
count=0
i=0
while True:
    if (i+1)<len(trees):#바로 다음 나무가 존재함
        if trees[i]==trees[i+1]:#다음 나무와 길이가 같음
            pass
        else:#다음 나무와 길이가 다름
            coe=i+1#계수 설정
            temp_result=coe*(trees[i]-trees[i+1])#현재 선에서 가장 많이 자를 수 있는 미터
            if temp_result >= result:#이선에서 끝날 경우
                if result%coe==0:
                    count+=int(result/coe)
                else:
                    count+=int(result/coe)+1
                break
            else:#아직 자를 미터가 남아있음
                result-=temp_result
                count+=int(temp_result/coe)
    else: #다음 나무가 존재하지 않음
        coe=i+1
        temp_result=coe*trees[i]
        if result%coe==0:
            count+=int(result/coe)
        else:
            count+=int(result/coe)+1
        break
    i+=1
        
print(trees[0]-int(count))