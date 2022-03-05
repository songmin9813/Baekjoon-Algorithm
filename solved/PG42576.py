def solution(participant, completion):
    dict_={}
    for v in participant:
        try:
            dict_[v]+=1
        except:
            dict_[v]=1
    for v in completion:
        dict_[v]-=1
        if dict_[v]==0:
            del dict_[v]
    return list(dict_.keys())[0]
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))