def solution():
    with open('./Day14/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    # get all columns
    # for each column remember last stone
    stones = [[] for x in range(len(data))]
    for x in data:
        for i,y in enumerate(x):
            stones[i].append(y)
    
    arr = []
    arr_set = dict() 
    c = 1000000000
    start = 0
    for i in range(1000000000):
        for i in range(4):  
            stones = roll_stones(stones) 
            stones = rotate_field(stones)

        special_load = get_special_load(stones)
        load = calc_load(stones)
        

        if special_load in arr_set:
            start = arr_set[special_load]
            break
        arr.append(load)
        arr_set[special_load] = i  
  
    return arr[start + ((c - start) % (len(arr) - start)) ]                    

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
    return np.rot90(np.array(stones), k=1).tolist()
    
def get_special_load(stones):
    s = ""
    for stone_row in stones:
        s += "".join(stone_row) 
    
    return s        
    

def calc_load(stones):             
    ans = 0
    for stone_row_idx, stone_row in enumerate(stones):
        for x in stone_row:
            if x == 'O':
                ans += len(stones) - (stone_row_idx + 1)
    
    return ans    
     
     
import numpy as np 
if __name__ == "__main__":
    print(solution())
