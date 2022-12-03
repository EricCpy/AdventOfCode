def solution():
    f = open("input.txt")
    res, res2 = 0, 0
    rucksacks = []
    for x in f:
        comp1, comp2 = set(x[: len(x) // 2]), set(x[len(x) // 2: len(x) - 1])
        res += helper(comp1 & comp2)
        
        rucksacks.append(set(x[0: len(x)-1]))
        if(len(rucksacks) == 3):
            res2 += helper(rucksacks[0] & rucksacks[1] & rucksacks[2])
            rucksacks.clear()
           
    return res, res2

def helper(intersects):
    c = list(intersects)[0] #only one intersect
    ans = 0
    if c.isupper():
        ans += 26
    ans += ord(c.lower()) - 96
    return ans

if __name__ == "__main__":
    print(solution())