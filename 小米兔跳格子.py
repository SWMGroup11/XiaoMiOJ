import sys


def solution1(line):
    nums = [int(x) for x in line.rstrip().split()]
    current = 1
    while 1:
        if current -1 == len(nums) - 1:
            return "true"
        elif nums[current - 1] == 0:
            return "false"
        elif current -1>len(nums):
            return "false"

        else:
            current += nums[current -1]


for line in sys.stdin:
    print(solution1(line))
