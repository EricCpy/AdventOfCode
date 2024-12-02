from collections import Counter

def solution():
    with open('./Day01/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    l1 = sorted([x.split("   ")[0] for x in data])
    l2 = sorted([x.split("   ")[1] for x in data])
    dist = 0
    for x, y in zip(l1, l2):
        dist += abs(int(x) - int(y))
    
    return dist

def solution2():
    with open('./Day01/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    l1 = sorted([x.split("   ")[0] for x in data])
    l2 = sorted([x.split("   ")[1] for x in data])
    
    count_dict1 = Counter(l1)
    count_dict2 = Counter(l2)  
    return sum(int(count_dict1[x]) * int(x) * int(count_dict2.get(x, 0)) for x in count_dict1)

if __name__ == "__main__":
    print(solution())
    print(solution2())