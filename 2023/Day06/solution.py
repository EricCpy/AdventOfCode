def solution_1():
    with open('./Day06/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    times = prepare_input(data[0].split(':')[1])
    distances = prepare_input(data[1].split(':')[1])
    prod = 1
    for i, t in enumerate(times):
        curr = 0
        for x in range(t):
            if x * (times[i] - x) > distances[i]:
                curr += 1

        prod *= max(1, curr)
        
    return prod   

def prepare_input(data):
    ans = []
    curr = ""
    for x in data:
        if x.isnumeric():
            curr += x
        elif curr != "":
            ans.append(int(curr))
            curr = ""
            
    ans.append(int(curr))
    return ans

def solution_2():
    with open('./Day06/input.txt', 'r') as f:
        data = f.read().splitlines()

    time = int(data[0].split(':')[1].replace(" ", ""))
    distance = int(data[1].split(':')[1].replace(" ", ""))
    prod = 0
    for x in range(time):
        if x * (time - x) > distance:
            prod += 1
        
    return prod

if __name__ == "__main__":
    print(solution_1())
    print(solution_2())