def solution_1():
    with open('./Day05/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    seeds = [int(x) for x in data[0].split(' ')[1:]]

    maps = []
    curr = []
    skip = False
    for line in data[3:]:
        if skip:
            skip = False
            continue
        
        if len(line) == 0:
            maps.append(sorted(curr, key=lambda x: x[1]))
            curr = []
            skip = True
            continue
            
        curr.append([int(x) for x  in line.split(' ')])
    
    maps.append(sorted(curr, key=lambda x: x[1]))
    curr = [seeds]
    for map in maps:
        curr_dsts = []
        for source in curr[len(curr)  - 1]:
            curr_dst = calc_dst(map, source)
            curr_dsts.append(curr_dst)
            
        curr.append(curr_dsts)
    
    return min(curr[len(curr)  - 1])

def calc_dst(map, seed):
    for x in map:
        if seed >= x[1] + x[2]:
            continue
        if seed < x[1]:
            return seed
        
        return x[0] + (seed - x[1])
    
    return seed
        

def solution_2():
    with open('./Day05/input.txt', 'r') as f:
        data = f.read().splitlines()


    seeds = [int(x) for x in data[0].split(' ')[1:]]
    new_seeds = [(int(seeds[i]), int(seeds[i+1])) for i in range(len(seeds)) if i % 2 == 0]
    maps = []
    curr = []
    skip = False
    for line in data[3:]:
        if skip:
            skip = False
            continue
        
        if len(line) == 0:
            maps.append(sorted(curr, key=lambda x: x[1]))
            curr = []
            skip = True
            continue
            
        curr.append([int(x) for x  in line.split(' ')])
        
    maps.append(sorted(curr, key=lambda x: x[1]))
    
    c = new_seeds
    for map in maps:
        curr_dsts = []
        for source in c:
            curr_dsts += calc_dst2(map, source)
            
        c = curr_dsts
    
    print(sorted(c, key=lambda x: x[0]))
    return min([source[0] for source in c])

def calc_dst2(map, seed) -> list:
    ans = []
    seed0 = seed[0]
    seed1 = seed[1]
    
    if map[0][1] > seed0:
        ans.append((seed0, min(map[0][1] - 1, (seed0 + seed1))))
    
    for x in map:
        if seed0 > x[1] + x[2]:
            continue
        if seed0 + seed1 < x[1]:
            break

        a = x[1] + x[2] - seed0 
        ans.append((x[0] - x[1] + seed0, min(a, seed1)))

        seed0 += min(a, seed1)
        seed1 -= min(a, seed1)
    
    
    if map[len(map) - 1][1] + map[len(map) - 1][2] < seed0 + seed1:
        ans.append((seed0, seed1))
    
    return ans


if __name__ == "__main__":
    print(solution_1())
    # prints too much, but one of the first nums is the ans
    print(solution_2())