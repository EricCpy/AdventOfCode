import json

def solution():
    with open('./Day19/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    workflows = {}
    for x in data: 
        if x == '':
            break

        split = x[:-1].split('{')
        name = split[0]
        conditions = split[1].split(',')
        conditions_processed = []
        for idx, cond in enumerate(conditions):
            if idx == len(conditions) - 1:
                conditions_processed.append(cond)
                continue
            
            a = cond[0]
            b = cond[1]
            split_cond = cond[2:].split(':')
            c = int(split_cond[0])
            d = split_cond[1]
            
            curr = (a,b,c,d)
            conditions_processed.append(curr)
        
        workflows[name] = conditions_processed
            
    ans = 0
    # ranges und recursiv durchgehen
    
    return ans
    
if __name__ == "__main__":
    print(solution())
