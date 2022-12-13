from collections import deque


def solution(sol1=True):
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    queue = deque()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if sol1:
                if data[i][j] == 'S':
                    queue.append((i, j))
                    break
                continue
            if data[i][j] == 'S' or data[i][j] == 'a':
                queue.append((i, j))
                
    dirs = [(0,1), (0, -1), (1,0), (-1,0)]
    visited = set()
    steps = 0
    visited.add(queue[0])
    
    while(len(queue) > 0):
        k = len(queue)
        steps += 1
        for _ in range(k):
            curr = queue.popleft()
            for dir in dirs:
                next = (curr[0] + dir[0], curr[1] + dir[1])
                if next[0] >= 0 and next[1] >= 0 and next[0] < len(data) and next[1] < len(data[0]):
                    if next in visited:
                        continue
                    
                    currC = data[curr[0]][curr[1]]
                    if currC == 'S':
                        currC = 'a'
                    nextC = data[next[0]][next[1]]
                    if nextC == 'E':
                        nextC = 'z'
                    
                    if ord(nextC) <= ord(currC) or ord(nextC) - 1 == ord(currC):
                        if data[next[0]][next[1]] == 'E':
                            return steps
                        queue.append(next)
                        visited.add(next)        
    return -1
                    
                     
if __name__ == "__main__":
    print(solution())
    print(solution(False))