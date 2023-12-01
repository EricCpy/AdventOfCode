import re

def solution():
    f = open("input.txt")
    res, res2 = 0, 0
    for x in f:
        nums = [int(x) for x in re.split('\D', x[:-1])]
        res += min(helper1(nums[:2], nums[2:]) + helper1(nums[2:], nums[:2]), 1)
        res2 += min(helper2(nums[:2], nums[2:]) + helper2(nums[2:], nums[:2]), 1)
    
    return res, res2

def helper1(numRange1, numRange2):
    if numRange1[0] <= numRange2[0] and numRange1[1] >= numRange2[1]: 
        return 1
    return 0

def helper2(numRange1, numRange2):
    if numRange1[0] <= numRange2[0] and numRange1[1] >= numRange2[0]:
        return 1
    return 0

if __name__ == "__main__":
    print(solution())