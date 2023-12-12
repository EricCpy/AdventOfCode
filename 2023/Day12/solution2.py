def solution():
    with open('./Day12/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    ans = 0
    for i, x in enumerate(data):
        ans += calc_permutations("?".join([x.split(' ')[0] for i in range(5)]), [int(b) for b in (",".join([x.split(' ')[1] for i in range(5)])).split(',')], 0, 0, False, dict())

    return ans

def calc_permutations(s, nums, idx, curr_goal, last_spring, memo):
    if (idx, curr_goal, nums[curr_goal]) in memo:
        return memo[(idx, curr_goal, nums[curr_goal])]
    
    if curr_goal >= len(nums):
        return 0
    
    if nums[curr_goal] < 0:
        return 0
    
    if idx == len(s):
        if curr_goal == len(nums) - 1 and nums[curr_goal] == 0:
            return 1
        return 0
    
    ans = 0
    if s[idx] == '.' or s[idx] == '?':
        if last_spring and nums[curr_goal] > 0:
            pass
        else:
            if last_spring and len(nums) - 1 != curr_goal:
                ans += calc_permutations(s, nums, idx + 1, curr_goal + 1, False, memo)
            else:
                ans += calc_permutations(s, nums, idx + 1, curr_goal, False, memo)
    
    if (s[idx] == '#' or s[idx] == '?'):
        nums[curr_goal] -= 1
        ans += calc_permutations(s, nums, idx + 1, curr_goal, True, memo)
        nums[curr_goal] += 1 

    memo[(idx, curr_goal, nums[curr_goal])] = ans 
    
    return ans
    
    
if __name__ == "__main__":
    print(solution())
