from collections import deque

N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
d = {'|': (N, S), '-': (E, W), 'L': (N, E), 'J': (N, W), '7': (S, W), 'F': (S, E), '.': ()}

def solution():
    with open('./Day10/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    queue = deque()
    visited = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                visited.add((i, j))
                visited.add((i,j))
                if N in d[data[i + 1][j]]:
                    queue.append((i + 1, j, 1))
                    visited.add((i + 1, j))
                if S in d[data[i - 1][j]]:
                    queue.append((i - 1, j, 1))
                    visited.add((i - 1, j))
                if E in d[data[i][j - 1]]:
                    queue.append((i, j - 1, 1))
                    visited.add((i, j - 1))
                if W in d[data[i][j + 1]]:
                    queue.append((i, j + 1, 1))
                    visited.add((i, j + 1))
    
    ans = 1        
    while len(queue) > 0:
        curr = queue.popleft()
        for dir in d[data[curr[0]][curr[1]]]:
            next = (curr[0] + dir[0], curr[1] + dir[1])
            if next in visited or next[0] < 0 or next[0] >= len(data) or next[1] < 0 or next[1] >= len(data[0]):
                continue
            
            visited.add(next)
            queue.append((next[0], next[1], curr[2] + 1))
            ans = max(curr[2] + 1, ans)
    
    return ans
    

if __name__ == "__main__":
    print(solution())
