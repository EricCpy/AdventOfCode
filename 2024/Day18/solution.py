from collections import deque

def solution(width, height, until):
    with open('./Day18/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    dirs = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
    ]
    
    grid = [["." for y in range(height)] for x in range(width)]
    for pos in data[:until]:
        x,y = pos.split(",")
        grid[int(y)][int(x)] = '#'
    
    
    queue = deque()
    queue.append((0,0, 0))
    visited = set()
    while queue:
        x,y,step = queue.popleft()
        if x == height - 1 and y == width - 1:
            return step

        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid) or (nx, ny) in visited or grid[nx][ny] == '#':
                continue
                
            queue.append((nx,ny, step + 1))
            visited.add((nx,ny))
        
    return -1

def solution2(width, height, start):
    with open('./Day18/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    for i in range(start, len(data)):
        if solution(width, height, i) == -1:
            return data[i - 1]
    
    return None

if __name__ == "__main__":
    print(solution(71,71,1024))
    print(solution2(71,71,1024))