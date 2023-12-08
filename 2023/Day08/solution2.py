from math import gcd

def solution_2():
    with open('./Day08/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    instructions = data[0]
    
    dirs = dict()
    for i in data[2:]:
        dirs[i[:3]] = (i[7:10], i[12:15])

    curr = [x for x in dirs.keys() if x[2] == 'A']
    i = 0
    found = dict()
    while len(found) < len(curr):
        curr = [dirs[c][1] if instructions[i%len(instructions)] == 'R' else dirs[c][0] for c in curr]
        for idx, c in enumerate(curr):
            if c[2] == 'Z':
                found[idx] = i + 1
            
        i+=1
        
    return least_common(found.values())

def least_common(found):
    ans = 1
    for x in found:
        ans = (x * ans) / gcd(x,int(ans))
    return int(ans)

if __name__ == "__main__":
    print(solution_2())
