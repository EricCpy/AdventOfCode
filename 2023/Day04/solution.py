def solution_1():
    with open('./Day04/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    res = 0
    for x in data:
        needed_have = x.split('|')
        needed = set(needed_have[0].split(':')[1].split(' '))
        have = set(needed_have[1].split(' '))
        needed.remove('')
        have.remove('')
        union = needed & have
        if len(union) > 0:
            res += 2 ** (len(needed & have) - 1)
        
        
        
    return res

def solution_2():
    with open('./Day04/input.txt', 'r') as f:
        data = f.read().splitlines()

    res = 0
    
    cards = {i + 1: 1 for i in range(len(data))}
    for i, x in enumerate(data):
        needed_have = x.split('|')
        needed = set(needed_have[0].split(':')[1].split(' '))
        have = set(needed_have[1].split(' '))
        union = needed & have
        union.remove('')
        
        for f in range(len(union)):
            curr = i + f + 2
            if curr in cards:
                cards[curr] += cards[i + 1]
            
        res += cards[i + 1]
    
    return res


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())