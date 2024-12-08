from collections import Counter

def solution():
    with open('./Day08/input.txt', 'r') as f:
        data = f.read().splitlines()

    freq_dict : dict[str, list[tuple[int, int]]] = {}
    for i, line in enumerate(data):
        for j, x in enumerate(line):
            if x != '.':
                v = freq_dict.get(x, [])
                v.append((i, j))
                freq_dict[x] = v
    
    antinodes = set()    
    for key in freq_dict:
        x = freq_dict[key]
        for i in range(len(x)):
            for j in range(i, len(x)):
                x_diff = x[i][0] - x[j][0]
                y_diff = x[i][1] - x[j][1]

                for curr_idx in [i, j]:
                    for diff in [(x_diff, y_diff), (-x_diff, -y_diff)]:
                        nx = x[curr_idx][0] + diff[0]
                        ny = x[curr_idx][1] + diff[1]
                    
                        if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]) or data[nx][ny] == key:
                            continue
                        
                        antinodes.add((nx, ny))
                    
    
    return len(antinodes)

def solution2():
    with open('./Day08/input.txt', 'r') as f:
        data = f.read().splitlines()

    freq_dict : dict[str, list[tuple[int, int]]] = {}
    for i, line in enumerate(data):
        for j, x in enumerate(line):
            if x != '.':
                v = freq_dict.get(x, [])
                v.append((i, j))
                freq_dict[x] = v
    
    antinodes = set()    
    for key in freq_dict:
        x = freq_dict[key]
        for i in range(len(x)):
            for j in range(i, len(x)):
                x_diff = x[i][0] - x[j][0]
                y_diff = x[i][1] - x[j][1]

                for rep in range(100):
                    fails = 0
                    for diff in [(x_diff, y_diff), (-x_diff, -y_diff)]:
                        nx = x[i][0] + diff[0] * rep
                        ny = x[i][1] + diff[1] * rep
                    
                        if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]):
                            fails+=1
                            continue
                        
                        antinodes.add((nx, ny))
                    
                    if fails == 2:
                        break
    
    return len(antinodes)


if __name__ == "__main__":
    print(solution())
    print(solution2())