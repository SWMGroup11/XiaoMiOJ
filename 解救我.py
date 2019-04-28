import sys

def solution1(line):
    str = [x for x in line.rstrip().split()][0]
    x = 0
    while x<len(str)-1:
        if str[x] == 'm':
            if str[x + 1] == 'i':
                str = str[:x] + str[x+2:]
                x -= 2
        x = x + 1
    return str


for line in sys.stdin:
    print(solution1(line))
