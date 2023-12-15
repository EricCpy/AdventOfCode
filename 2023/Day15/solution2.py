def solution():
    with open('./Day15/input.txt', 'r') as f:
        data = f.read().splitlines()
    boxes :dict[int, list[tuple[str, int]]]= {}
    for x in data[0].split(','):
        key = ""
        op = "="
        val = 0
        for idx, i in enumerate(x):
            if i == "=" or i == "-":
                op = i
                if i == "=":
                    val = int(x[idx + 1:])
                break
            key += i
            
        key_hashed = hash_algo(key)
        if op == "=": 
            if key_hashed not in boxes:
                boxes[key_hashed] = []
            added = False
            for idx, ff in enumerate(boxes[key_hashed]):
                if ff[0] == key:
                    boxes[key_hashed][idx] = (key, val)
                    added = True
                    break
            if (not added):
                boxes[key_hashed].append((key, val))
        else:
            if key_hashed in boxes: 
                for ff in boxes[key_hashed]:
                    if ff[0] == key:
                        boxes[key_hashed].remove(ff)
                        break

    ans = 0    
    for box in boxes.keys():
        curr_box = box + 1
        for idx, x in enumerate(boxes[box]):
            ans += (idx + 1) * curr_box * x[1]    
    
    return ans

def hash_algo(s: str):
    curr = 0
    for x in s:
        curr += ord(x)
        curr = (curr * 17) % 256
        
    return curr
     
if __name__ == "__main__":
    print(solution())
