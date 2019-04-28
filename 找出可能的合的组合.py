import sys

def solution1(line):
    str = [x for x in line.rstrip().split()][0]
    target =  int([x for x in line.rstrip().split()[1]][0])
    element = [int(x) for x in str.split(",")]
    for i in range(len(element)):
        while


for line in sys.stdin:
    print(solution1(line))
