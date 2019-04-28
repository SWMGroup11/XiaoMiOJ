import sys

count = 0
T = 0

for line in sys.stdin:
    if count==0:
        T = int(line)
        count += 1
    else:
        a = int(line.strip().split()[0])
        b = int(line.strip().split()[1]) + 1
        print (a*b)
