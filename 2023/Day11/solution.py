import copy

def solution():
    with open('./Day11/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    expanded_data = copy.deepcopy(data)
    cols = [True for x in range(len(data[0]))]
    for i, x in enumerate(data):
        r = True
        for j, y in enumerate(data[i]):
            if y != '.':
                cols[j] = False
                r = False

        if r:
            expanded_data.insert(i + len(expanded_data) - len(data), "".join(['.' for _ in range(len(data))]))
    
    for i in range(len(expanded_data)):
        c = 0
        for j in range(len(expanded_data[i])):
            if cols[j]:
                expanded_data[i] = expanded_data[i][:j+c] + '.' + expanded_data[i][j+c:]
                c += 1
              
    galaxies = []
    for i, x in enumerate(expanded_data):
        for j, y in enumerate(x):
            if y == '#':
                galaxies.append((i, j))
    
    ans = 0
    for i in range(len(galaxies)-1):
        for j in range(i, len(galaxies)):
            ans += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    return ans

if __name__ == "__main__":
    print(solution())
