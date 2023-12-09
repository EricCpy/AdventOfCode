def solution():
    with open('./Day09/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    ans = 0
    for x in data:
        currs = [[int(a) for a in x.split(' ')]]
        while any(a != 0 for a in currs[len(currs) - 1]):
            n_curr = []
            for i in range(len(currs[len(currs) - 1]) - 1 ):
                n_curr.append(currs[len(currs)-1][i + 1] - currs[len(currs)-1][i])
            currs.append(n_curr)   

        tmp = 0
        for x in reversed(currs[:-1]):
            tmp = x[0] - tmp 
            
        ans += tmp

    return ans
    
if __name__ == "__main__":
    print(solution())