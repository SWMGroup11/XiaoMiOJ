import sys

def solution1(line):
    str = [int(x) for x in line.rstrip().split()]
    target = str[0]
    num = str[1]
    nums = str[2:]
    dict = {}
    for i in nums:
        dict[i] = factor(i)
    value = [v for v in sorted(dict.values())]
    temp = value[target-1]
    back = 0
    while target-2>=0:
        if value[target-1] == value[target-2]:
            back += 1
            target -= 1
        else:
            break
    all = [k for k, v in dict.items() if v == temp]
    return all[back]




def factor(n):
    count = 0
    for i in range(1, n+1):  # 这里的逻辑和你一样
        if n % i == 0:
            count += 1
            continue
        else:
            pass
    return count


for line in sys.stdin:
    print(solution1(line))
