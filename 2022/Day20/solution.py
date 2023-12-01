def solution():
    with open('test.txt', 'r') as f:
        data = f.read().splitlines()
        nums = list(enumerate(map(int, data)))
        
    old = nums.copy()
    #swap
    for i, x in enumerate(old):
        for idx in range(len(nums)):
            if nums[idx][0] == i:
                break
        
        cur = idx
        if x < 0:
            for _ in range(-x):
                nums = swap(nums, cur, (cur - 1) % len(nums))
                cur = (cur - 1) % len(nums)

            continue

        if x > 0:
            for _ in range(x):
                nums = swap(nums, cur, (cur + 1) % len(nums))
                cur = (cur + 1) % len(nums)
    
    
    #find zero
    zero = data.index(0)
    
    ans = 0
    for i in range(0,3000,1000):
        ans += data[(zero + i) % len(data)]
        
    return ans
    
def swap(data, i, j):
    data[i], data[j] = data[j], data[i]


if __name__ == "__main__":
    print(solution())