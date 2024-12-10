from collections import deque

def solution():
    with open('./Day10/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    dirs = [
        (-1, 0), (0, 1), (1, 0), (0, -1)  # Up, Right, Down, Left 
    ]
    
    ans = 0
    for a, x_val in enumerate(data):
        for b, y_val in enumerate(x_val):
            if y_val == "0":
                queue = deque()
                queue.append((a, b))
                s = set()
                while len(queue) > 0:
                    x, y = queue.pop()
                    if data[x][y] == "9":
                        s.add((x,y))
                        continue
                    
                    for dir in dirs:
                        nx = x + dir[0]
                        ny = y + dir[1]
                        if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]) or data[nx][ny] == '.' or ord(data[nx][ny]) - ord(data[x][y]) != 1:
                            continue
                        
                        queue.append((nx, ny))

                ans += len(s)

    return ans


def solution2():
    with open('./Day10/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    dirs = [
        (-1, 0), (0, 1), (1, 0), (0, -1)  # Up, Right, Down, Left 
    ]
    
    queue = deque()
    for a, x_val in enumerate(data):
        for b, y_val in enumerate(x_val):
            if y_val == "0":
                queue.append((a, b))
           
           
    ans = 0     
    while len(queue) > 0:
        x, y = queue.pop()
        if data[x][y] == "9":
            ans += 1
            continue
        
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[nx]) or data[nx][ny] == '.' or ord(data[nx][ny]) - ord(data[x][y]) != 1:
                continue
            
            queue.append((nx, ny))

    return ans

if __name__ == "__main__":
    print(solution())
    print(solution2())