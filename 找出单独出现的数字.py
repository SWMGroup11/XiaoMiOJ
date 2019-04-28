import sys

for line in sys.stdin:
    line = line.strip().split()
    integer = [int(x) for x in line]
    while(1):
        i = integer[0]
        count = 0
        for j in integer[1:]:
            if(i == j):
                count = count +1
        if(count==0):
            print(i)
            integer.remove(i)
        else:
            for c in range (0,count+1):
                integer.remove(i)
        if(len(integer)==0):
            break