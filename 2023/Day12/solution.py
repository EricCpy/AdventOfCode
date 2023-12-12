def solution():
    with open('./Day12/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    ans = 0
    for x in data:
        ans += calc_permutations(x.split(' ')[0], [int(b) for b in x.split(' ')[1].split(',')], 0, 0, False)

    return ans

def calc_permutations(s, nums, idx, curr_goal, last_spring, debug_s = ""):
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
                ans += calc_permutations(s, nums, idx + 1, curr_goal + 1, False, debug_s + '.')
            else:
                ans += calc_permutations(s, nums, idx + 1, curr_goal, False, debug_s + '.')
    
    if (s[idx] == '#' or s[idx] == '?'):
        nums[curr_goal] -= 1
        ans += calc_permutations(s, nums, idx + 1, curr_goal, True, debug_s + '#')
        nums[curr_goal] += 1 

    return ans
    
    
if __name__ == "__main__":
    print(solution())
