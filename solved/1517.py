import sys
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
    def merge(low, mid, high):
        global result
        temp = []
        l, h = low, mid
        while l < mid and h < high:
            if arr[l] > arr[h]:
                temp.append(arr[h])
                h += 1
                result+=(mid-l)
            else:
                temp.append(arr[l])
                l += 1
        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        for i in range(low, high):
            arr[i] = temp[i - low]
    return sort(0, len(arr))
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
result=0
merge_sort(arr)
print(result)