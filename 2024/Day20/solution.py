from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

def precompute_distances(grid, end_x, end_y):
    distances = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
    queue = deque([(end_x, end_y, 0)])
    distances[end_x][end_y] = 0
    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and distances[nx][ny] > dist + 1:
                distances[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))
    return distances

def solution():
    with open('./Day20/input.txt', 'r') as f:
        data = f.read().splitlines()

    grid = [list(line) for line in data]
    start_x, start_y, end_x, end_y = -1, -1, -1, -1

    for x, line in enumerate(grid):
        for y, val in enumerate(line):
            if val == 'S':
                start_x, start_y = x, y
            elif val == 'E':
                end_x, end_y = x, y

    distances_to_end = precompute_distances(grid, end_x, end_y)
    distances_to_start = precompute_distances(grid, start_x, start_y)

    ans = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '.' or grid[x][y] == 'S':
                dist_to_start = distances_to_start[x][y]
                for dir1 in dirs:
                    for dir2 in dirs:
                        nx, ny = x + dir1[0] + dir2[0], y + dir1[1] + dir2[1]
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                            cheat_dist = dist_to_start + 2 + distances_to_end[nx][ny]
                            normal_dist = dist_to_start + distances_to_end[x][y]
                            if normal_dist - cheat_dist >= 100:
                                ans += 1

    return ans


def solution2():
    with open('./Day20/input.txt', 'r') as f:
        data = f.read().splitlines()

    grid = [list(line) for line in data]
    rows, cols = len(grid), len(grid[0])
    start_x, start_y, end_x, end_y = -1, -1, -1, -1

    for x, line in enumerate(grid):
        for y, val in enumerate(line):
            if val == 'S':
                start_x, start_y = x, y
            elif val == 'E':
                end_x, end_y = x, y

    distances_to_end = precompute_distances(grid, end_x, end_y)
    distances_to_start = precompute_distances(grid, start_x, start_y)
    
    ans = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '.' or grid[x][y] == 'S':
                dist_to_start = distances_to_start[x][y]
                normal_dist = dist_to_start + distances_to_end[x][y]
                
                queue = deque([(x, y, 0)])
                visited = set()
                visited.add((x, y))
                while len(queue) > 0:
                    qx, qy, steps = queue.popleft()
                    cheat_dist = dist_to_start + steps + distances_to_end[qx][qy]
                    if grid[qx][qy] != '#' and normal_dist - cheat_dist >= 100:
                        ans += 1

                    if steps == 20:
                        continue
                    
                    for dx, dy in dirs:
                        nx, ny = qx + dx, qy + dy
                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny, steps + 1))
                                                
    return ans

if __name__ == "__main__":
    print(solution())
    print(solution2())