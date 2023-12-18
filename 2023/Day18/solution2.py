N, S, W, O = (-1,0), (1,0), (0,-1), (0,1)
instruction_mapping = {'0': O, '2': W, '3': N, '1': S}
def solution():
    with open('./Day18/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    edges = 0
    curr = (0, 0)
    points = [curr]
    for instruction in data:
        s = instruction.split(' ')
        dir = instruction_mapping[s[2][-2]]
        moves = int(s[2][2:-2], 16)
        edges += moves
        end = (curr[0] + moves * dir[0], curr[1] + moves * dir[1])
        points.append(end)
        curr = end
    
    return calc_area(points, edges)


def calc_area(points, edges):
    r = 0
    for i in range(len(points) - 1):
        # gaußsche trapez formel
        y1, x1 = points[i]
        y2, x2 = points[i + 1]
        r += x1 * y2 - x2 * y1
    # satz von pick
    return (abs(r) // 2) + (edges // 2) + 1

 
if __name__ == "__main__":
    print(solution())
