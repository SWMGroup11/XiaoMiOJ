import sys

for line in sys.stdin:
    line = line.strip()
    nums = [int(i) for i in line.rstrip().split(",")]
    index = nums.index(min(nums))
    print(nums[(index+int(len(nums)/2))%len(nums)])