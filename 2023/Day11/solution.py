import copy

N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
d = {'|': (N, S), '-': (E, W), 'L': (N, E), 'J': (N, W), '7': (S, W), 'F': (S, E), '.': ()}

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
            print(i)
            expanded_data.insert(i + len(expanded_data) - len(data), "".join(['.' for _ in range(len(data))]))
    
    for i in range(len(expanded_data)):
        c = 0
        for j in range(len(expanded_data[i])):
            if cols[j]:
                expanded_data[i] = expanded_data[i][:j+c] + '.' + expanded_data[i][j+c:]
                c += 1
              
    galaxies = []   
    # manhattan dist zwischen allen berechnen

if __name__ == "__main__":
    print(solution())
