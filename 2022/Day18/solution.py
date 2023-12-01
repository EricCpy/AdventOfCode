from collections import deque

def solution():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    dirs = [(0,0,-1),(-1,0,0),(0,-1,0),(1,0,0),(0,1,0),(0,0,1)]
    grid = set()
    ans = 0
    for line in data:
        block = tuple([int(x) for x in line.split(',')])
        grid.add(block)
        ans += 6
        for dir in dirs:
            curr = tuple([dir[i] + x for i, x in enumerate(block)])
            if curr in grid:
                ans -=2
     
    return ans
            
def solution2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    dirs = [(0,0,-1),(-1,0,0),(0,-1,0),(1,0,0),(0,1,0),(0,0,1)]
    cubes = set()
    for line in data:
        block = tuple([int(x) for x in line.split(',')])
        cubes.add(block)
    
    min_x, min_y, min_z, max_x, max_y, max_z = 0, 0, 0, 0, 0, 0
    for x, y, z in cubes:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_z = min(min_z, z)
        max_z = max(max_z, z)
    min_x -= 1
    min_y -= 1
    min_z -= 1
    max_x += 1
    max_y += 1
    max_z += 1

    water_points = set()
    q = deque()
    q.append((min_x, min_y, min_z))
    while q:
        x, y, z = q.popleft()
        if (x, y, z) in water_points:
            continue
        water_points.add((x, y, z))
        for dir in dirs:
            nx, ny,nz = dir[0] + x, dir[1] + y, dir[2] + z
            if min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= z <= max_z:
                if (nx, ny, nz) not in cubes:
                    q.append((nx, ny, nz))

    lava_points = set()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) not in water_points:
                    lava_points.add((x, y, z))
    
    ans = 0
    for lava in lava_points:
        for dir in dirs:
            curr = tuple([dir[i] + x for i, x in enumerate(lava)])
            if curr not in lava_points:
                ans +=1
    
    return ans


if __name__ == "__main__":
    print(solution())
    print(solution2())