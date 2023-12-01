def solution():
    with open('test.txt', 'r') as f:
        data = f.read().splitlines()

    #intialize 
    flowDict = dict() #key -> AA : value -> (flowdata, [BB,CC,DD])
    for x in data:
        s = x.split(' ')
        tunnels = [s[-1]]
        for t in s[9:-1]:
            tunnels.append(t[:-1])
        
        flowDict[s[1]] = (int(s[4].split('=')[-1][:-1]), tunnels)
    
    ans = dfs(flowDict, 'AA', 0, 30, set())
    return ans
    

def dfs(flow, tunnel, value, timeLeft, opened):
    if timeLeft == 0:
        return value
    if timeLeft < 0:
        return 0
    openValue = flow[tunnel][0] * timeLeft
    m = 0
    for x in flow[tunnel][1]:
        m = max(dfs(flow, x, value, timeLeft-1, opened), m)
        if flow[tunnel][0] > 0 and tunnel not in opened: 
            opened.add(tunnel)
            m = max(m, dfs(flow, x, openValue, timeLeft-2, opened))
            opened.remove(tunnel)
    
    return m


if __name__ == "__main__":
    print(solution())