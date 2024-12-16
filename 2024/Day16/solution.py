from queue import PriorityQueue
import heapq

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
    with open('./Day01/input.txt', 'r') as f:
        data = f.read().splitlines()
     
    return 0

if __name__ == "__main__":
    print(solution())
    print(solution2())