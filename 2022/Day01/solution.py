
#Time O(n) Space O(1)
def solution():
    f = open("input.txt")
    firstMax, secondMax, thirdMax = 0, 0, 0
    curr = 0
    for x in f:
        if x == "\n": 
            firstMax, secondMax, thirdMax = helper(curr, firstMax, secondMax, thirdMax)
            curr = 0
            continue
        curr += int(x)

    firstMax, secondMax, thirdMax = helper(curr, firstMax, secondMax, thirdMax)
    return firstMax, firstMax + secondMax + thirdMax

def helper(curr, firstMax, secondMax, thirdMax):
    if firstMax < curr:
        thirdMax = secondMax
        secondMax = firstMax
        firstMax = curr
    elif secondMax < curr:
        thirdMax = secondMax
        secondMax = curr
    elif thirdMax < curr:
        thirdMax = curr
    
    return firstMax, secondMax, thirdMax


if __name__ == "__main__":
    print(solution())