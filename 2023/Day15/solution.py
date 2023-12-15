def solution():
    with open('./Day15/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    return sum([hash_algo(x) for x in data[0].split(',')])

def hash_algo(s: str):
    curr = 0
    for x in s:
        curr += ord(x)
        curr = (curr * 17) % 256
        
    return curr
     
if __name__ == "__main__":
    print(solution())
