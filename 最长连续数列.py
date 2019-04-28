import sys


def solution(line):
    lineList = line.strip().split(",")
    lineList = [int(x) for x in lineList]
    numDict = {}
    i = 0
    while(1):
        if(len(lineList)==0):
            break
        num = lineList[i]
        if not num in numDict:
            numDict[num] = 1
        left = 0
        right = 0
        while(num+left in numDict):
            left = left + 1
        while (num - right in numDict):
                right = right + 1
        numDict[num] =  left + right - 1
        while num in lineList:
            lineList.remove(num)
    maxLength = 0
    for i in numDict:
        if(numDict[i]>maxLength):
            maxLength = numDict[i]
    return maxLength
for line in sys.stdin:
    print(solution(line))