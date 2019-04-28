import sys


def solution(line):
    nums = [i for i in line.rstrip().split()]
    number = [int(i) for i in nums[0]]
    times = int(nums[1])

    for i in range(0,times):
        index = len(number)-1
        for j in range(len(number)-1):
            if number[j] > number[j+1]:
                index = j
                break
        number = number[0:index] + number[index+1:]
    result = 0
    for i in range(len(number)):
        result += pow(10,i)*int(number[len(number)-1-i])
    return result


for line in sys.stdin:
    print(solution(line))
