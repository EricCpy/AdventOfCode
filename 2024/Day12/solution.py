from collections import deque
import uuid

def solution():
    with open('./Day12/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    dirs = [
        (-1, 0), (0, 1), (1, 0), (0, -1)  # Up, Right, Down, Left 
    ]
    
    flower_dict = {}
    visited = set()
    for x, line in enumerate(data):
        for y, val in enumerate(line): 
            
            if (x,y) in visited:
                continue
            
            id = val + "-" + str(uuid.uuid4())
            flower_dict[id] = [0,0]
        
            queue = deque()
            queue.append((x,y))
            visited.add((x,y))
            while len(queue) > 0:
                curr = queue.pop()
                flower_dict[id][0] += 1
                for dir in dirs:
                    nx = curr[0] + dir[0]
                    ny = curr[1] + dir[1]
                    
                    if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]) or data[nx][ny] != val:
                        flower_dict[id][1] += 1
                        continue
                    
                    if (nx, ny) in visited:
                        continue
                    
                    queue.append((nx,ny))
                    visited.add((nx,ny))
        
    return sum(item[0] * item[1] for item in flower_dict.values())

def solution2():
    with open('./Day12/input.txt', 'r') as f:
        data = f.read().splitlines()

    dirs = [
        (-1, 0), (0, 1), (1, 0), (0, -1)  # Up, Right, Down, Left 
    ]

    flower_dict = {}
    visited = set()

    for x, line in enumerate(data):
        for y, val in enumerate(line): 

            if (x, y) in visited:
                continue

            id = val + "-" + str(x) + "-" + str(y)
            flower_dict[id] = [0, [{dir : {} for dir in dirs}, {dir : {} for dir in dirs}, 0]]  # Use a dictionary to store x as keys and sets of y values

            queue = deque()
            queue.append((x, y))
            visited.add((x, y))

            while queue:
                curr = queue.popleft()
                flower_dict[id][0] += 1

                for dir in dirs:

                    nx = curr[0] + dir[0]
                    ny = curr[1] + dir[1]

                    if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]) or data[nx][ny] != val:
                        if nx not in flower_dict[id][1][0][dir]:
                            flower_dict[id][1][0][dir][nx] = set()
                            
                        if ny not in flower_dict[id][1][1][dir]:
                            flower_dict[id][1][1][dir][ny] = set()
                        
                        flower_dict[id][1][0][dir][nx].add(ny)
                        flower_dict[id][1][1][dir][ny].add(nx)
                        continue

                    if (nx, ny) in visited:
                        continue

                    queue.append((nx, ny))
                    visited.add((nx, ny))

    visited = set()
    for x, line in enumerate(data):
        for y, val in enumerate(line): 

            if (x, y) in visited:
                continue

            id = val + "-" + str(x) + "-" + str(y)

            queue = deque()
            queue.append((x, y))
            visited.add((x, y))

            while queue:
                curr = queue.popleft()
                for dir in dirs:

                    nx = curr[0] + dir[0]
                    ny = curr[1] + dir[1]

                    if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]) or data[nx][ny] != val:
                        add = True
                        if nx in flower_dict[id][1][0][dir] and (ny - 1 in flower_dict[id][1][0][dir][nx]):
                            add = False
                        
                        if ny in flower_dict[id][1][1][dir] and (nx - 1 in flower_dict[id][1][1][dir][ny]):
                            add = False

                        if add:
                            flower_dict[id][1][2] += 1
                        continue

                    if (nx, ny) in visited:
                        continue

                    queue.append((nx, ny))
                    visited.add((nx, ny))

    return sum(item[0] * item[1][2] for item in flower_dict.values())


if __name__ == "__main__":
    print(solution())
    print(solution2())