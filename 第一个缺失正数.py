import sys

for line in sys.stdin:
    nums = [int(i) for i in line.rstrip().split(",")]
    currentMax = 1
    length = len(nums)
    dict = {x: False for x in nums}
    i = 0
    while i<length:
        if currentMax in dict:
            currentMax = currentMax + 1
        i = i + 1
    print(currentMax)