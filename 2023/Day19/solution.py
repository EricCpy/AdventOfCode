import json

def solution():
    with open('./Day19/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    workflows = {}
    ratings = []
    add_ratings = False
    for x in data: 
        if x == '':
            add_ratings = True
            continue
        
        if add_ratings:
            modified_x = '{"' + x[1:-1].replace('=', '":"').replace(',', '","') + '"}'
            rating_dict = json.loads(modified_x)
            ratings.append(rating_dict)
        else:    
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
    for rating in ratings:
        curr = "in"
        while curr != "R" and curr != "A":
            workflow = workflows[curr]
            for idx, i in enumerate(workflow):
                if idx == len(workflow) - 1:
                    curr = i
                    continue
                if i[1] == '<' and int(rating[i[0]]) < i[2]:
                    curr = i[3]
                    break
                elif i[1] == '>' and int(rating[i[0]]) > i[2]:
                    curr = i[3]
                    break
            
        if curr == "A":
            #print(rating)
            for x in rating.values():
                ans += int(x)        
        
    return ans
    
if __name__ == "__main__":
    print(solution())
