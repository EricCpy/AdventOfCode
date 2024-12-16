from queue import PriorityQueue
from collections import deque

def solution():
    with open('./Day16/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    dirs = [
        (-1, 0), (0, 1), (1, 0), (0, -1)  # Up, Right, Down, Left
    ]

    for x, line in enumerate(data):
        for y, val in enumerate(line):
            if val == 'S':
                start_x = x
                start_y = y
                break
    
    queue = PriorityQueue()
    visited = dict()
    queue.put((0, start_x, start_y, 1))
    visited[(start_x, start_y)] = 0
    
    while not queue.empty():
        cost, x, y, last_dir_idx = queue.get()
        
        if data[x][y] == 'E':
            return cost
        
        for i in [1, 0, -1]:
            dir_idx = (last_dir_idx + i) % len(dirs)
            dir = dirs[dir_idx]
            nx, ny = x + dir[0], y + dir[1]

            if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]) or data[nx][ny] == '#':
                continue
            
            turn_penalty = 1000 if i != 0 else 0
            ncost = cost + 1 + turn_penalty

            if (nx, ny) not in visited or visited[(nx, ny)] > ncost:
                queue.put((ncost, nx, ny, dir_idx))
                visited[(nx, ny)] = ncost
    
    return -1

def solution2():
    with open('./Day16/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    dirs = [
        (-1, 0), (0, 1), (1, 0), (0, -1)  # Up, Right, Down, Left
    ]

    for x, line in enumerate(data):
        for y, val in enumerate(line):
            if val == 'S':
                start_x, start_y = x, y
    
    queue = PriorityQueue()
    visited = {}
    
    queue.put((0, start_x, start_y, 1))
    visited[(start_x, start_y, 1)] = 0
    
    backtrack = {}
    min_cost = float('inf')
    end_states = set()

    while not queue.empty():
        cost, x, y, last_dir_idx = queue.get()
        
        if cost > visited.get((x, y, last_dir_idx), float('inf')):
            continue

        if data[x][y] == 'E':
            if cost > min_cost:
                continue
            min_cost = cost
            end_states.add((x, y, last_dir_idx))

        for i in [0, 1, -1]:
            dir_idx = (last_dir_idx + i) % len(dirs)
            dx, dy = dirs[dir_idx]
            if dir_idx == last_dir_idx:
                nx, ny = x + dx, y + dy
                new_cost = cost + 1
            elif dir_idx != last_dir_idx:
                nx, ny = x, y
                new_cost = cost + 1000

            if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]) or data[nx][ny] == '#':
                continue

            if new_cost <= visited.get((nx, ny, dir_idx), float('inf')):
                if new_cost < visited.get((nx, ny, dir_idx), float('inf')):
                    backtrack[(nx, ny, dir_idx)] = set()
                    visited[(nx, ny, dir_idx)] = new_cost
                    
                backtrack[(nx, ny, dir_idx)].add((x, y, last_dir_idx))
                queue.put((new_cost, nx, ny, dir_idx))

    seen = set()
    states = deque(end_states)

    while states:
        key = states.popleft()
        for last in backtrack.get(key, []):
            if last in seen: 
                continue
            
            seen.add(last)
            states.append(last)

    s = set()
    for x in seen:
        s.add(x[:2])

    return len(s) + 1

if __name__ == "__main__":
    print(solution())
    print(solution2())