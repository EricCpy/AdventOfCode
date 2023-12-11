import copy

def solution():
    with open('./Day11/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    expanded_data = copy.deepcopy(data)
    cols = [True for _ in range(len(data[0]))]
    rows = [True for _ in range(len(data))]
    for i, x in enumerate(data):
        for j, y in enumerate(data[i]):
            if y != '.':
                cols[j] = False
                rows[i] = False
              
    galaxies = []
    galaxy_movement = 999999
    curr_i= 0
    for i, x in enumerate(expanded_data):
        if rows[i]:
            curr_i+=galaxy_movement 
        curr_j = 0
        for j, y in enumerate(x):
            if cols[j]:
                curr_j+=galaxy_movement
            if y == '#':
                galaxies.append((curr_i, curr_j))
            curr_j += 1
        curr_i+=1
        
    ans = 0
    for i in range(len(galaxies)-1):
        for j in range(i, len(galaxies)):
            ans += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    return ans

if __name__ == "__main__":
    print(solution())
