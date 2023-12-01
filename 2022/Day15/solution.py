def solution(y):
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    fields = set()
    for x in data:
        sb = x.split(' ')
        s = (int(sb[2].split('=')[-1][0:-1]), int(sb[3].split('=')[-1][0:-1]))
        b = (int(sb[-2].split('=')[-1][0:-1]), int(sb[-1].split('=')[-1]))
        d = distance(s, b)
        
        left, right = s[0], s[0]
        while(d >= distance(s, (left, y))):
            fields.add(left)
            fields.add(right)
            left -= 1
            right += 1
 
    return len(fields) - 1

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solution2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    sensors = []
    beacons = []
    dists = []
    
    for x in data:
        sb = x.split(' ')
        sensors.append((int(sb[2].split('=')[-1][0:-1]), int(sb[3].split('=')[-1][0:-1])))
        beacons.append((int(sb[-2].split('=')[-1][0:-1]), int(sb[-1].split('=')[-1])))
        dists.append(distance(sensors[-1], beacons[-1]))
    
    posLines = []
    negLines = []
    for i, s in enumerate(sensors):
        negLines.append(s[0] + s[1] - dists[i])
        negLines.append(s[0] + s[1] + dists[i])
        posLines.append(s[0] - s[1] - dists[i])
        posLines.append(s[0] - s[1] + dists[i])
        
    pos = 0
    neg = 0
    
    for i in range(2 * len(sensors)):
        for j in range(i + 1, 2 * len(sensors)):
            a, b= posLines[i], posLines[j]
            
            if abs(a - b) == 2:
                pos = min(a, b) + 1
                
            a, b= negLines[i], negLines[j] 
            if abs(a-b) == 2:
                neg = min(a,b) + 1
    
    x, y = (pos + neg) // 2, (pos - neg) // 2

    return x * 4000000 + y 

if __name__ == "__main__":
    print(solution(2000000))
    print(solution2())