def solution(kn=2):
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    knots = [(0,0)] * kn
    moveDic = {'R': (1,0), 'U': (0,1), 'L': (-1, 0), 'D': (0, -1)}
    visited = set()
    visited.add((0,0))
    for x in data:
        move = moveDic[x[0]]
        for _ in range(int(x.split(' ')[1])):
            knots[0] = add(knots[0], move)
            for i in range(1, len(knots)):
                d = (knots[i-1][0] - knots[i][0], knots[i-1][1] - knots[i][1])
                if max(abs(d[0]), abs(d[1])) > 1:
                    knots[i] = add(knots[i], (d[0] / max(abs(d[0]), 1), d[1] / max(abs(d[1]), 1)))
                else:
                    break
            
            visited.add(knots[-1])
            
    return len(visited)

def add(h, move):
    return (h[0]+move[0], h[1]+move[1])

if __name__ == "__main__":
    print(solution(2))
    print(solution(10))