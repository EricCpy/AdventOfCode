def solution():
    def can_build(cache, available, needed, position, m):
        if position in cache:
            return cache[position]
        
        if len(needed) == 0:
            cache[position] = True
            return True
        
        for i in range(1, min(m + 1, len(needed) + 1)):
            if needed[:i] in available and can_build(cache, available, needed[i:], position + i, m):
                cache[position] = True
                return True
        
        cache[position] = False
        return False

    with open('./Day19/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    available = set(data[0].split(", "))
    m = max(len(x) for x in available)
    
    ans = 0
    for x in data[2:]:
        cache = {} 
        if can_build(cache, available, x, 0, m):
            ans += 1
    
    return ans


def solution2():
    def count_ways(cache, available, needed, position, m):
        if position in cache:
            return cache[position]
        
        if len(needed) == 0:
            return 1
        
        total_ways = 0
        for i in range(1, min(m + 1, len(needed) + 1)):
            current = needed[:i]                
            if current in available:
                total_ways += count_ways(cache, available, needed[i:], position + i, m)
        
        cache[position] = total_ways
        return total_ways

    with open('./Day19/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    available = set(data[0].split(", "))
    m = max(len(x) for x in available)
    
    total_count = 0
    for x in data[2:]:
        cache = {} 
        total_count += count_ways(cache, available, x, 0, m)
    
    return total_count


if __name__ == "__main__":
    print(solution())
    print(solution2())