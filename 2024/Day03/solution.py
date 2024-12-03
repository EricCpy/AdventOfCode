import re

def solution():
    with open('./Day03/input.txt', 'r') as f:
        data = f.read()
    
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
    return sum(int(x[0]) * int(x[1]) for x in matches)

def solution2():
    with open('./Day03/input.txt', 'r') as f:
        data = f.read()
        
    matches = re.finditer(r"(?:mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", data)
    do = True
    ans = 0
    for match in matches:
        x = match.groups()
        if not x[0]:
            do = True if match.group() == 'do()' else False 
        elif do:
            ans += int(x[0]) * int(x[1])
            
    return ans

if __name__ == "__main__":
    print(solution())
    print(solution2())