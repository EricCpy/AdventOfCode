from collections import Counter

def solution(start):
    with open('input.txt', 'r') as f:
        data = f.read()
    
    dic = Counter(data[:start])
    for i, x in enumerate(data[start:],start):
        if len(dic) == start:
            return i
        
        dic.subtract(data[i-start])
        dic.update({x : 1})
        if dic[data[i-start]] == 0:
            del dic[data[i-start]]
    
    if len(dic) == start:
        return len(data)
    
    return -1

if __name__ == "__main__":
    print(solution(4))
    print(solution(14))