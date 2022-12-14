def solution():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    cave = set()
    maxY = 0
    #init stones in grid
    for l in data:
        coords = l.split(' -> ')
        prevX, prevY = [int(x) for x in coords[0].split(',')]
        maxY = max(maxY, prevY)
        for i in coords[1:]:
            x, y = [int(x) for x in i.split(',')]
            maxY = max(maxY, y)
            initStoneRow(prevX, x, prevY, y, cave)
            prevX, prevY = x, y
    
    #fill with sand
    start = 500
    ground = maxY + 2
    sand = 0
    while((0, start) not in cave):
        prevX, prevY = start, 0
        x, y = move(cave, prevX, prevY, ground)
        while(prevY != y):
            prevX, prevY = x, y
            x, y = move(cave, prevX, prevY, ground)
        
        cave.add((y,x))
        sand += 1
            
    return sand
    
def move(cave, x, y, ground):
    y+=1
    if y == ground:
        return x, y - 1
    elif (y, x) not in cave:
        return x, y
    elif (y, x - 1) not in cave:
        return x-1, y
    elif (y,x + 1) not in cave:
        return x+1, y
    else:
        return x, y - 1
    
def initStoneRow(prevX, x, prevY, y, cave):
    if prevX != x:
        for i in range(min(prevX, x), max(x, prevX)+1):
            cave.add((y, i))
    else:
        for i in range(min(prevY, y), max(y, prevY)+1):
            cave.add((i, x))

if __name__ == "__main__":
    print(solution())