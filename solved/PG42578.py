def solution(clothes):
    dict_={}
    for v in clothes:
        try:
            dict_[v[1]]+=1
        except:
            dict_[v[1]]=1
    result=1
    for v in dict_.values():
        result*=(v+1)
    return result-1