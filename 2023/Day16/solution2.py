from collections import deque
import copy

N, S, W, O = (-1,0), (1,0), (0,-1), (0,1)

def solution():
    with open('./Day16/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    data = [[y for y in x] for x in data]

    top = [((-1, x), S) for x, _ in enumerate(data[0])] # richtig
    left = [((x, -1), O) for x, _ in enumerate(data)]
    bottom = [((len(data), x), N) for x, _ in enumerate(data[len(data) - 1])]
    right = [((x, len(x_val)), W) for x, x_val in enumerate(data)]
    
    start_positions = top + left + bottom + right
    
    ans = 0
    for curr in start_positions:
        queue = deque()
        queue.append(curr)
        visited : set[tuple[tuple, tuple]] = set()
        visited.add(curr)
        final_data = copy.deepcopy(data)
        while len(queue) > 0:
            (x,y), dir = queue.popleft()

            x_new = x + dir[0]
            y_new = y + dir[1]
            if x_new >= len(data) or x_new < 0 or y_new >= len(data[x_new]) or y_new < 0:
                continue
            
            new_dirs = get_new_dirs(data[x_new][y_new], dir)

            for dir in new_dirs:
                next = ((x_new, y_new), dir)
                if next not in visited:
                    queue.append(next)
                    visited.add(next)
                    final_data[x_new][y_new] = '#'

        ans = max(ans, sum(1 for x in final_data for y in x if y == '#'))
    
    return ans

def get_new_dirs(symbol,dir):
    if symbol == '.':
        return [dir]
    
    if symbol == '-':
        if dir == N or dir == S:
            return [W, O]
        return [dir]

    if symbol == '|':
        if dir == O or dir == W:
            return [N, S]
        return [dir]

    if symbol == '\\':
        if dir == N:
            return [W]
        if dir == S:
            return [O]
        if dir == W:
            return [N]
        if dir == O:
            return [S]

    if symbol == '/':
        if dir == N:
            return [O]
        if dir == S:
            return [W]
        if dir == W:
            return [S]
        if dir == O:
            return [N]


if __name__ == "__main__":
    print(solution())
