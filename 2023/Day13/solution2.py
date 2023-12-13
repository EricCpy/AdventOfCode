def solution():
    with open('./Day13/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    patterns= []
    pattern = []
    for x in data:
        if x == '':
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(x)
    
    patterns.append(pattern)
    ans = 0
    for p in patterns:
        rp = row_pattern(p)
        if rp != -1:
           ans += 100 * rp
       
        cp = col_pattern(p)
        if cp != -1:
            ans += cp 

    
    return ans

def col_pattern(pattern):
    m = -1
    for i in range(len(pattern[0]) - 1):
        column_data1 = "".join([row[i] for row in pattern])
        column_data2 = "".join([row[i + 1] for row in pattern])
        curr_diff = get_difference(column_data2, column_data1)
        
        if curr_diff <= 1:
            r = True
            j = 0
            while i - j - 1 >= 0 and i + 2 + j < len(pattern[0]):
                column_data1j = "".join([row[i -1 - j] for row in pattern])
                column_data2j = "".join([row[i + 2 + j] for row in pattern])
                curr_diff += get_difference(column_data2j, column_data1j)
                if curr_diff > 1: 
                    break
                j+=1

            if curr_diff == 1:
                m = max(m, i + 1)
    
    return m
    
    
def row_pattern(pattern):
    m = -1
    for i in range(len(pattern) - 1):
        curr_diff = get_difference(pattern[i], pattern[i+1])
        if curr_diff <= 1:
            j = 0
            while i - j - 1 >= 0 and i+ 2+ j < len(pattern):
                curr_diff += get_difference(pattern[i -j - 1], pattern[i + 2 + j])
                if curr_diff > 1: 
                    break
                j+=1
            if curr_diff == 1:
                m = max(m, i + 1)

    return m

def get_difference(pattern1, pattern2):
    diff = 0
    for i, j in zip(pattern1, pattern2):
        if i != j:
            diff += 1
    return diff
     
if __name__ == "__main__":
    print(solution())
