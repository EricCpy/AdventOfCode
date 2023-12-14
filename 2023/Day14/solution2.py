def solution():
    with open('./Day14/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    # get all columns
    # for each column remember last stone
    stones = [[] for x in range(len(data))]
    for x in data:
        for i,y in enumerate(x):
            stones[i].append(y)

    stones = rotate_field(stones)
    stones = rotate_field(stones)
    
    arr = []
    arr_set = set() 

    for _ in range(1000000000):
        for i in range(4):
            stones = roll_stones(stones)
            stones = rotate_field(stones)
        
        special_load = calc_special_load(stones)
        if special_load in arr_set:
            break
        else:
            load = calc_load(stones)
            arr.append(load)
            arr_set.add(special_load)    
        
    return arr[ 1000000000 % len(arr) ]                    

def roll_stones(stones):
    for stone_row_idx, stone_row in enumerate(stones):
        for stone_idx, x in enumerate(stone_row):
            if x == 'O':
                curr_row = stone_idx
                next = stones[stone_row_idx][curr_row -1]
                while next == '.' and curr_row - 1 >= 0:
                    stones[stone_row_idx][curr_row - 1] = 'O'
                    stones[stone_row_idx][curr_row] = '.'
                    curr_row -= 1
                    next = stones[stone_row_idx][curr_row -1]
                    
    return stones
                
def rotate_field(stones):
    nstones = [[] for x in range(len(stones))]
    for x in stones:
        for i,y in enumerate(x):
            nstones[i].append(y)

    return nstones
    
def calc_special_load(stones):
    ans = 0
    for stone_row_idx, stone_row in enumerate(stones):
        for stone_idx, x in enumerate(stone_row):
            if x == 'O':
                ans += stone_idx + len(stones) * (stone_row_idx + 1)
    
    return ans        
    

def calc_load(stones):             
    ans = 0
    for stone_row_idx, stone_row in enumerate(stones):
        for x in stone_row:
            if x == 'O':
                ans += len(stones) - (stone_row_idx + 1)
    
    return ans    
     
     
     
if __name__ == "__main__":
    print(solution())
