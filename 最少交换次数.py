import sys

def solution(line):
    nums = [int(i) for i in line.rstrip().split(",")]
    j = 0
    temp = 0
    count = 0
    for i in range(len(nums)-1,-1,-1):
        for j in range(0,i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                count += 1
    return count
for line in sys.stdin:
    print(solution(line))

