from functools import cmp_to_key
from collections import Counter


def solution_1():
    with open('./Day07/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    cards = [(x.split(' ')[0],int(x.split(' ')[1]))  for x in data]
    cards_sorted = sorted(cards, key=cmp_to_key(custom_compare))

    ans = 0
    for i, x in enumerate(cards_sorted):
        ans += (i + 1) * x[1]

    return ans
    
rank = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
def custom_compare(a: str, b: str):
    funcs= [five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card]
    min_a = 10
    min_b = 10

    counts_a = Counter(a[0])
    counts_b = Counter(b[0])
    set_a = set(set_transformer(counts_a))
    set_b = set(set_transformer(counts_b))
    for i, x in enumerate(funcs):
        if x(set_a, counts_a):
            min_a = min(min_a, i)
        if x(set_b, counts_b):
            min_b = min(min_b, i)
        
    
    if min_a > min_b:
        return -1
    elif min_a < min_b:
        return 1
    else:
        for x, y in zip(a[0], b[0]):
            x = rank.index(x)
            y = rank.index(y)
            
            if x > y:
                return -1
            elif x < y:
                return 1
         
        return 0

def set_transformer(b):
    c = 0
    if "J" in b:
        c = b["J"]
        del b["J"]
        
    best = ""
    for i in b:
        if best == "":
            best = i
            continue
        if b[best] < b[i]:
            best = i
    
    b[best] += c

    return set(b.values()) 

def five_of_a_kind(a,b):
    
    return set(b.values()) == {5}
    
def four_of_a_kind(a,b):
    return a == {4,1}
    
def full_house(a,b):
    return a == {3,2}
    
def three_of_a_kind(a,b):
    return a == {3,1}
    
def two_pair(a,b):
    two = 0
    for x in b.values():
        if x == 2:
            two += 1
    return two == 2

def one_pair(a,b):
    return a == {2,1}
    
def high_card(a,b):
    return a == {1}

if __name__ == "__main__":
    print(solution_1())
