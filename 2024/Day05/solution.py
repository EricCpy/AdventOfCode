def solution():
    with open('./Day05/input.txt', 'r') as f:
        data = f.read().splitlines()

    ans = 0
    start = False
    rules = {}

    for x in data:
        if x == '':
            break
        split = x.split("|")
        rules[split[1]] = rules.get(split[1], []) + [split[0]]
        
    for x in data:
        if x == '':
            start = True
            continue
        if not start:
            continue

        nums = x.split(",")
        valid = True

        for idx, num in enumerate(nums):
            if num in rules:
                for required in rules[num]:
                    if required in nums[idx:]:
                        valid = False
                        break
            if not valid:
                break

        if valid:
            ans += int(nums[len(nums) // 2])

    return ans


def solution2():
    with open('./Day05/input.txt', 'r') as f:
        data = f.read().splitlines()

    ans = 0
    start = False
    rules = {}

    for x in data:
        if x == '':
            break
        split = x.split("|")
        rules[split[1]] = rules.get(split[1], []) + [split[0]]

    for x in data:
        if x == '':
            start = True
            continue
        if not start:
            continue

        nums = x.split(",")
        for num in nums:
            if num in rules:
                total_len = sum(1 for other_num in nums if other_num in rules[num])
                if total_len == len(nums) // 2:
                    ans += int(num)
                    
    return ans - solution()

if __name__ == "__main__":
    print(solution())
    print(solution2())