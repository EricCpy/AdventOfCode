from collections import Counter

def solution():
    with open('./Day02/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    save = 0
    for line in data:
        nums = [int(x) for x in line.split()]
        is_valid = True

        for i in range(1, len(nums)):
            if i < len(nums) - 1:
                if not (0 < abs(nums[i] - nums[i - 1]) <= 3 and 0 < abs(nums[i + 1] - nums[i]) <= 3):
                    is_valid = False
                    break
            
            if i > 1:
                prev_diff = nums[i - 1] - nums[i - 2]
                curr_diff = nums[i] - nums[i - 1]
                if (prev_diff > 0 and curr_diff < 0) or (prev_diff < 0 and curr_diff > 0):
                    is_valid = False
                    break
        
        if is_valid:
            save += 1

    return save

def solution2():
    def is_valid_sequence(nums):
        for i in range(1, len(nums)):
            # Check absolute difference constraints
            if i < len(nums) - 1:
                if not (0 < abs(nums[i] - nums[i - 1]) <= 3 and 0 < abs(nums[i + 1] - nums[i]) <= 3):
                    return False

            # Check for switching between increasing and decreasing
            if i > 1:
                prev_diff = nums[i - 1] - nums[i - 2]
                curr_diff = nums[i] - nums[i - 1]
                if (prev_diff > 0 and curr_diff < 0) or (prev_diff < 0 and curr_diff > 0):
                    return False
        return True

    with open('./Day02/input.txt', 'r') as f:
        data = f.read().splitlines()

    save = 0
    for line in data:
        nums = [int(x) for x in line.split()]
        
        # Check if the original sequence is valid
        if is_valid_sequence(nums):
            save += 1
            continue
        
        # Try removing each number and check validity
        for i in range(len(nums)):
            reduced_nums = nums[:i] + nums[i + 1:]  # Remove the ith number
            if is_valid_sequence(reduced_nums):
                save += 1
                break

    return save

if __name__ == "__main__":
    print(solution())
    print(solution2())