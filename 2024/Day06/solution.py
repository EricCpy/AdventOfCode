from collections import deque

def solution(data, x, y):
    dirs = deque([
        (-1, 0, '^'), (0, 1, '>'), (1, 0, 'd'), (0, -1, '<')  # Up, Right, Down, Left 
    ])

    curr = dirs.popleft()
    visited = dict()
    
    while not curr in visited.get(x * len(data[0]) + y, set()):
        data[x][y] = 'X'
        visited_dirs = visited.get(x * len(data[0]) + y, set())
        visited_dirs.add(curr)
        visited[x * len(data[0]) + y] = visited_dirs
        
        nx, ny = x + curr[0], y + curr[1]
        if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]):
            return False
        
        if data[nx][ny] == '#':
            dirs.append(curr)
            curr = dirs.popleft()
            continue
            
        x, y = nx, ny
    
    
    
    return True


def solution2():
    with open('./Day06/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    
    for idx, line in enumerate(data):
        curr = []
        for idx2, char in enumerate(line):
            curr.append(char)
            if char == '^':
               x, y = idx, idx2 
        data[idx] = curr  
    
    ans = 0
    for idx, line in enumerate(data):
        for idx2, char in enumerate(line):
            if char != '^' and char != '#':
                data[idx][idx2] = '#'
                ans += 1 if solution(data, x, y) else 0
                data[idx][idx2] = '.'

    return ans
    


if __name__ == "__main__":
    with open('./Day06/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    
    for idx, line in enumerate(data):
        curr = []
        for idx2, char in enumerate(line):
            curr.append(char)
            if char == '^':
               x, y = idx, idx2 
        data[idx] = curr
    
    print(solution(data, x, y))
    print(solution2())