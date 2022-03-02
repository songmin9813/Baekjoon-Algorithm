import heapq
def solution(phone_book):
    q=[]
    for v in phone_book:
        heapq.heappush(q,v)
    cv=heapq.heappop(q)
    while q:
        if cv==q[0][:len(cv)]:
            return False
        cv=heapq.heappop(q)
    return True