import sys


def solution1(line):
    target = int(line.rstrip())
    if target == 1:
        return 1
    elif target == 2:
        return 2
    else:
        return solution1(str(target-1)) + solution1(str(target-2))


def solution2(line):
    target = int(line.rstrip())
    result = [1, 2]
    if target == 1:
        return 1
    elif target == 2:
        return 2
    else:
        for i in range(2, target):
            result.append(result[i-1] + result[i-2])
    return result[-1]


for line in sys.stdin:
    print(solution2(line))
