def solution():
    with open('./Day14/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    # get all columns
    # for each column remember last stone
    cols = [[] for x in range(len(data))]
    for x in data:
        for i,y in enumerate(x):
            cols[i].append(y)

    for i in range(10000):
        ans = 0
        for col in cols:
            last_stone = len(data)
            for i, x in enumerate(col):
                if x == 'O':
                    ans += last_stone
                    last_stone -= 1
                if x == '#':
                    last_stone = len(data) - (i + 1) 
    
    return ans                    
                
     
if __name__ == "__main__":
    print(solution())
