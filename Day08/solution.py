def solution1():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    see = [ [False for _ in x ] for x in data ]
    #forward
    colMax = [-1] * len(data[0])
    for i in range(len(data)):
        rMax = -1
        for j in range(len(data[i])):
            curr = int(data[i][j])
            if curr > rMax or curr > colMax[j]:
                see[i][j] = True
                rMax = max(rMax, curr)
                colMax[j] = max(colMax[j], curr)
    
    #backward         
    colMax = [-1] * len(data[0])
    for i in reversed(range(len(data))):
        rMax = -1
        for j in reversed(range(len(data[i]))):
            curr = int(data[i][j])
            if curr > rMax or curr > colMax[j]:
                see[i][j] = True
                rMax = max(rMax, curr)
                colMax[j] = max(colMax[j], curr)
    
    #count
    ans=0
    for row in see:
        for col in row:
            if col:
                ans+=1
    
    return ans

def solution2():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    see = [ [1 for _ in x ] for x in data ]
    #forward
    cStacks = [[] for _ in range(len(data[0]))] 
    for i in range(len(data)):
        rStack = []
        for j in range(len(data[i])):
            curr = int(data[i][j])
            while len(rStack) > 0 and int(data[i][rStack[-1]]) < curr:
                rStack.pop()
            if len(rStack) == 0:
                see[i][j] *= j
            else:
                see[i][j] *= abs(rStack[-1] - j)   
            
            rStack.append(j)
            
            while len(cStacks[j]) > 0 and int(data[cStacks[j][-1]][j]) < curr:
                cStacks[j].pop()
            
            if len(cStacks[j]) == 0:
                see[i][j] *= i
            else:
                see[i][j] *= abs(cStacks[j][-1] - i)  
            
            cStacks[j].append(i)

    #backward         
    cStacks = [[] for _ in range(len(data[0]))]
    n = len(data) - 1 
    for i in reversed(range(len(data))):
        rStack = []
        for j in reversed(range(len(data[i]))):
            curr = int(data[i][j])
            while len(rStack) > 0 and int(data[i][rStack[-1]]) < curr:
                rStack.pop()
            if len(rStack) == 0:
                see[i][j] *= (len(data[i]) - 1 - j)
            else:
                see[i][j] *= abs(len(data[i]) - 1 - rStack[-1] - len(data[i]) - 1 - j)   
            rStack.append(j) 
            
            while len(cStacks[j]) > 0 and int(data[cStacks[j][-1]][j]) < curr:
                cStacks[j].pop()
            if len(cStacks[j]) == 0:
                see[i][j] *= (n - i)
            else:
                see[i][j] *= abs(n - cStacks[j][-1] - (n - i))   
            cStacks[j].append(i)
    
    #max
    score=0
    for row in see:
        for col in row:
            score = max(score, col)
    
    return score

if __name__ == "__main__":
    print(solution1())
    print(solution2())