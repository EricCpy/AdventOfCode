import functools

def solution():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    ans = 0
    allLists = []
    for i, x in enumerate(data[::3]):
        l1 = eval(x)
        l2 = eval(data[i*3 + 1])
        allLists.append(l1)
        allLists.append(l2)
        if compareLists(l1, l2) == 1:
            ans += i + 1

    allLists.append([[2]])
    allLists.append([[6]])
    
    allLists.sort(key=functools.cmp_to_key(compareLists), reverse=True)
    i,j = 0,0
    for x in range(len(allLists)):
        if allLists[x] == [[2]]:
            i = x + 1
        elif allLists[x]== [[6]]:
            j = x + 1     

    return ans, i*j

def compareLists(l1, l2):
    for i in range(min(len(l1), len(l2))):
        if isinstance(l1[i], list) or isinstance(l2[i], list):
            x = 0
            if isinstance(l2[i], int):
                x = compareLists(l1[i], [l2[i]])
            elif isinstance(l1[i], int):
                x = compareLists([l1[i]], l2[i])  
            else:
                x = compareLists(l1[i], l2[i])
                
            if x == 1:
                return 1
            elif x == -1:
                return -1
        else:
            if l1[i] < l2[i]: return 1
            elif l1[i] > l2[i]: return -1
            
    if len(l1) < len(l2):
        return 1
    elif len(l1) > len(l2):
        return -1
            
    return 0
                
                 
if __name__ == "__main__":
    print(solution())