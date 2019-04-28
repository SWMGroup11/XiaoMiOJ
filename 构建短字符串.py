import sys


def solution1(line):
    a,b = line.rstrip().split()
    for i in a:
        if i in b:
            temp = b.index(i)
            b = b[:temp] + b[temp + 1:]
        else:
            return "false"
    return "true"
for line in sys.stdin:
    print(solution1(line))
