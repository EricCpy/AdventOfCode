from queue import PriorityQueue

N, S, W, O = (-1,0), (1,0), (0,-1), (0,1)
dirs = [N,S,W,O]
def solution():
    with open('./Day17/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    data = [[int(y) for y in x] for x in data]
    curr = ((0,0), O, 0)
    curr_2 = ((0,0), S, 0)
    
    visited = dict()
    visited[curr] = 0
    visited[curr_2] = 0
    
    queue = PriorityQueue()
    queue.put((0, curr))
    queue.put((0, curr_2))
    
    while not queue.empty():
        dist, ((x, y), old_dir, steps) = queue.get()    
        if x == len(data) - 1 and y == len(data[0]) - 1:
            return dist
        
        for dir in dirs:
            if (dir == N and old_dir == S) or \
                (dir == S and old_dir == N) or \
                (dir == O and old_dir == W) or \
                (dir == W and old_dir == O):
                continue
            if steps < 4 and dir != old_dir:
                continue
            if steps >= 10 and old_dir == dir:
                continue
            new_steps = 0
            if old_dir == dir:
                new_steps += steps
            new_steps += 1
            new_x = x + dir[0]
            new_y = y + dir[1]
            
            if new_x >= len(data) or new_x < 0 or new_y >= len(data[0]) or new_y < 0:
                continue
            
            n_dist = dist + data[new_x][new_y]
            val = ((new_x, new_y), dir, new_steps)
            if val not in visited or visited[val] > n_dist:
                queue.put((n_dist, val))
                visited[val] = n_dist
    
    return -1
    
if __name__ == "__main__":
    print(solution())
