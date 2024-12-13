def solution():
    with open('./Day13/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    results = []
    
    for i in range(0, len(data), 4):
        a_split = data[i].split(": ")[1].split(" ")
        b_split = data[i + 1].split(": ")[1].split(" ")
        result_split = data[i + 2].split(": ")[1].split(" ")
        
        a = [int(a_split[0][2:-1]), int(a_split[1][2:])]
        b = [int(b_split[0][2:-1]), int(b_split[1][2:])]
        results_val = [int(result_split[0][2:-1]), int(result_split[1][2:])]
        
        min_cost = 801
        optimal_x1, optimal_x2 = -1, -1
        
        for x1 in range(0, 100): 
            x2_1 = (results_val[0] - a[0] * x1) / b[0]
            if x2_1.is_integer() and 0 <= x2_1 < 100:
                x2_1 = int(x2_1)
                
                if a[1] * x1 + b[1] * x2_1 == results_val[1]:
                    current_cost = 3 * x1 + x2_1
                    if current_cost < min_cost:
                        min_cost = current_cost
                        optimal_x1, optimal_x2 = x1, x2_1
        
        results.append((optimal_x1, optimal_x2, min_cost))
    
    return sum(result[2] for result in results if result[2] <= 800)


def solution2():
    with open('./Day13/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    ans = 0
    
    for i in range(0, len(data), 4):
        a_split = data[i].split(": ")[1].split(" ")
        b_split = data[i + 1].split(": ")[1].split(" ")
        result_split = data[i + 2].split(": ")[1].split(" ")
        
        a = [int(a_split[0][2:-1]), int(a_split[1][2:])]
        b = [int(b_split[0][2:-1]), int(b_split[1][2:])]
        results_val = [int(result_split[0][2:-1]) + 10000000000000, int(result_split[1][2:]) + 10000000000000]
        
        anumerator = results_val[0] * b[1] - results_val[1] * b[0]
        adenominator = a[0] * b[1] - b[0] * a[1]
        bnumerator = results_val[0] * a[1] - results_val[1] * a[0]
        bdenominator = a[1] * b[0] - b[1] * a[0]
        if anumerator % adenominator or bnumerator % bdenominator:
            continue
        a = anumerator // adenominator
        b = bnumerator // bdenominator
        ans += 3 * a + b
    
    return ans


if __name__ == "__main__":
    print(solution())
    print(solution2())