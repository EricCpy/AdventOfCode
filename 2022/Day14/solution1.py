def solution():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    #find min x, y and and max x, y
    minX, maxX, maxY = 1000, 0, 0
    for l in data:
        coords = l.split(' -> ')
        for i in coords:
            x, y = i.split(',')
            x,y = int(x), int(y)
            minX = min(minX, x)
            maxX = max(maxX, x)
            maxY = max(maxY, y)
    
    cave = [[False for _ in range(minX, maxX+1)] for _ in range(maxY+1)]
    #init stones in grid
    for l in data:
        coords = l.split(' -> ')
        prevX, prevY = [int(x) for x in coords[0].split(',')]
        prevX -= minX
        for i in coords[1:]:
            x, y = [int(x) for x in i.split(',')]
            x -= minX
            initStoneRow(prevX, x, prevY, y, cave)
            prevX, prevY = x, y

    #fill with sand
    start = 500 - minX
    sand = 0
    while(not cave[0][start]):
        prevX, prevY = start, 0
        x, y = move(cave, prevX, prevY)
        while(prevY != y):
            prevX, prevY = x, y
            x, y = move(cave, prevX, prevY)
            
        if x + 1 == len(cave[0]) or x - 1 < 0 or y + 1 == len(cave):
            return sand
        
        cave[y][x] = True
        sand += 1
            
    return sand
    
def move(cave, x, y):
    y+=1
    if y == len(cave):
        return x, y - 1
    elif not cave[y][x]:
        return x, y
    elif x - 1 >= 0 and not cave[y][x-1]:
        return x-1, y
    elif x + 1 < len(cave[0]) and not cave[y][x+1]:
        return x+1, y
    else:
        return x, y - 1
    
def initStoneRow(prevX, x, prevY, y, cave):
    if prevX != x:
        for i in range(min(prevX, x), max(x, prevX)+1):
            cave[y][i] = True
    else:
        for i in range(min(prevY, y), max(y, prevY)+1):
            cave[i][x] = True

if __name__ == "__main__":
    print(solution())