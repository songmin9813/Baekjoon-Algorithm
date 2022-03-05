import sys
nums=[int(sys.stdin.readline())for _ in range(5)]
for i in range(5):
    if nums[i]<40:
        nums[i]=40
print(sum(nums)//5)