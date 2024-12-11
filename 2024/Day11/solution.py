def solution(blinks):
    with open('./Day11/input.txt', 'r') as f:
        data = f.read()
    
    curr = data.split(" ")
    for _ in range(blinks):
        ncurr = []
        for x in curr:
            count_digits = len(x)
            if x == "0":
                ncurr.append("1")
            elif count_digits % 2 == 0:
                ncurr.append(x[:count_digits // 2])
                ncurr.append(str(int(x[count_digits // 2:])))
            else:
                ncurr.append(str(int(x) * 2024))

        curr = ncurr
    
    return len(curr)

def solution2(blinks):
    def calculate_contributions(num, blinks_left, cache):
        if blinks_left == 0:
            return 1

        if (num, blinks_left) in cache:
            return cache[(num, blinks_left)]

        if num == "0":
            contributions = calculate_contributions("1", blinks_left - 1, cache)   
        else:
            count_digits = len(num)
            if count_digits % 2 == 0:
                mid = count_digits // 2
                part1 = num[:mid]
                part2 = str(int(num[mid:]))
                contributions = (
                    calculate_contributions(part1, blinks_left - 1, cache)
                    + calculate_contributions(part2, blinks_left - 1, cache)
                )
            else:
                multiplied = str(int(num) * 2024)
                contributions = calculate_contributions(multiplied, blinks_left - 1, cache)

        cache[(num, blinks_left)] = contributions
        return contributions
    

    with open('./Day11/input.txt', 'r') as f:
        data = f.read().split(" ")

    cache = {} # memorization

    total_count = 0
    for num in data:
        total_count += calculate_contributions(num, blinks, cache)

    return total_count
    

if __name__ == "__main__":
    print(solution(25))
    print(solution2(75))