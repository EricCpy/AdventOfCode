def solution():
    def possible(res, nums, curr):
        if curr == res and len(nums) == 0:
            return True
        if len(nums) == 0:
            return False
        curr1 = curr + nums[0]
        curr2 = curr * nums[0]
        return possible(res, nums[1:], curr1) or possible(res, nums[1:], curr2)
        
    with open('./Day07/input.txt', 'r') as f:
        data = f.read().splitlines()

    ans = 0
    for line in data:
        split = line.split(':')
        res = int(split[0])
        nums = [int(x) for x in split[1].split(' ')[1:]]
        if possible(res, nums[1:], nums[0]):
            ans += int(res)

    return ans

def solution2():
    def possible(res, nums, curr):
        if curr == res and len(nums) == 0:
            return True
        if len(nums) == 0:
            return False
        curr1 = curr + nums[0]
        curr2 = curr * nums[0]
        curr3 = int(str(curr) + str(nums[0]))
        return possible(res, nums[1:], curr1) or possible(res, nums[1:], curr2) or possible(res, nums[1:], curr3)
        
    with open('./Day07/input.txt', 'r') as f:
        data = f.read().splitlines()

    ans = 0
    for line in data:
        split = line.split(':')
        res = int(split[0])
        nums = [int(x) for x in split[1].split(' ')[1:]]
        if possible(res, nums[1:], nums[0]):
            ans += int(res)

    return ans
if __name__ == "__main__":
    print(solution())
    print(solution2())