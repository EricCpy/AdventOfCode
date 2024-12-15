from collections import deque

def solution():
    with open('./Day15/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    split = data.index('')
    old_grid = data[:split]
    movements = "".join(data[split:]) 

    dirs = {
        '^': (-1, 0), 
        '>': (0, 1), 
        'v': (1, 0), 
        '<': (0, -1)  # Up, Right, Down, Left 
    }
    pos = None
    grid = []
    for x, line in enumerate(old_grid):
        curr = []
        for y, val in enumerate(line):
            if val == '@':
                pos = (x, y)
            
            curr.append(val)

        grid.append(curr)
    
    for movement in movements:
        dir = dirs[movement]
        nx = pos[0] + dir[0]
        ny = pos[1] + dir[1]
        if grid[nx][ny] == '#':
            continue
        
        if grid[nx][ny] == '.':
            grid[pos[0]][pos[1]] = '.'
            pos = (nx, ny)
            grid[pos[0]][pos[1]] = '@'
            continue
        
        nx_o = nx
        ny_o = ny
        while grid[nx_o][ny_o] == 'O':
            nx_o = nx_o + dir[0]
            ny_o = ny_o + dir[1]
        
        if grid[nx_o][ny_o] == '#':
            continue
        
        grid[pos[0]][pos[1]] = '.'
        pos = (nx, ny)
        grid[pos[0]][pos[1]] = '@'
        grid[nx_o][ny_o] = 'O'
    
    ans = 0     
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == 'O':
                ans += 100 * i + j    

    return ans

def solution2():
    with open('./Day15/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    split = data.index('')
    old_grid = data[:split]
    movements = "".join(data[split:]) 

    dirs = {
        '^': (-1, 0), 
        '>': (0, 1), 
        'v': (1, 0), 
        '<': (0, -1)  # Up, Right, Down, Left 
    }
    pos = None
    grid = []
    for x, line in enumerate(old_grid):
        curr = []
        for y, val in enumerate(line):
            if val == '@':
                pos = (x, y * 2)
                curr.append('@')
                curr.append('.')
            elif val == '.':
                curr.append('.')
                curr.append('.')
            elif val == '#':
                curr.append('#')
                curr.append('#')
            else:
                curr.append('[')
                curr.append(']')

        grid.append(curr)
    
    for movement in movements:
        dir = dirs[movement]
        nx = pos[0] + dir[0]
        ny = pos[1] + dir[1]
        if grid[nx][ny] == '#':
            continue
        
        if grid[nx][ny] == '.':
            grid[pos[0]][pos[1]] = '.'
            pos = (nx, ny)
            grid[pos[0]][pos[1]] = '@'
            continue
        
        queue = deque()
        visited = set()
        queue.append((nx, ny))
        visited.add((nx,ny, grid[nx][ny]))
        
        if grid[nx][ny] == ']':
            queue.append((nx, ny - 1))
            visited.add((nx,ny - 1, '['))
        else:
            queue.append((nx, ny + 1))
            visited.add((nx,ny + 1, ']'))
          
        move = True
        while len(queue) > 0:
            curr = queue.popleft()
            next1 = (curr[0] + dir[0], curr[1] + dir[1])
            next2 = None
            if grid[next1[0]][next1[1]] == '.':
                continue
            if grid[next1[0]][next1[1]] == ']':
                next2 = (curr[0] + dir[0], curr[1] + dir[1] - 1)
            else:
                next2 = (curr[0] + dir[0], curr[1] + dir[1] + 1)

            for next in [next1, next2]:
                if (next[0], next[1], grid[next[0]][next[1]]) in visited or grid[next[0]][next[1]] == '.':
                    continue
                if grid[next[0]][next[1]] == '#':
                    move = False
                    break

                queue.append(next)
                visited.add((next[0], next[1], grid[next[0]][next[1]]))

            if not move:
                break

        if move:
            used = set()
            for point in visited:
                p_nx = point[0] + dir[0]
                p_ny = point[1] + dir[1]
                grid[p_nx][p_ny] = point[2]
                used.add((p_nx, p_ny))
                if (point[0], point[1]) not in used:
                    grid[point[0]][point[1]] = '.'
            
            grid[pos[0]][pos[1]] = '.'
            pos = (nx, ny)
            grid[pos[0]][pos[1]] = '@'

    ans = 0     
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == '[':
                ans += 100 * i + j  
        
    return ans


if __name__ == "__main__":
    print(solution())
    print(solution2())