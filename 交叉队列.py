import sys

for line in sys.stdin:
    s1,s2,s3 = line.strip().split(",")
    i1 = 0
    i2 = 0
    i3 = 0
    back1 = 0
    back2 = 0
    if len(s1) + len(s2) != len(s3):
        print("false")
        continue
    while 1:
        if i3 == len(s3):
            print("true")
            break
        if back1 == 0 and (i1 < len(s1)) and (s1[i1] == s3[i3]):
            i1 = i1 + 1
            i3 = i3 + 1
        elif (i2 < len(s2)) and (s2[i2] == s3[i3]):
            i2 = i2 + 1
            i3 = i3 + 1
            back1 = 0
        else:
                i1 = i1 - 1
                i3 = i3 - 1
                back1 = 1
        if i1 == -1:
                    print("false")
                    break

