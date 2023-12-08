def solution_1():
    with open('./Day08/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    instructions = data[0]
    
    dirs = dict()
    for i in data[2:]:
        dirs[i[:3]] = (i[7:10], i[12:15])

    curr = "AAA"
    ans = 0
    i = 0
    while curr != "ZZZ":
        curr = dirs[curr][1] if instructions[i] == 'R' else dirs[curr][0]
        i += 1
        if i == len(instructions):
            i = 0
        ans += 1
        
    return ans

if __name__ == "__main__":
    print(solution_1())
