def solution_1():
    with open('./Day03/input.txt', 'r') as f:
        data = f.read().splitlines()
 
    num = ""
    res = 0
    not_numeric = lambda x : x != '.' and not x.isnumeric()
    special = False
    for i in range(len(data)):
        for j, x in enumerate(data[i]):
            if x.isnumeric():
                num += x
                if not special:
                    special = (not_numeric(data[i][j - 1]) if j - 1 >= 0 else False) \
                            or (not_numeric(data[i][j + 1]) if j + 1 < len(data[i]) else False) \
                            or (not_numeric(data[i + 1][j]) if i + 1 < len(data) else False) \
                            or (not_numeric(data[i + 1][j + 1]) if i + 1 < len(data) and j + 1 < len(data[i]) else False) \
                            or (not_numeric(data[i + 1][j - 1]) if i + 1 < len(data) and j - 1 >= 0 else False) \
                            or (not_numeric(data[i - 1][j]) if i - 1 >= 0 else False) \
                            or (not_numeric(data[i - 1][j + 1]) if i - 1 >= 0 and j + 1 < len(data[i]) else False) \
                            or (not_numeric(data[i - 1][j - 1]) if i - 1 >= 0 and j - 1 >= 0 else False)
                
            elif len(num) > 0:
                if special:
                    res += int(num)
                
                special = False
                num = ""
    
    if len(num) > 0 and special:
        res += int(num)
        
    return res


def solution_2():
    with open('./Day03/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    moves = [(1,1), (-1,-1), (-1,1), (1,-1), (-1,0), (1,0), (0, 1), (0, -1)]
    
    num = ""
    res = 0
    star_dict = dict()
    stars = set()
    for i in range(len(data)):
        for j, x in enumerate(data[i]):
            if x.isnumeric():
                num += x
                for move in moves:
                    curr = (i + move[0], j + move[1])
                    if curr[0] >= 0 and curr[0] < len(data) and curr[1] >= 0 and curr[1] < len(data[i]) and data[curr[0]][curr[1]] == '*':
                        stars.add(curr)                    
                
            elif len(num) > 0:
                num_int = int(num)
                for star in stars:
                    if star not in star_dict:
                        star_dict[star] = []
                    star_dict[star].append(num_int)
                     
                stars = set()
                num = ""
    
    if len(num) > 0:
        num_int = int(num)
        for star in stars:
            if star not in star_dict:
                star_dict[star] = []
            star_dict[star].append(num_int)
    
    for num_list in star_dict.values():
        if len(num_list) == 2:
            res += num_list[0] * num_list[1]
    
    return res

if __name__ == "__main__":
    print(solution_1())
    print(solution_2())